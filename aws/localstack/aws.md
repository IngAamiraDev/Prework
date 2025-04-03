# Install AWS CLI-Local in WSL

## Install
pip install awscli-local[ver1]
pip install "awscli-local[ver1]"
pip install awscli-local

## Dynamodb

## Crear tabla
```bash
awslocal dynamodb create-table \
	        --table-name artemis-local-change-registry-dy \
	        --key-schema \
	            AttributeName=registry_id,KeyType=HASH \
	            AttributeName=promoter_datetime,KeyType=RANGE \
	        --attribute-definitions \
	            AttributeName=registry_id,AttributeType=S \
	            AttributeName=promoter_datetime,AttributeType=S \
	        --billing-mode PAY_PER_REQUEST \
    --region us-east-1
```

## Pasar json a localstack

### En la consola tomar la tabla
```bash
aws dynamodb describe-table --table-name arn:aws:dynamodb:us-east-1:200839614099:table/artemis-dev-prueba-api-dev-whatsapp-sessions-dy --region us-east-1
```

### Convertir JSON a un Comando AWS CLI
* Guardar el archivo json en un directorio
```bash
aws dynamodb create-table \
    --cli-input-json file://mi_tabla.json \
    --endpoint-url http://localhost:4566
```

## S3

### Crear bucket
aws --endpoint-url=http://localhost:4566 s3 mb s3://mi-bucket-local

awslocal s3api create-bucket --bucket artemis-local-versioned-pickle
awslocal s3api create-bucket --bucket artemis-multimedia-local
awslocal s3api create-bucket --bucket sofy-multimedia-local
awslocal s3api create-bucket --bucket tabot-multimedia-local
awslocal s3api create-bucket --bucket artemis-local-prototypes

awslocal s3api put-object --bucket sofy-multimedia-local --key teams/image/
awslocal s3api put-object --bucket sofy-multimedia-local --key webchat/image/
awslocal s3api put-object --bucket sofy-multimedia-local --key whatsapp/image/

### Lista los buckets creados
aws --endpoint-url=http://localhost:4566 s3 ls

aws --endpoint-url=http://localhost:4566 s3 ls s3://artemis-local-versioned-pickle/
aws --endpoint-url=http://localhost:4566 s3 ls s3://artemis-local-versioned-pickle/ --recursive

## Lambda Functions

### Instalar dependencias en el mismo directorio
pip install -r requirements.txt -t .

### Comprimir la Lambda
zip -r copy_skills_lambda.zip copy_skills_lambda -x "copy_skills_lambda/venv/*"

### Crear la lambda
awslocal lambda create-function \
    --function-name copy_skills_lambda \
    --runtime python3.8 \
    --role arn:aws:iam::000000000000:role/execution_role \
    --handler lambda_function.lambda_handler \
    --zip-file fileb:///mnt/c/amira/Bancolombia/Sprints/214/copy_skills_lambda.zip
    --region us-east-1

### Respuesta de la lambda
awslocal lambda invoke --function-name copy_skills_lambda response.json
cat response.json

## Revisar configuración AWS
ls .aws/
ls .aws/
cat .aws/config
cat .aws/credential
aws configure

## Recursos
- [AWS-CLI-Local](https://github.com/localstack/awscli-local)
