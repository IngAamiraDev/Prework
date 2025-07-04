# Migración de datos de DynamoDB a S3

## Pre-requisitos
1. Python 3.8 o superior
2. Node.js 14 o superior

## Instalar las dependencias de Nodejs:
```sh
cd scan_dynamodb
npm install
cd ..
```

## Recomendaciones:
1. Si se va a ejecutar el script desde la terminal
Se debe hacer desde la raíz del proyecto, es decir, desde la carpeta que contiene el archivo `README.md`. Esto asegura que las rutas relativas funcionen correctamente.
2. Si se va a ejecutar el script en debugger
Para evitar problemas con rutas relativas, se recomienda usar rutas absolutas. En este caso, se define la ruta del proyecto y la ruta de los datos de la siguiente manera:
```python
import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root directory
PATH_DATA = os.path.join(PROJECT_ROOT, "temp")  # Absolute path to 'temp'
```

# Lectura de datos desde dynamoDB
1. Configurar el perfil de lectura de dynamodb en AWS CLI con el siguiente comando:
```sh
aws configure sso
```
- SSO session name: bank
- SSO start URL [None]: https://d-9067080964.awsapps.com/start#
- CLI profile name [None]: info-pdn-read-dy
2. Modificar el nombre de la tabla y el canal en el app_v3.js
3. Ejecutar el scripts de lectura:
```sh
node ./scan_dynamodb/app.js
```
Los datos son guardados en la carpeta `temp/s3/$(channel)`

## Guardar datos en Zip (Opcional)
Nota: Recomendado para reducir el tamaño de los datos. A partir de este paso, en los siguientes scripts se debe seleccionar la opción de leer desde el zip (0).
1. Ejecutar el siguiente comando para comprimir los datos leídos desde dynamodb:
```sh
python ./save_data_zip/app.py
```

# Migración a s3
1. Ejecutar el script de división por fecha:
```sh
python ./split_s3/app.py
```
Los datos se dividirán por fecha y se guardan en la carpeta `temp/s3/upload/(channel)` y además se guardará los registros a eliminar en la carpeta `temp/dynamodb/$(channel)`
2. Ejecutar el siguiente comando para hacer el merge de los archivos:
```sh
python ./merge_s3/app.py
```
2. Configurar el perfil de s3 en AWS CLI con el siguiente comando:
```sh
aws configure sso
```
- SSO session name: bank
- SSO start URL [None]: https://d-9067080964.awsapps.com/start#
- CLI profile name [None]: info-pdn-write-s3
3. Ejecutar el siguiente comando para empezar la migración al s3
```sh
cd temp/s3/upload
aws s3 sync . s3://aw1165001-tabot-pdn-events --profile=info-pdn-write-s3
```

# Eliminación de directorio/archivos subidos a s3 desde el sistema
1. Copiar el log de los archivos subidos a s3 en `temp/s3/data/upload_s3.txt`
    Nota: Este archivo debe estar vacío antes de iniciar la ejecución del script.
2. Ejecutar el siguiente comando para eliminar los archivos subidos a s3 desde otra terminal:
```sh
python ./delete_files/app.py
```
Nota: Este script deja los logs de los archivos/directorios que se subieron a s3 y los elimina del sistema.

# Eliminación de registros dynamodb
1. Configurar el perfil de s3 en AWS CLI con el siguiente comando:
```sh
aws configure sso
```
- SSO session name: bank
- SSO start URL [None]: https://d-9067080964.awsapps.com/start#
- CLI profile name [None]: info-pdn-write-dy
1. Ejecutar el scripts de eliminación
```sh
python ./delete_dynamodb/app_v2.py
```
