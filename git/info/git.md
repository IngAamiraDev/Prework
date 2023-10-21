# Instalando Git 🛠 


## ¿Qué es Git? ⚫

Git es el sistema de control de versiones, el cual nos permite llevar un control exacto de todos los cambios a lo largo del tiempo de los proyectos, guarda un copia completa del proyecto y guarda los cambios que se hagan.


## ¿Qué es GitHub? ⚪

GitHub es una plataforma en la cual se puede subir los repositorios de Git a la nube, para así poder tener un respaldo y poder compartirlo con la comunidad, además de poder trabajar en proyectos con distintos colaboradores a la vez.


## Diferencias entre Git y GitHub ☯

- Git es el gestor de versiones que se utiliza con más frecuencia en la industria.
- Git no es necesariamente GitHub, GitHub es una plataforma en donde todos los equipos van subiendo su código, colaboran entre ellos, etc.
- Existen más plataformas para utilizar Git como GitLab, GitHub, Bitbucket.


## Preguntas frecuentes:

### ¿Para qué sirve el comando git init?
- Para inicializar git y crear un repositorio en git.

### ¿Para qué sirve el comando git status?
- Esto nos permite saber que archivos no están siendo trackeados por Git.

### ¿Para qué sirve el comando git add “nombre-archivo”?
- Para que git trackee el archivo que escribimos.

### ¿Para qué sirve el comando git add .?
- Para agregar todos los archivos a git que esté dentro del directorio en el que nos encontramos en ese momento.

### ¿Para qué sirve el comando git commit -m “mensaje”?
- Para crear un commit. Esto es lo que nos permite crear dentro de git una versión de nuestro proyecto. la bandera o flag -m nos permite agregar un mensaje descriptivo para saber qué cambio hicimos en el proyecto.

### ¿Para qué nos sirve el comando git config --global user. name “nombre”?
- Nos permite agregar un nombre de usuario a Git.

### ¿Para qué nos sirve el comando git config --global user.email “correo electronico”?
- Nos permite agregar un correo eléctronico a Git.

### ¿Qué pasa si no tenemos definido un usuario y correo eléctronico en git y queremos hacer un commit?
- Git no nos permite realizar el commit hasta que definamos al usuario y su correo eléctronico.


## Instalación de Git 🔧

`sudo apt update` -> Realizar el update cada vez que se instale algo nuevo:
`sudo apt-get install git-all` -> Para instalar Git
`git version` -> Verificar versiones de Git


## Llave SSH 🔑

Cuando se configura la clave SSH con GitHub, ya no es necesario autenticarse introduciendo el correo y contraseña en la terminal cada vez que se hace un commit.

### Pasos para vincular la llave SSH 🔐
- `ssh-keygen -t ed25519 -C` + "email_de_GitHub"  -> 
- Dar ENTER, luego se le da ENTER de nuevo
- Pregunta por una palabra clave que se ingresa 2 veces (no olvidar).
- `eval "$(ssh-agent -s)"` -> Validar que el agente SSH está corriendo
- `ssh-add ∼/.ssh/id_ed25519` -> Agregar la llave al agente SSH:
- **Nota:** Para escribir la virgulilla "~" presionar las teclas Alt Gr + 4 + barra espaciadora.
- `cat ~/.ssh/id_ed25519.pub` -> imprimir el contenido de la llave pública
- Copiar la llave ssh
- Ir a [GitHub](https://github.com/)
- Iniciar sesión
- Seguir la ruta: `Profile > Settings > SSH and GPG keys > New SSh key`
- Pegar el contenido de la llave ssh
- Asignar un título a la llave ssh
- Click en Add SSH key


## Cambiar los proyectos HTTPS por SSH
- [Congigurar Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- `git remote set-url origin` + "ruta_ssh"
- `git remote -v` -> Validar que registre fetch y push para git@github.com:username/namerepo.git


## Enviar de remoto a local
- `git add remote origin` + "url del repo" -> Agregar el repositorio remoto
- `git remote -v` -> Para verificar si el repositorio remoto se agregó correctamente
- `git branch -M main` -> Cambiar el nombre de la rama principal a main en Github
- `git push origin main` -> Enviar repo local