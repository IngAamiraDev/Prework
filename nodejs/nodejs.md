# 🔨 Instalación de Node JS 🔨

## ¿Qué es Node.js? 📎

Node.js es un entorno en tiempo de ejecución multiplataforma para la capa del servidor (en el lado del servidor) basado en JavaScript que es un entorno controlado por eventos diseñado para crear aplicaciones escalables, permitiéndote establecer y gestionar múltiples conexiones al mismo tiempo.

## Instalación de Node.js 🪛
`sudo apt update`
`sudo apt upgrade`
`sudo apt install nodejs`
`node -v` -> Para conocer la versión de nodejs
`sudo apt remove nodejs` -> Para remover nodejs
`sudo apt install npm` -> Instalar el manejador de paquetes de Node: npm 📥 
`sudo npm install -g n` -> Se instala el paquete n que permite administrar las versiones de Node
`sudo n latest` -> Para instalar la versión más actualizada disponible, se ejecuta
`sudo n install` + "número_de_versión" -> Para instalar una versión especifica de Node (e.g. `sudo n install 15.2.1`)

Nota: en caso de que no sirva con n, se puede usar el comando nvm.
 
 
Instalar versión en específico usando el comando nvm 🔎
 
Fuente: aquí
 

Se puede realizar operaciones como instalar, desinstalar, cambiar de versión, etc, con Node Version Manager usando el comando nvm.
 
Para instalar nvm, se debe instalar primero curl que es una herramienta que permite transferir data desde un servidor, colocar en la terminal:
sudo apt install curl
 

Luego poner:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
 

Se reinicia la terminal con:
reset
 

Para instalar la última versión:
nvm install --lts 									
 

Se verifica la última versión instalada de nodejs:
node -v
 

Para instalar una versión específica con nvm:
nvm install <número_de_versión>
 
Por ejemplo 16.15.0 se le puede especificar al comando de instalación:
nvm install 16.15.0
 

Para mostrar en una lista las versiones instaladas de nodejs:
nvm ls
 

Para enumerar las versiones disponibles para la instalación (la lista es larga):
nvm ls-remote
 

Para seleccionar la versión de node ya instalada previamente solo en la sesión actual:
nvm use <número_de_versión>
Por ejemplo si se tiene instalada actualmente la versión 18.16.0 y se quiere usar la 16.15.0, se le especifica la versión:
nvm use 16.15.0