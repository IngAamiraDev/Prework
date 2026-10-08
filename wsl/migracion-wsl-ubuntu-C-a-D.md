# Migración de WSL Ubuntu del disco C: al disco D:

## Objetivo

Mover la distribución Ubuntu de WSL 2 desde su ubicación actual en `C:` hacia `D:`, manteniendo la distribución funcional y evitando mover los componentes globales de WSL que Windows administra en `C:`.

La arquitectura final será:

```text
D:\
└── WSL\
    ├── Backup\
    │   └── Ubuntu.tar
    └── Ubuntu\
        └── ext4.vhdx
```

> Importante: esta guía mueve la distribución Linux. No intenta mover `wsl.exe`, el kernel de WSL ni los componentes de Windows.

---

## 1. Comprobar el estado actual

Abrir PowerShell y ejecutar:

```powershell
wsl --status
wsl -l -v
```

Verificar que aparezca `Ubuntu` y que use versión `2`.

También conviene comprobar el espacio disponible:

```powershell
Get-PSDrive C,D
```

---

## 2. Hacer una copia de seguridad adicional

Antes de modificar la distribución, crear una carpeta de respaldo:

```powershell
New-Item -ItemType Directory -Force D:\WSL\Backup
```

Exportar Ubuntu:

```powershell
wsl --shutdown
wsl --export Ubuntu D:\WSL\Backup\Ubuntu.tar
```

Comprobar que el archivo existe:

```powershell
Get-Item D:\WSL\Backup\Ubuntu.tar
```

No continuar hasta comprobar que el `.tar` tiene un tamaño razonable.

---

## 3. Desregistrar la distribución original

Esta operación elimina la instancia registrada de Ubuntu.

```powershell
wsl --shutdown
wsl --unregister Ubuntu
```

Comprobar:

```powershell
wsl -l -v
```

`Ubuntu` ya no debería aparecer.

> ⚠️ No ejecutar `wsl --unregister docker-desktop`. Docker Desktop es una distribución independiente.

---

## 4. Crear la ubicación definitiva en D:

```powershell
New-Item -ItemType Directory -Force D:\WSL\Ubuntu
```

---

## 5. Importar Ubuntu directamente en D:

```powershell
wsl --import Ubuntu D:\WSL\Ubuntu D:\WSL\Backup\Ubuntu.tar --version 2
```

Esto crea el disco virtual de Ubuntu en:

```text
D:\WSL\Ubuntu\ext4.vhdx
```

Comprobar:

```powershell
Get-Item D:\WSL\Ubuntu\ext4.vhdx
```

---

## 6. Configurar el usuario predeterminado

Una distribución importada con `wsl --import` normalmente inicia como `root`.

Entrar:

```powershell
wsl -d Ubuntu
```

Comprobar el usuario:

```bash
whoami
```

Si el usuario existente es `aamira`, configurar `/etc/wsl.conf`:

```bash
nano /etc/wsl.conf
```

Contenido:

```ini
[boot]
systemd=true

[user]
default=aamira
```

Guardar y salir.

Si el usuario no existe, crearlo:

```bash
adduser aamira
usermod -aG sudo aamira
```

---

## 7. Reiniciar WSL

Salir de Ubuntu:

```bash
exit
```

En PowerShell:

```powershell
wsl --shutdown
wsl -d Ubuntu
```

Comprobar:

```bash
whoami
echo $HOME
```

El resultado esperado es:

```text
aamira
/home/aamira
```

---

## 8. Verificar que Ubuntu está realmente en D:

En PowerShell:

```powershell
Get-Item D:\WSL\Ubuntu\ext4.vhdx
```

También:

```powershell
wsl -l -v
```

---

## 9. Mover los proyectos de desarrollo

Para proyectos de Angular, NestJS, Node.js, Python, etc., se recomienda trabajar dentro del filesystem Linux:

```text
/home/aamira/projects
```

Crear la carpeta:

```bash
mkdir -p ~/projects
```

Windows `D:\GitHub` es accesible desde WSL como:

```text
/mnt/d/GitHub
```

Copiar los proyectos:

```bash
cp -a /mnt/d/GitHub/. ~/projects/
```

Para una copia con progreso y mejor control:

```bash
sudo apt update
sudo apt install -y rsync
```

Luego:

```bash
rsync -a --info=progress2 \
  --exclude='node_modules/' \
  --exclude='dist/' \
  --exclude='.angular/cache/' \
  /mnt/d/GitHub/ ~/projects/
```

No borrar `D:\GitHub` todavía.

---

## 10. Reinstalar dependencias Linux

No reutilizar `node_modules` creados desde Windows.

Para cada proyecto Node/Angular/NestJS:

```bash
cd ~/projects/nombre-del-proyecto
rm -rf node_modules
npm install
```

Si existe `package-lock.json`, preferir:

```bash
npm ci
```

---

## 11. Instalar herramientas básicas

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git curl build-essential python3 python3-pip python3-venv
```

---

## 12. Instalar Node.js mediante NVM

Recomendado para proyectos Node.js:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Recargar Bash:

```bash
source ~/.bashrc
```

Instalar la versión LTS:

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

## 13. Configurar Git

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@example.com"
```

Comprobar:

```bash
git config --global --list
```

Si los repositorios están en GitHub, se recomienda configurar SSH en Ubuntu y clonar los repositorios directamente dentro de `~/projects`.

---

## 14. Configurar Docker Desktop

Si ya utilizas Docker Desktop en Windows, no es necesario instalar Docker Engine manualmente dentro de Ubuntu.

En Docker Desktop:

```text
Settings
→ Resources
→ WSL Integration
→ Enable integration with Ubuntu
```

Después, desde Ubuntu:

```bash
docker --version
docker run --rm hello-world
```

---

## 15. VS Code + WSL

Instalar VS Code en Windows y la extensión:

```text
WSL
```

Desde Ubuntu:

```bash
cd ~/projects/nombre-del-proyecto
code .
```

Esto permite que VS Code trabaje directamente dentro del filesystem Linux.

---

## 16. Verificación final

Desde Ubuntu:

```bash
whoami
echo $HOME
pwd
df -h /
```

Esperado:

```text
aamira
/home/aamira
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

---

## 17. Limpieza posterior

Solo después de comprobar que:

- Ubuntu inicia correctamente.
- El usuario funciona.
- Los proyectos están disponibles.
- Git funciona.
- Node funciona.
- Docker funciona si lo necesitas.
- No falta ningún archivo.

Se puede eliminar el respaldo si ya no es necesario:

```powershell
Remove-Item D:\WSL\Backup\Ubuntu.tar
```

No eliminar `D:\GitHub` hasta confirmar que todos los proyectos y cambios locales fueron migrados.

---

## Resultado final recomendado

```text
Windows
D:\
├── GitHub\                 # respaldo/copia Windows, temporal
└── WSL\
    ├── Backup\
    │   └── Ubuntu.tar      # respaldo, opcional
    └── Ubuntu\
        └── ext4.vhdx       # filesystem Linux real

Ubuntu WSL
/home/aamira/
└── projects/
    ├── proyecto-1/
    ├── proyecto-2/
    └── proyecto-3/
```

### Recomendación

Para desarrollo profesional con Angular, NestJS, Node.js, Python y Docker, mantener los repositorios dentro de `/home/aamira/projects` ofrece normalmente una mejor experiencia que trabajar directamente desde `/mnt/d`.

Usar `/mnt/d` principalmente para archivos compartidos con Windows, backups y datasets grandes.
