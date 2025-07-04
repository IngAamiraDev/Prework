# Docker

## Crear BD Postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres

## Verifica que PostgreSQL esté funcionando:
docker ps | grep postgres

# Ver logs de PostgreSQL
docker logs some-postgres

# Ver logs de LocalStack
docker logs localstack

# Reiniciar servicios
docker restart some-postgres

## Iniciar servicios
docker start some-postgres

## Detener todos los Docker
docker stop $(docker ps -q)