const fs = require("fs");
const path = require("path");
const archiver = require("archiver");

async function createZipAndClean(directoryPath) {
    if (!fs.existsSync(directoryPath)) {
        console.warn(`Directory ${directoryPath} does not exist. Skipping.`);
        return;
    }

    const zipPath = `${directoryPath}.zip`;
    const output = fs.createWriteStream(zipPath);
    const archive = archiver("zip", { zlib: { level: 9 } });

    return new Promise((resolve, reject) => {
        output.on("close", () => {
            console.log(`Zip created: ${zipPath} (${archive.pointer()} bytes)`);
            fs.rmSync(directoryPath, { recursive: true, force: true });
            console.log(`Directory ${directoryPath} deleted.`);
            resolve();
        });

        archive.on("error", (err) => {
            console.error(`Error creating zip: ${err.message}`);
            reject(err);
        });

        archive.pipe(output);
        archive.directory(directoryPath, false);
        archive.finalize();
    });
}

module.exports = { createZipAndClean };