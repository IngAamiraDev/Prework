# 🔨 Instalación de Node JS 🔨


## ¿Qué es Node.js? 📎

Node.js es un entorno en tiempo de ejecución multiplataforma para la capa del servidor (en el lado del servidor) basado en JavaScript que es un entorno controlado por eventos diseñado para crear aplicaciones escalables, permitiéndote establecer y gestionar múltiples conexiones al mismo tiempo.


## Instalación de Node.js 🪛
`sudo apt update` -> Servidores de software disponible
`sudo apt upgrade`
`sudo apt install nodejs` -> Instala nodejs
`node -v` -> Para conocer la versión de nodejs


## Para remover nodejs
`sudo apt remove nodejs` -> Para remover nodejs


## Instalar paquetes de actualización
`sudo apt install npm` -> Instalar el manejador de paquetes de Node: npm 📥 
`sudo npm install -g n` -> Se instala el paquete n que permite administrar las versiones de Node
`sudo n latest` -> Para instalar la versión más actualizada disponible, se ejecuta
`sudo n install` + "número_de_versión" -> Para instalar una versión especifica de Node (e.g. `sudo n install 15.2.1`)


## Instalar versión en específico usando el comando nvm 🔎
**Nota:** En caso de que no sirva con n, se puede usar el comando nvm. 
- Se puede realizar operaciones como instalar, desinstalar, cambiar de versión, etc, con Node Version Manager usando el comando nvm.
- `sudo apt install curl` -> Herramienta que permite transferir data desde un servidor
- `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash`
- `reset` -> Reinicia la terminal con: 


## Para instalar la última versión:
- `nvm install --lts`
- `node` -v Se verifica la última versión instalada de nodejs:


## Para instalar una versión específica con nvm:
- `nvm install` + "número_de_versión" -> Para instalar una versión especifica (e.g. `nvm install 16.15.0`)


## Para seleccionar la versión de node ya instalada previamente solo en la sesión actual:
`nvm use` + "número_de_versión" -> Para instalar una versión especifica (e.g. `nvm use 16.15.0`)


## Para mostrar en una lista las versiones instaladas de nodejs:
- `nvm ls`


## Para enumerar las versiones disponibles para la instalación (la lista es larga):
`nvm ls-remote`