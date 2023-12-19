# Comandos y Conceptos de Git

Este repositorio contiene una lista de comandos y conceptos esenciales relacionados con Git, una herramienta de control de versiones ampliamente utilizada. Estos comandos y conceptos son fundamentales para trabajar de manera efectiva con Git y gestionar proyectos de desarrollo de software.

## Contenido:

- [Convenciones de Nombres](#convenciones-de-nombres)
- [Buenas Prácticas](#buenas-prácticas)
- [Consideraciones Iniciales](#consideraciones-iniciales)
- [Comandos Básicos en la Terminal](#comandos-básicos-en-la-terminal)
- [Comandos para Iniciar tu Repositorio con Git](#comandos-para-iniciar-tu-repositorio-con-git)
- [Modificar/Ajustar/Eliminar la Configuración](#modificarajustareliminar-la-configuración)
- [Clonar/Crear/Agregar](#clonarcrearagregar)
- [Analizar Cambios en los Archivos de un Proyecto Git](#analizar-cambios-en-los-archivos-de-un-proyecto-git)
- [Volver en el Tiempo con Branches y Checkout](#volver-en-el-tiempo-con-branches-y-checkout)
- [Git Reset vs Git Rm / Viajes en el Tiempo](#git-reset-vs-git-rm--viajes-en-el-tiempo)
- [Merge Fast-Forward](#merge-fast-forward)
- [Tags (Versiones)](#tags-versiones)
- [Stash](#stash)
- [Rebase](#rebase)
- [Comandos para Trabajo Remoto con Git](#comandos-para-trabajo-remoto-con-git)
- [Posibles Warning](#posibles-warning)
- [Recursos Adicionales](#recursos-adicionales)
- [Curso Profesional Git GitHub by Platzi](#curso-profesional-git-github-by-platzi)


## Convenciones de Nombres

- **Nombres de Ramas:** Las ramas deben nombrarse de manera descriptiva y seguir la convención snake_case. Ejemplo: `feature/nueva_funcionalidad` o `bugfix/arreglo_importante`.

- **Mensajes de Commit:** Los mensajes de commit deben ser concisos y descriptivos. Utiliza un formato de mensaje que comienza con un verbo en tiempo presente. Ejemplo: "Agrega validación de formulario" o "Corrige error de sintaxis en el archivo X".

- **Archivos y Carpetas:** Asigna nombres descriptivos a los archivos y carpetas. Evita caracteres especiales y espacios en los nombres de archivos. Utiliza guiones bajos o guiones para separar palabras. Ejemplo: `mi_archivo_importante.js`.

## Buenas Prácticas

- **Frecuencia de Commits:** Realiza commits regularmente y en porciones lógicas. No acumules cambios en un solo commit. Esto facilita el seguimiento de la historia del proyecto.

- **Pull Requests (Solicitudes de Fusión):** Cuando trabajes en una nueva función o solución a un problema, crea una rama separada y abre un Pull Request para revisión. Esto permite una revisión y colaboración más efectiva.

- **Comentarios en Código:** Incluye comentarios significativos en el código cuando sea necesario para explicar la lógica o la intención detrás de una sección de código.

- **Documentación:** Siempre que sea posible, proporciona documentación clara para el proyecto, incluyendo cómo instalarlo, cómo contribuir y cómo usarlo.

## Consideraciones Iniciales

- **Instalar Git Bash:** Configura Git Bash en tu entorno.
- **Configurar el Entorno:** Ajusta la configuración de Git para tu proyecto.
- **Configuración del Archivo .gitignore:** Especifica exclusiones según las necesidades del proyecto.
- **Inicializar el Ambiente Local:** Crea un repositorio Git local.
- **Configurar las Ramas:** Se recomienda tener las ramas master, release y develop.
- **Rama Master (Producción):** La rama principal del proyecto.
- **Rama Release (Pruebas):** Utilizada solo para detectar bugs.
- **Rama Develop (Desarrollo):** Se crean ramas por atributos.

## Comandos para Iniciar tu Repositorio con Git

- **`git init`:** Crea un repositorio local.
- **`git config --global user.name "Usuario"`:** Configura el nombre de usuario.
- **`git config --global user.email "Correo@correo.com"`:** Configura la dirección de correo electrónico.
- **`git config --global -e`:** Sale de la consola con `:q` y Enter para validar la configuración del usuario y correo.
- **`git status`:** Verifica el estado actual del repositorio.
- **`git config`:** Muestra las posibles configuraciones.
- **`git config --list`:** Lista las configuraciones existentes.
- **`git config --list --show-origin`:** Muestra las configuraciones y sus rutas.

## Modificar/Ajustar/Eliminar la Configuración

- **`git config --global --replace-all user.name "nombre"`:** Modifica el nombre del usuario.
- **`git config --global --unset-all user.name`:** Elimina el nombre del usuario.
- **`git config --global --add user.name`:** Agrega el nombre.

## Clonar/Crear/Agregar

- **`git clone "Ruta" "Nombre"`:** Clona el repositorio completo.
- **`git clone -b "Nombre Rama" "Ruta.git"`:** Clona solo una rama.
- **`git branch`:** Identifica la rama actual.
- **`git checkout -b "Nombre Rama"`:** Crea una nueva rama.
- **`git checkout -b feature/sum`:** Crea un atributo.
- **`git checkout develop`:** Cambia a la rama "develop".
- **`git checkout --.`:** Recupera todo hasta el último commit.
- **`git checkout "Men commit"`:** Vuelve a la versión anterior.
- **`git add -A`, `git add .`, `git add --all`:** Agrega los últimos cambios.
- **`git add "*.txt"`:** Agrega todos los archivos .txt en todo el proyecto.
- **`git add *.txt`:** Agrega todos los archivos .txt en el directorio actual.
- **`git add 'Lista archivos'`:** Agrega los archivos que se listan.
- **`git add pdfs/*.pdf`:** Agrega todos los archivos PDF en la carpeta "pdfs".
- **`git add pdfs/`:** Agrega todo el contenido dentro de la carpeta "pdfs".

## Analizar Cambios en los Archivos de un Proyecto Git

- **`git log`:** Historial de commits.
- **`git log --oneline`:** Forma reducida de los commits.
- **`git log --oneline --decorate --all --graph`:** Muestra toda la historia del repositorio de manera gráfica y embellecida.
- **`git log --stat`:** Muestra la cantidad de bytes añadidos y eliminados en cada archivo modificado.
- **`git show filename`:** Permite ver la historia de los cambios en un archivo.
- **`git diff`:** Muestra las modificaciones realizadas.
- **`git diff --staged`:** Muestra las diferencias entre los archivos en el área de preparación y el último commit.

## Volver en el Tiempo con Branches y Checkout

- **`git checkout`:** Permite regresar al estado en el cual se realizó un commit o branch específico.
- **`git checkout --`:** Deshace cambios en un archivo en estado "modified" (que no fue agregado al área de preparación).
- **`git checkout --.`:** Recupera todo hasta el último commit.
- **`git checkout "Nombre archivo"`:** Revierte cambios en un archivo específico.
- **`git commit -am "Mensaje"`:** Agrega los cambios y realiza un commit.
- **`git commit --amend -m "Mensaje"`:** Modifica un commit.

## Git Reset vs Git Rm / Viajes en el Tiempo

- **`git reset --mixed "commit Id"`:** Regresa en el tiempo a un ID específico.
- **`git reset --hard "commit Id"`:** Regresa a un commit eliminado o perdido.
- **`git reset --hard "commit Id"`:** Restaura todo forzadamente.
- **`git reset --soft`:** Vuelve el branch al estado del commit especificado.
- **`git reset --hard`:** Borra absolutamente todo.
- **`git reset --soft HEAD^`:** Modifica cambios dentro del mismo commit.
- **`git reset --soft/hard`:** Regresa al commit especificado, eliminando todos los cambios realizados después de ese commit.
- **`git reflog`:** Revisa commits eliminados o perdidos.
- **`git fetch`:** Compara la nube y tu repositorio local.
- **`git rm --cached`:** Elimina los archivos del área de preparación y del próximo commit, pero los mantiene en tu disco duro.
- **`git rm --force`:** Elimina los archivos de Git y del disco duro.
- **`git rm --cached "nombre_del_archivo.txt"`:** Elimina el archivo del área de preparación (staging).
- **`git rm "nombre_del_archivo.txt"`:** Elimina el archivo del repositorio.

## Merge Fast-Forward

- **`git branch`:** Valida las ramas actuales.
- **`git checkout master`:** Cambia a la rama requerida.
- **`git diff ramavalidar master`:** Compara ramas.
- **`git merge + "rama"`:** Realiza el merge de ramas (Fast-Forward).
- **`git branch -d "rama"`:** Elimina una rama.

## Git Tags (Versiones)

- **`git tag`:** Ver los tags del proyecto.
- **`git tag "name_tag"`:** Crea un nuevo tag.
- **`git tag -a v1.0 -m 'my version 1.0'`:** Crear una etiqueta con un mensaje.
- **`git push origin v1.0`:** Publicar un tag espesífico en remoto.
- **`git push origin --tags`:** Publica las etiquetas masivas que aún no se han enviado al remoto.
- **`git tag -d "nombretag"`:** Elimina un tag.

## Git Stash

- **`git stash list`:** Lista los stash actuales.
- **`git stash`:** Guarda el proyecto en un repositorio de emergencia con el último commit.
- **`git stash pop`:** Regresa los cambios de stash al repositorio y elimina el stash.
- **`git stash drop`:** Elimina el stash.
- **`git stash apply`:** Restaura lo que hay en el stash.
- **`git stash apply stash@{1}`:** Restaura un stash en específico.
- **`git stash drop stash@{1}`:** Elimina un stash en específico.
- **`git stash list --start`:** Lista con más información del stash.
- **`git show stash`:** Otra forma de listar los stash.

## Git Rebase

- **`git checkout rama`.**
- **`git rebase master`:** Crea un área temporal de los commits de la rama.
- **`git rebase -i HEAD~4`:** Une varios commits (lista los últimos 4 commits).

## Comandos para Trabajo Remoto con Git

- **`git clone "url_del_servidor_remoto"`:** Descarga los archivos y todo el historial de cambios en la carpeta .git.
- **`git remote add origin "link.git"`:** Agrega el repositorio a GitHub.
- **`git remote`:** Lista los repositorios remotos.
- **`git remote -v`:** Lista repositorios remotos con URLs.
- **`git push`:** Envía los cambios al servidor remoto.
- **`git push -u origin master`:** Realiza un push al repositorio remoto.
- **`git push origin "feature/IncluirBI"`:** Hace un push a una rama feature.
- **`git push --tags`:** Realiza push de tags.
- **`git pull`:** Básicamente, git fetch y git merge al mismo tiempo.
- **`git fetch`:** Actualiza desde el servidor remoto y guarda los cambios en el repositorio local.
- **`git merge "feature/sum"`:** Aplica los cambios realizados en los atributos a las ramas (debes ubicarte en la rama primero).
- **`git push --all`:** Carga el repositorio.
- **`git origin pull develop`:** Hala los cambios colaborativos.

## Posibles Warning

- **`git add -A`** (se corrige con **`git config core.autocrlf true`**).


## Recursos Adicionales

- [Etiquetado](https://git-scm.com/book/es/v2/Fundamentos-de-Git-Etiquetado)