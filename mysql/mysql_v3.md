# Comandos Básicos MySQL

## Obtener la Ip de WSL
ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1

## Reiniciar servidor
sudo service mysql restart

## Iniciar la consola
mysql -u root -h -p
mysql -u root -h 172.20.86.213 -p
mysql -u root -p -h 172.20.86.213 -P 3306

## Validar permisos de los usuarios
SELECT user, host FROM mysql.user;

## Bajar la vulnerabilidad de seguridad
SET GLOBAL validate_password.policy = LOW;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root123*';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root123*';
FLUSH PRIVILEGES;

CREATE USER 'root'@'localhost' IDENTIFIED BY 'root123*';
DROP USER 'ingaamira'@'%';

## Crear usuarios con privilegios

CREATE USER 'ingaamira'@'localhost' IDENTIFIED BY 'ingaamira123*';
GRANT ALL ON mysql.* TO 'ingaamira'@'localhost';

ALTER USER 'ingaamira'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ingaamira123*';


CREATE USER 'ingaamira'@'%' IDENTIFIED BY 'ingaamira123*';
GRANT ALL ON mysql.* TO 'ingaamira'@'%';

ALTER USER 'ingaamira'@'%' IDENTIFIED WITH mysql_native_password BY 'ingaamira123*';

FLUSH PRIVILEGES;

## Obtener la IP de WSL
ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1

## Acceder Desde windows
wsl mysql -h 172.20.86.213 -u root -p

## Agrega el Path
[System.Environment]::SetEnvironmentVariable("Path", $Env:Path + ";C:\Users\ANDRES MIRA\AppData\Local\Microsoft\WindowsApps\wsl.exe /usr/bin", [System.EnvironmentVariableTarget]::User)


## Eliminar todos los registros de las tablas de una BD
```sql
SET FOREIGN_KEY_CHECKS = 0;

SELECT CONCAT('TRUNCATE TABLE ', table_name, ';') 
FROM information_schema.tables 
WHERE table_schema = 'artemis_local';

SET FOREIGN_KEY_CHECKS = 1;
```

```sql
SET FOREIGN_KEY_CHECKS = 0;

SELECT CONCAT('DELETE FROM ', table_name, ';') 
FROM information_schema.tables 
WHERE table_schema = 'artemis_local';

SET FOREIGN_KEY_CHECKS = 1;
```

## Solución recomendada: Redirección con socat (funciona siempre)
Esto funciona como un puente, ya que Windows y WSL2 tienen red aislada, esta solución evita todo el lío de IPs:

1. Instala socat en WSL2 (si no lo tienes)
```bash
sudo apt update
sudo apt install socat
```
2. Ejecutar socat en segundo plato
```bash
nohup socat TCP-LISTEN:3307,fork TCP:localhost:3306 >/dev/null 2>&1 &
```
3. Configurar MySQL Workbench (Windows)

### Kill process socat
`pgrep -fl "socat TCP-LISTEN:3307"`
`sudo kill -9 <PID>`

### Script de arranque de socat

✅ Paso 1: Crear script de arranque de socat

`nano ~/start-mysql-bridge.sh`

```bash
#!/bin/bash

# Verifica si socat ya está corriendo en el puerto 3307
if ! pgrep -f "socat TCP-LISTEN:3307" > /dev/null; then
  echo "[socat] Iniciando redirección localhost:3307 -> localhost:3306..."
  nohup socat TCP-LISTEN:3307,fork TCP:localhost:3306 >/dev/null 2>&1 &
else
  echo "[socat] Ya está corriendo."
fi
```

* Hazlo ejecutable
`chmod +x ~/start-mysql-bridge.sh`

✅ Paso 2: Llamarlo desde `.bashrc` ó `.zshrc`

* `nano ~/.bashrc`
* `nano ~/.zshrc`

⬇️ Al final del archivo, pega:
```sh
# Load socat for bridge to MySQL
~/start-mysql-bridge.sh
```

✅ Paso 3: Verificar

Cerrar WSL2 -> `wsl --shutdown`

Se puede ver mensajes cómo:
```bash
[socat] Iniciando redirección localhost:3307 -> localhost:3306...

[socat] Ya está corriendo.
```