# 🔨 Instalación y Configuración de Node.js en WSL 🔨

## Tabla de Contenido
1. [¿Qué es Node.js?](#qué-es-nodejs)
2. [Instalación de Node.js](#instalación-de-nodejs)
3. [Remover Node.js](#remover-nodejs)
4. [Instalar paquetes de actualización](#instalar-paquetes-de-actualización)
5. [Instalar versión en específico usando el comando nvm](#instalar-versión-en-específico-usando-el-comando-nvm)
6. [Instalar la última versión](#instalar-la-última-versión)
7. [Instalar una versión específica con nvm](#instalar-una-versión-específica-con-nvm)
8. [Seleccionar la versión de Node.js en la sesión actual](#seleccionar-la-versión-de-nodejs-en-la-sesión-actual)
9. [Mostrar una lista de las versiones instaladas de Node.js](#mostrar-una-lista-de-las-versiones-instaladas-de-nodejs)
10. [Enumerar las versiones disponibles para la instalación](#enumerar-las-versiones-disponibles-para-la-instalación)
11. [Conclusión](#conclusión)

## 1. ¿Qué es Node.js? <a name="qué-es-nodejs"></a>
Node.js es un entorno en tiempo de ejecución multiplataforma para la capa del servidor (en el lado del servidor) basado en JavaScript que es un entorno controlado por eventos diseñado para crear aplicaciones escalables, permitiéndote establecer y gestionar múltiples conexiones al mismo tiempo.

## 2. Instalación de Node.js <a name="instalación-de-nodejs"></a>
Asegurémonos de que Node.js esté instalado en tu sistema y configuremos el entorno para trabajar con él.

- `sudo apt update` -> Servidores de software disponibles
- `sudo apt upgrade`
- `sudo apt install nodejs` -> Instala Node.js
- `node -v` -> Para conocer la versión de Node.js

## 3. Remover Node.js <a name="remover-nodejs"></a>
- `sudo apt remove nodejs` -> Para remover Node.js

## 4. Instalar paquetes de actualización <a name="instalar-paquetes-de-actualización"></a>
- `sudo apt install npm` -> Instala el manejador de paquetes de Node: npm 📥 
- `sudo npm install -g n` -> Se instala el paquete n que permite administrar las versiones de Node
- `sudo n latest` -> Para instalar la versión más actualizada disponible
- `sudo n install` + "número_de_versión" -> Para instalar una versión específica de Node (e.g. `sudo n install 15.2.1`)

## 5. Instalar versión en específico usando el comando nvm <a name="instalar-versión-en-específico-usando-el-comando-nvm"></a>
**Nota:** En caso de que no sirva con n, se puede usar el comando nvm. 
- Se puede realizar operaciones como instalar, desinstalar, cambiar de versión, etc, con Node Version Manager usando el comando nvm.
- `sudo apt install curl` -> Herramienta que permite transferir datos desde un servidor
- `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash`
- `reset` -> Reinicia la terminal con:

## 6. Instalar la última versión <a name="instalar-la-última-versión"></a>
- `nvm install --lts`
- `node` -v Se verifica la última versión instalada de Node.js:

## 7. Instalar una versión específica con nvm <a name="instalar-una-versión-específica-con-nvm"></a>
- `nvm install` + "número_de_versión" -> Para instalar una versión específica (e.g. `nvm install 16.15.0`)

## 8. Seleccionar la versión de Node.js en la sesión actual <a name="seleccionar-la-versión-de-nodejs-en-la-sesión-actual"></a>
- `nvm use` + "número_de_versión" -> Para instalar una versión específica (e.g. `nvm use 16.15.0`)

## 9. Mostrar una lista de las versiones instaladas de Node.js <a name="mostrar-una-lista-de-las-versiones-instaladas-de-nodejs"></a>
- `nvm ls`

## 10. Enumerar las versiones disponibles para la instalación <a name="enumerar-las-versiones-disponibles-para-la-instalación"></a>
- `nvm ls-remote`

## Conclusión <a name="conclusión"></a>
En este tutorial, has aprendido a instalar y configurar Node.js en Windows Subsystem for Linux (WSL). También has visto cómo administrar las versiones de Node.js usando Node Version Manager (nvm). 

¡Ahora estás listo para desarrollar aplicaciones con Node.js en WSL!