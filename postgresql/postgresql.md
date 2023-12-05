# Instalación de POSTGRESQL en WSL2 y accesos con pagAdmin en Windows

## Instalar PostgreSQL
- Actualiza con los comandos `sudo apt update && sudo apt upgrade`
- Luego de actualizado el sistema, instala postgres con el siguiente comando: `sudo apt install postgresql postgresql-contrib`
- Validar la versión instalada `psql --version`

Si la instalación salió bien, en tu terminal verás esto:

![V PostgreSQL](/postgresql/imgs/v-postgresql.png)


## Comandos básicos
- **`sudo service postgresql start`:** Start BD
- **`sudo service postgresql status`:** Status BD
- **`sudo service postgresql stop`:** Stop BD
- **`sudo -u postgres psql`:** Start terminal
- **`\list`:** List BD
- **`ALTER USER <name-user> WITH PASSWORD '<new-pwd>'`:** Update pwd user master
- **`\quit`:** Quit terminal


## How to Uninstall PostgreSQL From Ubuntu

### Method 1: Using ‘sudo apt remove postgresql’

- **`sudo apt remove postgresql postgresql-contrib`:**
- **`sudo apt autoremove`:**

### Method 2: Using ‘purge remove postgresql’
- **`dpkg -l |grep postgres`:**
- **`sudo apt-get --purge remove postgresql postgresql-14 postgresql-client-common postgresql-common postgresql-contrib`:**
- **`dpkg -l | grep postgres`:**

## Errores / Warnings

### Could not bind IPv4 address ‘127.0.0.1’: Address already in use
Significa que el puerto 5432 (que es el puerto predeterminado de PostgreSQL) ya está en uso y no puede ser utilizado por PostgreSQL. 

Para solucionar este problema deberás cambiar dicho puerto siguiendo estos pasos:
- Validar la version: `psql -V`
- Editar archivo de configuración: `sudo nano /etc/postgresql/<version>/main/postgresql.conf` -> Cambiar `<version>` según el caso.
- (e.g. `sudo nano /etc/postgresql/12/main/postgresql.conf`)
- Busca la línea que dice port=5432
- Cambia el número del puerto por otro disponible
- Guarda los cambios


## Recursos Adicionales
- [PostgreSQL in WSL2](https://platzi.com/tutoriales/1480-postgresql/12864-instalacion-de-postgresql-en-wsl2-y-accesos-con-pagadmin-en-windows/)
- [Pgadmin](https://www.pgadmin.org/download/pgadmin-4-windows/)
- [Uninstall PostgreSQL](https://www.commandprompt.com/education/how-to-uninstall-postgresql-from-ubuntu/)
