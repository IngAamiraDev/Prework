import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": 
        json.dumps(
            {
                "Configuration": {
                    "FunctionName": "mi-app-mi-lambda",
                    "FunctionArn": "arn:aws:lambda:us-east-1:<AWS_ACCOUNT_ID>:function:mi-app-mi-lambda",
                    "Runtime": "python3.9",
                    "Role": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/mi-app-mi-lambda-role",
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
                            "<SUBNET_ID>",
                            "<SUBNET_ID>"
                        ],
                        "SecurityGroupIds": [
                            "<SECURITY_GROUP_ID>"
                        ],
                        "VpcId": "<VPC_ID>",
                        "Ipv6AllowedForDualStack": False
                    },
                    "TracingConfig": {
                        "Mode": "PassThrough"
                    },
                    "RevisionId": "99026735-15c7-49ca-9e23-498ad530149b",
                    "Layers": [
                        {
                            "Arn": "arn:aws:lambda:us-east-1:<AWS_ACCOUNT_ID>:layer:PrismaDefender_python_14695981039346656037_31_01_123:1",
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
                        "LogGroup": "/aws/lambda/mi-app-mi-lambda"
                    }
                },
                "Code": {
                    "RepositoryType": "S3",
                    "Location": "<URL_PRESIGNADA_REMOVIDA>"
                },
                "Tags": {
                    "azure-devops:repository": "Mi_Repositorio",
                    "<ORGANIZACION>:project-name": "<PROYECTO>",
                    "aws:cloudformation:stack-name": "mi-stack-contenido",
                    "azure-devops:pipeline-id": "<PIPELINE_ID_REMOVIDO>",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-east-1:<AWS_ACCOUNT_ID>:stack/mi-stack-contenido/9304bee0-a7be-11ed-99f8-0efcee6db611",
                    "<ORGANIZACION>:responsible": "<EQUIPO_REMOVIDO>",
                    "<ORGANIZACION>:clasificacion-disponibilidad": "impacto tolerable",
                    "<ORGANIZACION>:environment": "dev",
                    "<ORGANIZACION>:application-code": "<CODIGO_APLICACION>",
                    "azure-devops:creator-email": "<CORREO_CORPORATIVO_REMOVIDO>",
                    "aws:cloudformation:logical-id": "CopySkillsLambda",
                    "<ORGANIZACION>:cost-center": "<CENTRO_COSTO_REMOVIDO>",
                    "<ORGANIZACION>:clasificacion-integridad": "impacto tolerable",
                    "<ORGANIZACION>:clasificacion-confidencialidad": "interna"
                }
            }
        ),
    }
