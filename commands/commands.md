# Consideraciones Iniciales:

- Instalar Git bash
- Configurar el entorno
- Configuración del archivo .gitignore (Revisar exepciones de acuerdo al proyecto)
- Inicializar el ambiente local
- Configurar las ramas, se recomienda: master, release, develop.
- La rama master (Producción)
- La rama release (Tester), sobre esta rama no se programa, solo se detecta bugs.
- La rama develop (Desarrollo), se crean ramas por atributos


# Comandos básicos en la terminal:

- `pwd`                                                           -> Nos muestra la ruta de carpetas en la que te encuentras ahora mismo.
- `mkdir`                                                         -> Nos permite crear carpetas (por ejemplo, mkdir Carpeta-Importante).
- `touch`                                                         -> Nos permite crear archivos (por ejemplo, touch archivo.txt).
- `rm`                                                            -> Nos permite borrar un archivo o carpeta
- `cat`                                                           -> Ver el contenido de un archivo (por ejemplo, cat nombre-archivo.txt).
- `ls`                                                            -> Nos permite cambiar ver los archivos de la carpeta donde estamos ahora mismo.
- `ls -a`                                                         -> Mostrar todos los archivos, incluso los ocultos.
- `ls -l`                                                         -> Ver todos los archivos como una lista.
- `ls -la`                                                        -> lista los archivos que contiene una carpeta con sus atributos.
- `cd`                                                            -> Nos permite navegar entre carpetas.
- `cd /`                                                          -> Ir a la ruta principal
- `cd o cd ~`                                                     -> Ir a la ruta de tu usuario
- `cd carpeta/subcarpeta`                                         -> Navegar a una ruta dentro de la carpeta donde estamos ahora mismo.
- `cd .. (cd + dos puntos)`                                       -> Regresar una carpeta hacia atrás.
- `history`                                                       -> Ver los últimos comandos que ejecutamos y un número especial con el que podemos repetir su ejecución.
- `! + número`                                                    -> Ejecutar algún comando con el número que nos muestra el comando history (por ejemplo, !72).
- `clear`                                                         -> Para limpiar la terminal. También podemos usar los atajos de teclado Ctrl + L o Command + L.

**OJO** en Windows el terminal no es case sensitive (Sensible las mayusculas), con Linux,y UNIX si son case sensitive


# Comandos para iniciar tu repositorio con Git

- `git init`                                                      -> Crear el repositorio local
- `git config --global user.name "Usuario"`                       -> Configuración del Usuario
- `git config --global user.email "Correo@correo.com"`            -> Configuración del correo
- `git config --global -e (Salir de la consola :q Enter)`         -> Validar la configuración del usuario y correo
- `git status`                                                    -> Validar el estado actual
- `git conf`                                                      -> Para ver las posibles configuraciones
- `git conf --list`                                               -> Para ver la lista de configuraciones hechas
- `git conf --list --show-origin`                                 -> Para mostrar las configuraciones y sus rutas


# Modificar/Ajustar/Eliminar la configuración

- `git config --global --replace-all user.name + "username"`      -> Aquí va tu nombre modificado
- `git config --global --unset-all user.name + "username"`        -> Elimina el nombre del usuario
- `git config --global --add user.name`                           -> Aquí va tu nombre


# Clonar/Crear/Agregar

- `git clone + "Ruta' 'Nombre"`                                    -> Clonar repo completo
- `git clone -b + "Nombre Rama" + "Ruta.git"`                      -> Clonar solo una rama
- `git branch`                                                     -> Identificar la rama
- `git checkout -b 'Nombre Rama'`                                  -> Crear una nueva rama
- `git checkout -b feature/sum`                                    -> Crear una atributo
- `git checkout develop`                                           -> Ir a la rama
- `git checkout --.`                                               -> Recuperar todo hasta el último commit
- `git checkout + "Men commit"`                                    -> Volver a las versión anterior
- `git add -A`                                                     -> Agrega los últimos cambios
- `git add .`                                                      -> Agrega los últimos cambios
- `git add --all`                                                  -> Agrega los últimos cambios
- `git add "*.txt"`                                                -> Agrega todos los txt de todo el proyecto
- `git add *.txt`                                                  -> Agrega todos los txt del directorio actual
- `git add --all`                                                  -> Agrega todos los archivos
- `git add 'Lista archivos'`                                       -> Agrega los archivos que se listen
- `git add pdfs/*.pdf`                                             -> Agrega todos los archivos pdf que están en la carpeta pdfs
- `git add pdfs/`                                                  -> Agrega todo el contenudo dentro de la carpeta pdfs


# Analizar cambios en los archivos de un proyecto Git

- `git log`                                                        -> Historial de commit
- `git log --oneline`                                              -> Forma reducida de los commit
- `git log --oneline --decorate -- all --graph`                    -> Muestra de manera comprimida toda la historia del repositorio de manera gráfica y embellecida.
- `git log --stat`                                                 -> Muestra la cantidad de bytes añadidos y eliminados en cada uno de los archivos - `modificados.
- `git show filename`                                              -> Permite ver la historia de los cambios en un archivo.
- `git diff`                                                       -> Lista de modificaciones
- `git diff --staged`


# Volver en el tiempo con branches y checkout

- `git checkout`                                                   -> Permite regresar al estado en el cual se realizó un commit o branch especificado.
- `git checkout –`                                                 -> Deshacer cambios en un archivo en estado modified (que ni fue agregado a staging)
- `git checkout --.`                                               -> Recuperar todo hasta el último commit
- `git checkout -- + "Nombre archivo"`                             -> Revertir cambios de un archivo específico
- `git commit -am + "Mensaje"`                                     -> Agregar los cambios + commit
- `git commit --amend -m + "Mensaje"`                              -> Modificar un commit



# Git Reset vs Git Rm / Viajes en el tiempo

- `git log --oneline --decorate -- all --graph`                    -> Mostrar los commit y el id reducido
- `git reset --mixed + "commit Id"`                                -> Regresar en el tiempo a un id específico
- `git reset --hard + "commit Id"`                                 -> Regresar a commit eliminado o perdido
- `git reset --hard + "commit Id"`                                 -> Restaurar todo "Forzado"
- `git reset --soft`                                               -> Vuelve el branch al estado del commit especificado.
- `git reset --hard`                                               -> Borra absolutamente todo.
- `git reset --soft HEAD^`                                         -> Modificar cambios dentro del mismo commit
- `git reset --soft/hard`                                          -> Regresa al commit especificado, eliminando todos los cambios que se hicieron después de ese commit.
- `git reflog`                                                     -> Revisión de commit eliminados o perdidos
- `git fetch`                                                      -> Comaparación entre la nube y tierra
- `git rm --cached`                                                -> Elimina los archivos del área de Staging y del próximo commit, pero los mantiene en nuestro disco duro.
- `git rm --force`                                                 -> Elimina los archivos de Git y del disco duro.
- `git rm --cached + "nombre_del_archivo.txt"`                     -> Para eliminar el archivo del staged(ram)
- `git rm + "nombre_del_archivo.txt"`                              -> Para eliminar del repositorio



# Marge Fast-Forward

- `git branch`                                                     -> Validar las ramas actuales
- `git checkout master`                                            -> Ir a la Rama requerida
- `git diff ramavalidar master`                                    -> Comparar ramas
- `git marge + "rama"`                                             -> Marge ramas ( Fast-Forward )
- `git branch -d + "rama"`                                         -> Eliminar una rama


# Tags (Veriones)

- `git tag`                                                        -> Ver los tag del proyecto
- `git tag + "nombretag"`                                          -> Crear un nuevo tag
- `git tag -d + "nombretag"`                                       -> Eliminar un tag


# Stash

- `git stash list`                                                 -> Lista los Stash actuales
- `git stash`                                                      -> Guarda el proyecto en un repositorio de emergencia con el último commit
- `git stash pop`                                                  -> Regresar los cambios de stash al repositorio y elimina el stash
- `git stash drop`                                                 -> Elimina el stash
- `git stash apply`                                                -> Restaura lo que hay en el Stash
- `git stash apply stash@{1}`                                      -> Restaura un stash en específico
- `git stash drop stash@{1}`                                       -> Elimina un stash en específico
- `git stash list --start`                                         -> Lista con mayor información del Stash
- `git show stash`                                                 -> Otra forma de listar los Stash


# Rebase

- `git checkout rama`
- `git rebase master`                                              -> Crea un área temporal de los commit de la rama
- `git rebase -i HEAD~4`                                           -> Unir varios commt (Lista los útimos 4 commit)



# Comandos para trabajo remoto con GIT

- `git clone + "url_del_servidor_remoto"`                          -> Descargar los archivos y todo el historial de cambios en la carpeta .git.
- `git remote add origin + "link.git"`                             -> Agregar el repositorio al GitHub
- `git remote`                                                     -> Listar
- `git remote -v`                                                  -> 
- `git push`                                                       -> Enviar los cambios al servidor remoto.
- `git push -u origin master`                                      ->
- `git push origin + "feature/IncluirBI"`                          -> Hacer un push a una rama feature
- `git push --tags`                                                ->
- `git pull`                                                       -> Básicamente, git fetch y git merge al mismo tiempo.
- `git fetch`                                                      -> Actualizaciones del servidor remoto y guardarlas en nuestro repositorio local.
- `git merge + "feature/sum"`                                      -> Aplicar los cambios realizados en los atributos a las ramas (Se debe ubicar antes en la rama)
- `git push --all`                                                 -> Cargar el repositorio
- `git origin pull develop`                                        -> halar los cambios colaborativos



# Posibles Warning
- git add -A (se corrige con git config core.autocrlf true)


# Url
[Versionamientos Semántico](https://semver.org/lang/es/)
[Video GitFlow](https://drive.google.com/drive/folders/1JJiHAjG720fwGfbWmBK8PID9MqYXSWJE?usp=sharing)