# Instalación y Configuración de MySQL en WSL

## 1️⃣ Instalación de MySQL en WSL
Ejecuta los siguientes comandos en **WSL**:
```bash
sudo apt update
sudo apt install mysql-server -y
```
Verifica la versión instalada:
```bash
mysql --version
```

## 2️⃣ Iniciar y Habilitar MySQL
Inicia el servicio de MySQL:
```bash
sudo service mysql start
```
Verifica el estado:
```bash
sudo service mysql status
```
Para que MySQL se inicie automáticamente con WSL:
```bash
sudo systemctl enable mysql
```

## 3️⃣ Configurar Acceso a MySQL desde Windows
Abre MySQL desde WSL:
```bash
mysql -u root -p
```
Verifica los usuarios permitidos:
```sql
SELECT host, user FROM mysql.user;
```
Si `root` solo aparece con `localhost`, ejecuta:
```sql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'tu_contraseña';
FLUSH PRIVILEGES;
```

Edita el archivo de configuración:
```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
Busca la línea:
```ini
bind-address = 127.0.0.1
```
Cámbiala por:
```ini
bind-address = 0.0.0.0
```
Guarda (Ctrl + X, luego Y y Enter) y reinicia MySQL:
```bash
sudo service mysql restart
```

## 4️⃣ Configurar Firewall en WSL y Windows
En WSL:
```bash
sudo ufw allow 3306
sudo ufw allow OpenSSH
sudo ufw enable
```
En Windows (PowerShell como Administrador):
```powershell
New-NetFirewallRule -DisplayName "Allow MySQL WSL" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3306
```

## 5️⃣ Configurar MySQL Workbench con SSH
1. **Abrir MySQL Workbench** y crear una nueva conexión.
2. En **"Connection Method"**, seleccionar **"Standard TCP/IP over SSH"**.
3. Configurar los siguientes datos:
   - **SSH Hostname:** `172.20.86.213`
   - **SSH Username:** `tu_usuario_wsl`
   - **SSH Password:** (deja vacío si usas clave SSH)
   - **MySQL Hostname:** `127.0.0.1`
   - **MySQL Port:** `3306`
   - **Username:** `root`
   - **Password:** (tu contraseña de MySQL)
4. **Guardar y probar la conexión.**

## 6️⃣ Solución de Problemas
### **MySQL no inicia en WSL**
```bash
sudo service mysql start
sudo systemctl enable mysql
```

### **Error 1698 (28000): Access denied for user 'root'@'localhost'**
Ejecutar:
```bash
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'tu_contraseña';
FLUSH PRIVILEGES;
```

### **No se puede conectar desde MySQL Workbench**
Verifica si MySQL está escuchando en el puerto correcto:
```bash
sudo netstat -tulnp | grep mysql
```
Si solo aparece `127.0.0.1:3306`, sigue el **paso 3** para cambiar `bind-address`.

### **Error SSH: "Permission denied"**
Revisar el estado de SSH en WSL:
```bash
sudo service ssh status
```
Si no está instalado, ejecuta:
```bash
sudo apt install openssh-server -y
sudo service ssh start
```
Habilita el acceso root en SSH:
```bash
sudo nano /etc/ssh/sshd_config
```
Busca y cambia:
```ini
PermitRootLogin prohibit-password
```
a:
```ini
PermitRootLogin yes
```
Guarda y reinicia SSH:
```bash
sudo service ssh restart
```