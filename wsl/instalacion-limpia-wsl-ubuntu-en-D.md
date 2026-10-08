# Instalación limpia de Ubuntu WSL 2 en el disco D:

## Objetivo

Instalar una Ubuntu completamente limpia en WSL 2, almacenando su filesystem y `ext4.vhdx` en `D:`.

La arquitectura final será:

```text
D:\
└── WSL\
    ├── Downloads\
    │   └── ubuntu-24.04.rootfs.tar.gz
    └── Ubuntu\
        └── ext4.vhdx
```

> Importante: WSL y algunos componentes globales de Windows continúan instalados en `C:`. Lo que se coloca en `D:` es la distribución Ubuntu y su disco virtual.

---

## 1. Comprobar WSL

Abrir PowerShell como administrador:

```powershell
wsl --status
wsl --version
wsl -l -v
```

Si WSL ya está instalado, no es necesario reinstalarlo.

Comprobar espacio:

```powershell
Get-PSDrive C,D
```

---

## 2. Respaldar información de una Ubuntu anterior

Si ya existe una Ubuntu con información importante, NO continuar directamente con la eliminación.

Exportarla primero:

```powershell
wsl --shutdown
New-Item -ItemType Directory -Force D:\WSL\Backup
wsl --export Ubuntu D:\WSL\Backup\Ubuntu.tar
```

Verificar:

```powershell
Get-Item D:\WSL\Backup\Ubuntu.tar
```

Si la Ubuntu anterior no contiene nada que conservar, puede eliminarse en el paso siguiente.

---

## 3. Eliminar la Ubuntu anterior

Listar distribuciones:

```powershell
wsl -l -v
```

Cerrar WSL:

```powershell
wsl --shutdown
```

Eliminar únicamente Ubuntu:

```powershell
wsl --unregister Ubuntu
```

Verificar:

```powershell
wsl -l -v
```

> ⚠️ No eliminar `docker-desktop`.

---

## 4. Crear carpetas en D:

```powershell
New-Item -ItemType Directory -Force D:\WSL\Downloads
New-Item -ItemType Directory -Force D:\WSL\Ubuntu
```

---

## 5. Descargar Ubuntu 24.04 LTS

Descargar el root filesystem oficial de Ubuntu:

```powershell
Invoke-WebRequest `
  -Uri "https://cloud-images.ubuntu.com/wsl/releases/24.04/current/ubuntu-noble-wsl-amd64-24.04lts.rootfs.tar.gz" `
  -OutFile "D:\WSL\Downloads\ubuntu-24.04.rootfs.tar.gz"
```

Verificar:

```powershell
Get-Item D:\WSL\Downloads\ubuntu-24.04.rootfs.tar.gz
```

---

## 6. Importar Ubuntu directamente en D:

```powershell
wsl --import Ubuntu D:\WSL\Ubuntu D:\WSL\Downloads\ubuntu-24.04.rootfs.tar.gz --version 2
```

Este comando hace que el disco virtual de Ubuntu quede en:

```text
D:\WSL\Ubuntu\ext4.vhdx
```

Comprobar:

```powershell
Get-Item D:\WSL\Ubuntu\ext4.vhdx
```

---

## 7. Iniciar Ubuntu

```powershell
wsl -d Ubuntu
```

Inicialmente es normal entrar como `root`.

Comprobar:

```bash
whoami
```

Debe mostrar:

```text
root
```

---

## 8. Actualizar el sistema

Dentro de Ubuntu:

```bash
apt update
apt upgrade -y
```

Instalar herramientas básicas:

```bash
apt install -y sudo git curl wget build-essential python3 python3-pip python3-venv
```

---

## 9. Crear el usuario de desarrollo

Crear el usuario:

```bash
adduser aamira
```

Agregarlo al grupo sudo:

```bash
usermod -aG sudo aamira
```

Verificar:

```bash
id aamira
```

---

## 10. Configurar el usuario predeterminado

Crear/editar:

```bash
nano /etc/wsl.conf
```

Usar:

```ini
[boot]
systemd=true

[user]
default=aamira
```

Guardar y salir.

---

## 11. Reiniciar WSL

Salir:

```bash
exit
```

Desde PowerShell:

```powershell
wsl --shutdown
wsl -d Ubuntu
```

Verificar:

```bash
whoami
echo $HOME
```

Esperado:

```text
aamira
/home/aamira
```

---

## 12. Crear estructura para proyectos

Dentro de Ubuntu:

```bash
mkdir -p ~/projects
```

La ubicación recomendada es:

```text
/home/aamira/projects
```

No es recomendable desarrollar proyectos Node/Angular/NestJS directamente en `/mnt/d` cuando el objetivo es obtener el mejor rendimiento de WSL.

---

## 13. Migrar proyectos existentes de D:\GitHub

Windows:

```text
D:\GitHub
```

Desde Ubuntu:

```text
/mnt/d/GitHub
```

Si necesitas copiar todos los proyectos:

```bash
cp -a /mnt/d/GitHub/. ~/projects/
```

Para una copia con progreso:

```bash
apt install -y rsync
```

Luego:

```bash
rsync -a --info=progress2 \
  --exclude='node_modules/' \
  --exclude='dist/' \
  --exclude='.angular/cache/' \
  /mnt/d/GitHub/ ~/projects/
```

No borrar `D:\GitHub` hasta verificar la migración.

---

## 14. Alternativa recomendada: clonar desde GitHub

Si todos los proyectos están correctamente publicados en GitHub y no tienes cambios locales sin guardar, es preferible hacer un clone limpio:

```bash
cd ~/projects
git clone git@github.com:USUARIO/REPOSITORIO.git
```

Ventajas:

- Checkout Linux limpio.
- No se trasladan `node_modules`.
- Se evitan archivos generados de Windows.
- Se reduce el riesgo de problemas de permisos.
- El repositorio queda preparado para trabajar directamente en WSL.

---

## 15. Instalar Node.js con NVM

Instalar NVM:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Recargar:

```bash
source ~/.bashrc
```

Instalar Node.js LTS:

```bash
nvm install --lts
nvm use --lts
```

Verificar:

```bash
node --version
npm --version
```

---

## 16. Instalar dependencias de los proyectos

Para un proyecto con `package-lock.json`:

```bash
cd ~/projects/nombre-del-proyecto
npm ci
```

Si no existe `package-lock.json`:

```bash
npm install
```

No copiar `node_modules` desde Windows.

---

## 17. Configurar Git

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@example.com"
```

Comprobar:

```bash
git config --global --list
```

Si utilizas GitHub frecuentemente, configurar SSH dentro de Ubuntu y utilizar URLs `git@github.com:...`.

---

## 18. Configurar Docker Desktop

Si Docker Desktop ya está instalado en Windows, no es necesario instalar Docker Engine manualmente dentro de Ubuntu.

En Docker Desktop:

```text
Settings
→ Resources
→ WSL Integration
→ Enable integration with Ubuntu
```

Después, dentro de Ubuntu:

```bash
docker --version
docker run --rm hello-world
```

---

## 19. Configurar VS Code

Instalar VS Code en Windows y la extensión:

```text
WSL
```

Desde Ubuntu:

```bash
cd ~/projects/nombre-del-proyecto
code .
```

VS Code se conectará al filesystem Linux de Ubuntu.

---

## 20. Verificación final

Dentro de Ubuntu:

```bash
whoami
echo $HOME
pwd
df -h /
git --version
node --version
npm --version
docker --version
```

Comprobar proyectos:

```bash
ls -la ~/projects
```

Desde PowerShell:

```powershell
wsl -l -v
Get-Item D:\WSL\Ubuntu\ext4.vhdx
```

Ubuntu debe aparecer como versión `2`.

---

## 21. Limpieza

Después de verificar que todo funciona, se puede conservar o eliminar el instalador:

```powershell
Remove-Item D:\WSL\Downloads\ubuntu-24.04.rootfs.tar.gz
```

Si existe un backup y ya no es necesario:

```powershell
Remove-Item D:\WSL\Backup\Ubuntu.tar
```

No eliminar `D:\GitHub` hasta comprobar que todos los proyectos y cambios locales fueron recuperados.

---

## Resultado final recomendado

```text
D:\
└── WSL\
    ├── Downloads\
    │   └── ubuntu-24.04.rootfs.tar.gz
    └── Ubuntu\
        └── ext4.vhdx

Ubuntu
/home/aamira/
└── projects/
    ├── angular-project/
    ├── nest-project/
    ├── python-project/
    └── ...
```

### Recomendación

Para desarrollo con Angular, NestJS, Node.js, Python, Git y Docker:

- Ubuntu: `D:\WSL\Ubuntu`
- Proyectos: `/home/aamira/projects`
- Archivos compartidos Windows/Linux: `/mnt/d`
- Backups: `D:\WSL\Backup`
- Docker: Docker Desktop + WSL Integration
- Editor: VS Code + extensión WSL

Esta distribución separa correctamente el almacenamiento de la máquina virtual Linux del almacenamiento de Windows y evita depender de `/mnt/d` para el desarrollo diario.
