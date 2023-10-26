# Instalando y Configurando Git en WSL 🛠

## Tabla de Contenido
1. [¿Qué es Git?](#1-qué-es-git)
2. [¿Qué es GitHub?](#2-qué-es-github)
3. [Diferencias entre Git y GitHub](#3-diferencias-entre-git-y-github)
    - 3.1 [Git es el gestor de versiones que se utiliza con más frecuencia en la industria](#31-git-es-el-gestor-de-versiones-que-se-utiliza-con-más-frecuencia-en-la-industria)
    - 3.2 [Git no es necesariamente GitHub](#32-git-no-es-necesariamente-github)
    - 3.3 [Existen más plataformas para utilizar Git](#33-existen-más-plataformas-para-utilizar-git-como-gitlab-github-bitbucket)
4. [Preguntas frecuentes](#4-preguntas-frecuentes)
    - 4.1 [¿Para qué sirve el comando git init?](#41-para-qué-sirve-el-comando-git-init)
    - 4.2 [¿Para qué sirve el comando git status?](#42-para-qué-sirve-el-comando-git-status)
    - 4.3 [¿Para qué sirve el comando git add “nombre-archivo”?](#43-para-qué-sirve-el-comando-git-add-nombre-archivo)
    - 4.4 [¿Para qué sirve el comando git add .?](#44-para-qué-sirve-el-comando-git-add-)
    - 4.5 [¿Para qué sirve el comando git commit -m “mensaje”?](#45-para-qué-sirve-el-comando-git-commit-m-mensaje)
    - 4.6 [¿Para qué nos sirve el comando git config --global user. name “nombre”?](#46-para-qué-nos-sirve-el-comando-git-config-global-user-name-nombre)
    - 4.7 [¿Para qué nos sirve el comando git config --global user.email “correo electronico”?](#47-para-qué-nos-sirve-el-comando-git-config-global-useremail-correo-electronico)
    - 4.8 [¿Qué pasa si no tenemos definido un usuario y correo eléctronico en git y queremos hacer un commit?](#48-qué-pasa-si-no-tenemos-definido-un-usuario-y-correo-eléctronico-en-git-y-queremos-hacer-un-commit)
5. [Instalación de Git](#5-instalación-de-git)
    - 5.1 [Realizar el update cada vez que se instale algo nuevo](#51-realizar-el-update-cada-vez-que-se-instale-algo-nuevo)
    - 5.2 [Para instalar Git](#52-para-instalar-git)
    - 5.3 [Verificar versiones de Git](#53-verificar-versiones-de-git)
6. [Llave SSH](#6-llave-ssh)
    - 6.1 [Pasos para vincular la llave SSH por método ED25519 por WSL](#61-pasos-para-vincular-la-llave-ssh-por-método-ed25519-por-wsl)
    - 6.2 [Pasos para vincular la llave SSH por método RSA por WSL](#62-pasos-para-vincular-la-llave-ssh-por-método-rsa-por-wsl)
7. [Cambiar los proyectos HTTPS por SSH](#7-cambiar-los-proyectos-https-por-ssh)
8. [Enviar de remoto a local](#8-enviar-de-remoto-a-local)
9. [Recursos adicionales](#9-recursos-adicionales)
10. [Curso Profesional Git GitHub by Platzi](#10-curso-profesional-git-github-by-platzi)
11. [Flujos de trabajo](#11-flujos-de-trabajo)
    - 11.1 [GitFlow](#111-gitflow)
12. [Books](#12-books)
    - 12.1 [ProGit](#121-progit)

## 1. ¿Qué es Git? ⚫ <a name="1-qué-es-git"></a>
Git es el sistema de control de versiones, el cual nos permite llevar un control exacto de todos los cambios a lo largo del tiempo de los proyectos, guarda una copia completa del proyecto y guarda los cambios que se hagan.

## 2. ¿Qué es GitHub? ⚪ <a name="2-qué-es-github"></a>
GitHub es una plataforma en la cual se pueden subir los repositorios de Git a la nube, para así poder tener un respaldo y poder compartirlo con la comunidad, además de poder trabajar en proyectos con distintos colaboradores a la vez.

## 3. Diferencias entre Git y GitHub ☯ <a name="3-diferencias-entre-git-y-github"></a>

- 3.1 Git es el gestor de versiones que se utiliza con más frecuencia en la industria.
- 3.2 Git no es necesariamente GitHub; GitHub es una plataforma en donde todos los equipos van subiendo su código, colaboran entre ellos, etc.
- 3.3 Existen más plataformas para utilizar Git, como GitLab, GitHub, Bitbucket.

## 4. Preguntas frecuentes: <a name="4-preguntas-frecuentes"></a>

### 4.1 ¿Para qué sirve el comando `git init`? <a name="41-para-qué-sirve-el-comando-git-init"></a>
- Para inicializar Git y crear un repositorio en Git.

### 4.2 ¿Para qué sirve el comando `git status`? <a name="42-para-qué-sirve-el-comando-git-status"></a>
- Esto nos permite saber qué archivos no están siendo trackeados por Git.

### 4.3 ¿Para qué sirve el comando `git add "nombre-archivo"`? <a name="43-para-qué-sirve-el-comando-git-add-nombre-archivo"></a>
- Para que Git trackee el archivo que escribimos.

### 4.4 ¿Para qué sirve el comando `git add .`? <a name="44-para-qué-sirve-el-comando-git-add-"></a>
- Para agregar todos los archivos a Git que estén dentro del directorio en el que nos encontramos en ese momento.

### 4.5 ¿Para qué sirve el comando `git commit -m "mensaje"`? <a name="45-para-qué-sirve-el-comando-git-commit-m-mensaje"></a>
- Para crear un commit. Esto es lo que nos permite crear dentro de Git una versión de nuestro proyecto. La bandera o flag -m nos permite agregar un mensaje descriptivo para saber qué cambio hicimos en el proyecto.

### 4.6 ¿Para qué nos sirve el comando `git config --global user. name "nombre"`? <a name="46-para-qué-nos-sirve-el-comando-git-config-global-user-name-nombre"></a>
- Nos permite agregar un nombre de usuario a Git.

### 4.7 ¿Para qué nos sirve el comando `git config --global user.email "correo electrónico"`? <a name="47-para-qué-nos-sirve-el-comando-git-config-global-useremail-correo-electronico"></a>
- Nos permite agregar un correo eléctronico a Git.

### 4.8 ¿Qué pasa si no tenemos definido un usuario y correo electrónico en Git y queremos hacer un commit? <a name="48-qué-pasa-si-no-tenemos-definido-un-usuario-y-correo-eléctronico-en-git-y-queremos-hacer-un-commit"></a>
- Git no nos permite realizar el commit hasta que definamos al usuario y su correo electrónico.

## 5. Instalación de Git 🔧 <a name="5-instalación-de-git"></a>

- 5.1 `sudo apt update` -> Realizar el update cada vez que se instale algo nuevo.
- 5.2 `sudo apt-get install git-all` -> Para instalar Git.
- 5.3 `git version` -> Verificar las versiones de Git.

## 6. Llave SSH 🔑 <a name="6-llave-ssh"></a>

Cuando se configura la clave SSH con GitHub, ya no es necesario autenticarse introduciendo el correo y contraseña en la terminal cada vez que se hace un commit.

**Nota:** La ruta de inicio debe ser -> `~/.ssh`.

### 6.1 Pasos para vincular la llave SSH por método ED25519 por WSL 🔐 <a name="61-pasos-para-vincular-la-llave-ssh-por-método-ed25519-por-wsl"></a>

- `ssh-keygen -t ed25519 -C` + "email_de_GitHub"  -> 
- Dar ENTER, luego se le da ENTER de nuevo.
- Pregunta por una palabra clave que se ingresa 2 veces (no olvidar).
- `eval "$(ssh-agent -s)"` -> Validar que el agente SSH está corriendo.
- `ssh-add ∼/.ssh/id_ed25519` -> Agregar la llave al agente SSH.
- **Nota:** Para escribir la virgulilla "~", presionar las teclas Alt Gr + 4 + barra espaciadora.
- `cat ~/.ssh/id_ed25519.pub` -> Imprimir el contenido de la llave pública.
- Copiar la llave SSH.
- Ir a [GitHub](https://github.com/).
- Iniciar sesión.
- Seguir la ruta: `Profile > Settings > SSH and GPG keys > New SSh key`.
- Pegar el contenido de la llave SSH.
- Asignar un título a la llave SSH.
- Hacer clic en Add SSH key.

### 6.2 Pasos para vincular la llave SSH por método RSA por WSL 🔐 <a name="62-pasos-para-vincular-la-llave-ssh-por-método-rsa-por-wsl"></a>

- `ssh-keygen -t rsa -b 4096 -C` + "Your EMAIL".
- **Nota:** Al activar el pw en "Passphrase", esto hará que siempre que se haga pull/push pida la misma contraseña.
- `ssh-keygen -f ~/.ssh/id_rsa -p` -> En caso de activar pw en "Passphrase" y desactivar.
- `eval $(ssh-agent -s)` -> Revisar el servidor de llaves que esté activo.
- `ssh-add ~/.ssh/id_rsa` -> Agregar la llave privada a nuestro sistema o al servidor.

## 7. Cambiar los proyectos HTTPS por SSH <a name="7-cambiar-los-proyectos-https-por-ssh"></a>

- [Configurar Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
- `git remote set-url origin` + "ruta_ssh".
- `git remote -v` -> Validar que registre fetch and push.

## 8. Enviar de remoto a local <a name="8-enviar-de-remoto-a-local"></a>

- `git add remote origin` + "url del repo" -> Agregar el repositorio remoto.
- `git remote -v` -> Para verificar si el repositorio remoto se agregó correctamente.
- `git branch -M main` -> Cambiar el nombre de la rama principal a main en Github.
- `git push origin main` -> Enviar repo local.

## 9. Recursos adicionales <a name="9-recursos-adicionales"></a>

- [Add SSH to GitHub](https://gist.github.com/JARVIS-AI/a20f38c88bee6b0d2fd5938b94bac438).
- [Configurar llaves SSH en Git y GitHub](https://platzi.com/tutoriales/1557-git-github/4067-configurar-llaves-ssh-en-git-y-github/).
- [Versionamiento Semántico](https://semver.org/lang/es/).
- [Video GitFlow](https://drive.google.com/drive/folders/1JJiHAjG720fwGfbWmBK8PID9MqYXSWJE?usp=sharing).
- [Resolución de Problemas Comunes con Git](/git/info/resolucion_problemas_git.md).

## 10. Curso Profesional Git GitHub by Platzi <a name="10-curso-profesional-git-github-by-platzi"></a>

- [1. Curso Profesional Git GitHub Platzi](/git/docs/Curso_Profesional_Git_GitHub.pdf).
- [2. Curso Profesional Git GitHub Platzi](/git/docs/Curso_Profesional_Git_GitHub_2.pdf).

## 11. Flujos de trabajo <a name="11-flujos-de-trabajo"></a>

- 11.1 [GitFlow](/git/docs/GitFlow.pdf).

## 12. Books <a name="12-books"></a>

- 12.1 [ProGit](/git/books/progit.pdf).