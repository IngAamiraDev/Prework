# Instalando Git 🛠 

## ¿Qué es Git? ⚫

Git es el sistema de control de versiones, el cual nos permite llevar un control exacto de todos los cambios a lo largo del tiempo de los proyectos, guarda un copia completa del proyecto y guarda los cambios que se hagan.

## ¿Qué es GitHub? ⚪

GitHub es una plataforma en la cual se puede subir los repositorios de Git a la nube, para así poder tener un respaldo y poder compartirlo con la comunidad, además de poder trabajar en proyectos con distintos colaboradores a la vez.

## Diferencias entre Git y GitHub ☯

- Git es el gestor de versiones que se utiliza con más frecuencia en la industria.
- Git no es necesariamente GitHub, GitHub es una plataforma en donde todos los equipos van subiendo su código, colaboran entre ellos, etc.
- Existen más plataformas para utilizar Git como GitLab, GitHub, Bitbucket.
 
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