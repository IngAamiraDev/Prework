process.env["AWS_PROFILE"] = "info-pdn-read-dy";
const fs = require("fs");
const crypto = require("crypto");
const { parallelScanAsStream } = require("@shelf/dynamodb-parallel-scan");

const start = Date.now();
tableName = "tabot-aw1165001-events-cpc";
channel = "cpc";
(async () => {
  console.log("Scan started...");
  const stream = await parallelScanAsStream(
    {
      TableName: tableName,
    },
    { concurrency: 24, chunkSize: 10000, highWaterMark: 100000 }
  );

  for await (const items of stream) {
    fs.writeFile(
      `temp/s3/${channel}/${crypto.randomUUID()}.json`,
      JSON.stringify(items, (_key, value) =>
        typeof value === "bigint" ? parseFloat(value) : value
      ),
      (err) => {
        if (err) throw err;
      }
    );
  }
})();

process.on("exit", function () {
  console.log("Elapsed time: ", (Date.now() - start) / 1000, "seconds");
});

process.on("SIGINT", function () {
  process.exit();
});
