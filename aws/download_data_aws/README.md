# Prerequisitos
1. arn de dynamo o s3
2. Solicitar perfil a demanda según el caso, dynamo o s3
    * [Ejemplo Dynamo](https://grupobancolombia.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_build/results?buildId=9002802&view=results)
    * [Ejemplo S3](https://grupobancolombia.visualstudio.com/Vicepresidencia%20Servicios%20de%20Tecnolog%C3%ADa/_build/results?buildId=9002802&view=results)

**Nota:**
* Para lectura/escritura en s3/dyanmo son máximo 2hrs que se puede solicitar
* Para lectura en dynamo son máximo 24hrs
* Ajustar/Modificar el pipeline de acuerdo a lo requerido

# Descargar data de S3
1. Solicitar el perfil a demanda
2. Configurar los datos del perfil en `config/config.json`
3. Ajustar el nombre de la tabla
4. Ejecutar el siguiente script. Los datos se guardan en `temp/s3/{name_bucket}/`
```sh
python3 ./s3/app.py
```

# Descargar data de DynamoDB
1. Solicitar el perfil a demanda 
2. Configurar los datos del perfil en `config/config.json`
3. Ajustar el nombre del bucket y el nombre del canal
4. Ejecutar el siguiente script. Los datos se guardan en `temp/dynamodb/{name_table}/`
```sh
python3 ./dynamodb/app.py
```