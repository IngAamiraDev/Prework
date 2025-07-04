# Installl Local Stack With Docker
docker run \
--rm -it \
-p 127.0.0.1:4566:4566 \
-p 127.0.0.1:4510-4559:4510-4559 \
-v /var/run/docker.sock:/var/run/docker.sock \
localstack/localstack

## Ejecutar LocalStack directamente con Docker
docker run --rm -it -p 4566:4566 localstack/localstack
docker run --rm -it -p 4566:4566 -v $(pwd)/localstack_data:/var/localstack localstack/localstack

## Comprobar que LocalStack está respondiendo
curl http://localhost:4566/_localstack/health

## Verifica que LocalStack esté funcionando:
docker ps | grep localstack

## # Reiniciar servicios
docker restart localstack

## Recursos
- [Install Local-Stack](https://docs.localstack.cloud/getting-started/installation/)