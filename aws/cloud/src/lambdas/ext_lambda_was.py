import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": 
        json.dumps(
            {
                "Configuration": {
                    "FunctionName": "nu0284001-artemis-dev-copy-skills-lambda",
                    "FunctionArn": "arn:aws:lambda:us-east-1:200839614099:function:nu0284001-artemis-dev-copy-skills-lambda",
                    "Runtime": "python3.9",
                    "Role": "arn:aws:iam::200839614099:role/nu0284001-artemis-dev-copy-skills-lambda-role",
                    "Handler": "app.handler",
                    "CodeSize": 17097338,
                    "Description": "Lambda para mover y firmar el pickle de skills",
                    "Timeout": 900,
                    "MemorySize": 512,
                    "LastModified": "2025-03-19T22:10:48.478+0000",
                    "CodeSha256": "pdH9c9T7lIieb7mID9LVBemSSRDoHbnkzDMil2I1Fdg=",
                    "Version": "$LATEST",
                    "VpcConfig": {
                        "SubnetIds": [
                            "subnet-05d0913191415e0df",
                            "subnet-039e82818731426ca"
                        ],
                        "SecurityGroupIds": [
                            "sg-002120d29103e1069"
                        ],
                        "VpcId": "vpc-0282c775421a7b255",
                        "Ipv6AllowedForDualStack": false
                    },
                    "TracingConfig": {
                        "Mode": "PassThrough"
                    },
                    "RevisionId": "99026735-15c7-49ca-9e23-498ad530149b",
                    "Layers": [
                        {
                            "Arn": "arn:aws:lambda:us-east-1:200839614099:layer:PrismaDefender_python_14695981039346656037_31_01_123:1",
                            "CodeSize": 1836985
                        }
                    ],
                    "State": "Active",
                    "LastUpdateStatus": "Successful",
                    "PackageType": "Zip",
                    "Architectures": [
                        "x86_64"
                    ],
                    "EphemeralStorage": {
                        "Size": 512
                    },
                    "SnapStart": {
                        "ApplyOn": "None",
                        "OptimizationStatus": "Off"
                    },
                    "RuntimeVersionConfig": {
                        "RuntimeVersionArn": "arn:aws:lambda:us-east-1::runtime:d6dc717114b06da7d4b5a2df328222709ec4fad2853004fac301b8b63a65c084"
                    },
                    "LoggingConfig": {
                        "LogFormat": "Text",
                        "LogGroup": "/aws/lambda/nu0284001-artemis-dev-copy-skills-lambda"
                    }
                },
                "Code": {
                    "RepositoryType": "S3",
                    "Location": "https://prod-04-2014-tasks.s3.us-east-1.amazonaws.com/snapshots/200839614099/nu0284001-artemis-dev-copy-skills-lambda-45cd35e9-4993-4af5-88b7-74b21958dc1d?versionId=HL861uzjltLg5XTBtF8isDX5z9eegcgj&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIBRr0gWnlLZJDQv%2Bqm40h8m4uf05NsjjdbMNeNjVN8BWAiB5B1jMLHJE23PZ4Xi00xq37Ls9Cq%2BJfNhm51lwVmYLuyqJAggtEAAaDDc0OTY3ODkwMjgzOSIMC1DmxwtG4fXFZFmoKuYBXPNLL1tDUtcBIQyLCDFFmwNv4uvxYD0hFiUZhR1r1C5f2bBQZHKKoq7k2CGBk%2Bt8X2ovTH9W42uuR2JZtSenZUw1Kn1WOiehaHNuWCxrghk4pu2gHvFJlGCqhcHxi2kKBQ4nOLSy0rtPiYoct20NSkDew2y68Tm93%2BIASz9sYti8H4DVkgYJcPzLZAMqJGRPAqLTJ0zdahPQh6ZlbwHXcY9W0g56HjorSlUfvIE2AKNE4hBa%2FsHVFuj9aCE8KXPTgcX%2BPV2JWtjYnPFxiam0GPSK6CAVJlpZdB49BqR3zRxMVsMLwXYw4dGPvwY6kAGIYLRfoGtZPo3P76qlKKoxm14kB6FeQQdV7YQ6SU8VqSM7RpX5yZQZz%2Fz6UuTXyyaQQNMEf6vXXdCdyIHojHJKZ9wzvbS3ifgIh6JMQRu8M86uQ0wvl51w9oFm9Rj4%2FlPpC%2FIcEiSmWxcCrWxA%2FIQ9x40UTNJc1kyOIuQ1plk3PBiJutT2O54j%2FKIgvWh4b4E%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250326T223825Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIA25DCYHY3YSIWPQVV%2F20250326%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=1bf026e88f3577516449bc0f56a41951f4c0ee74ba79cb971785240757cf672e"
                },
                "Tags": {
                    "azure-devops:repository": "Cloud_nu0284001_artemis",
                    "bancolombia:project-name": "artemis",
                    "aws:cloudformation:stack-name": "nu0284001-artemis-dev-content",
                    "azure-devops:pipeline-id": "18866",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-east-1:200839614099:stack/nu0284001-artemis-dev-content/9304bee0-a7be-11ed-99f8-0efcee6db611",
                    "bancolombia:responsible": "ldc-fc-sistemas-generativos-ia-ti",
                    "bancolombia:clasificacion-disponibilidad": "impacto tolerable",
                    "bancolombia:environment": "dev",
                    "bancolombia:application-code": "nu0284001",
                    "azure-devops:creator-email": "ejrueda@bancolombia.com.co",
                    "aws:cloudformation:logical-id": "CopySkillsLambda",
                    "bancolombia:cost-center": "c103500368",
                    "bancolombia:clasificacion-integridad": "impacto tolerable",
                    "bancolombia:clasificacion-confidencialidad": "interna"
                }
            }
        ),
    }
