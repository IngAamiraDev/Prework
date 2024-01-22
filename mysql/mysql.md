# How to install MySQL on WSL2 (Ubuntu)

## Install
- Update Package -> `sudo apt update && sudo apt upgrade`
- Install MySQL server -> `sudo apt install mysql-server`
- Confirm installation -> `mysql --version`

## Secure the MySQL server
- Start MySQL Service -> `sudo service mysql start`
- First start the MySQL server -> `sudo /etc/init.d/mysql start`
- Then run the security script (Secure MySQL Installation) -> `sudo mysql_secure_installation`
- (Optional) Install MySQL Client -> `sudo apt install mysql-client`
- Status MySQL Service -> `systemctl status mysql.service`

## Connect to MySQL
- Access MySQL -> `mysql -u root -p`
- Start the MySQL shell by running the following -> `sudo mysql`
- mysql>  `SELECT user,authentication_string,plugin,host FROM mysql.user;`

## Change the authentication method for root
- sudo mysql
- mysql> `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'strongpassword123';`
- Reloading the grant tables mysql> `FLUSH PRIVILEGES;`
- Recheck authentication method for MySQL Users mysql> `SELECT user,authentication_string,plugin,host FROM mysql.user;`

## Creating a New User
- $ `sudo mysql` -> Start Mysql
- mysql> `CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';` -> Making a new user within the MySQL shell
- mysql> `GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';` -> Making a new Previleges
- mysql> `FLUSH PRIVILEGES;` -> Reload all the privileges
- $ `mysql -u username -p` -> Connecting

# Others Resources
- [How to install MySQL on WSL 2 (Ubuntu)](https://pen-y-fan.github.io/2021/08/08/How-to-install-MySQL-on-WSL-2-Ubuntu/)
- [Visual C++ Redistributable 2019](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- [Download DB ](https://dev.mysql.com/downloads/windows/installer/8.0.html)
- [Installing MySQL in Ubuntu (WSL2)](https://harshityadav95.medium.com/installing-mysql-in-ubuntu-linux-windows-subsystem-for-linux-from-scratch-d5771a4a2496)