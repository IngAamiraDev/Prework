# Commands in WSL

## Comandos Básicos en la Terminal

- **`cd /:`:** Directorio raíz.
- **`cd ...`:** Nivel de directorio.
- **`cd --`:** Directorio anterior.
- **`pwd`:** Muestra la ruta actual de carpetas.
- **`mkdir`:** Permite crear carpetas (e.g. `mkdir <name-folder or path>`).
- **`rmdir`:** (“remove directory”): elimina un directorio vacío.
- **`rm -r`:** (“remove recursuvely”): elimina un directorio junto con su contenido.
- **`touch`:** Crea archivos (por ejemplo, `touch archivo.txt`).
- **`rm`:** Borra un archivo o carpeta.
- **`cat`:** Muestra el contenido de un archivo (e.g. `cat nombre-archivo.txt`).
- **`ls`:** Lista los archivos en la carpeta actual.
- **`ls -a`:** Lista todos los archivos, incluso los ocultos.
- **`ls -l`:** Muestra la lista de archivos con detalles.
- **`ls -la`:** Lista los archivos con detalles, incluyendo los ocultos.
- **`cd`:** Navega entre carpetas.
- **`cd /`:** Navega a la ruta principal.
- **`cd` o `cd ~`:** Navega a la ruta de tu usuario.
- **`cd carpeta/subcarpeta`:** Navega a una subcarpeta desde la carpeta actual.
- **`cd ..`:** Retrocede una carpeta.
- **`history`:** Visualiza los comandos previamente ejecutados.
- **`! + número`:** Ejecuta un comando usando su número de historial (e.g. `!72`).
- **`clear`:** Limpia la terminal.
- **`sudo adduser <new-user>`:** -> Agregar un nuevo usuario.
- **`sudo apt update && sudo apt upgrade`:** -> Actualizar el sistema.

## Advanced commands
- **`grep sudo /etc/group| cut -d: -f4`:** Find Users Included to Sudo
- **`sudo usermod -a -G sudo <username>`:** -> To Add a User to Sudo in WSL
- **`sudo gpasswd -d <username> sudo`:** To Remove a User from Sudo in WSL

**Nota:** En Windows, el terminal no distingue entre mayúsculas y minúsculas, pero en Linux y UNIX sí.

## Configurar un nuevo usuario como el predeterminado en WSL
Para esto tendrás que abrir Powershell o Cmd.exe como administrador y escribir lo siguiente:
- `ubuntu config --default-user <name-user>`

## Recursos Adicionales
- [Basic Commands](https://platzi.com/tutoriales/2042-prework-windows/11390-comandos-basicos-y-atajos-para-la-terminal-que-todo-principiante-debe-conocer/)
- [Users WSL](https://winaero.com/add-remove-sudo-users-wsl-linux-windows-10/)
