# Instalar Docker en WSL2 (Ubuntu) — Windows 10/11

La forma más estable hoy es instalar:

1. WSL2
2. Docker Desktop
3. Integrarlo con Ubuntu en WSL

---

# 1. Verificar WSL

Abre PowerShell como administrador:

```powershell
wsl --status
```

Si no está instalado:

```powershell
wsl --install
```

Reinicia Windows.

---

# 2. Instalar Ubuntu

Lista distribuciones:

```powershell
wsl --list --online
```

Instalar Ubuntu:

```powershell
wsl --install -d Ubuntu
```

Abrir Ubuntu y crear usuario/password.

---

# 3. Verificar que uses WSL2

```powershell
wsl -l -v
```

Debe salir:

```txt
VERSION
2
```

Si aparece 1:

```powershell
wsl --set-version Ubuntu 2
```

---

# 4. Instalar Docker Desktop

Descárgalo desde:

https://www.docker.com/products/docker-desktop/

Instálalo normalmente.

---

# 5. Activar integración con WSL

En Docker Desktop:

## Settings → Resources → WSL Integration

Activa:

- Enable integration with my default WSL distro
- Ubuntu

Apply & Restart.

---

# 6. Probar Docker desde Ubuntu (WSL)

Abrir Ubuntu:

```bash
docker --version
```

Luego:

```bash
docker run hello-world
```

Debe mostrar:

```txt
Hello from Docker!
```

---

# 7. Evitar usar sudo (recomendado)

En Ubuntu:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Cerrar Ubuntu completamente:

```powershell
wsl --shutdown
```

Abrir Ubuntu otra vez.

Probar:

```bash
docker ps
```

Sin sudo.

---

# 8. Verificar Docker Compose

Docker Compose ya viene integrado:

```bash
docker compose version
```

(NO usar docker-compose viejo).

---

# 9. Estructura recomendada para proyectos

Trabaja dentro de Linux:

```bash
/home/tuusuario/proyectos
```

Evita trabajar en:

```txt
/mnt/c/
```

Porque Docker + Node + Angular + Nest funcionan mucho más rápido dentro del filesystem Linux.

---

# 10. Comandos útiles

## Ver contenedores

```bash
docker ps
```

## Ver imágenes

```bash
docker images
```

## Detener todo

```bash
docker stop $(docker ps -q)
```

## Limpiar Docker

```bash
docker system prune -a
```

---

# 11. Validar virtualización

Si Docker no inicia:

## Task Manager → Performance → CPU

Debe decir:

```txt
Virtualization: Enabled
```

Si no:

Entrar BIOS y activar:

- Intel VT-x
- AMD-V

---

# 12. Recomendado para Angular/Nest

Instala también:

```bash
sudo apt update
sudo apt install build-essential
```

Y Node con NVM:

https://github.com/nvm-sh/nvm

Instalar LTS:

```bash
nvm install --lts
```

---

# Verificación final

En Ubuntu:

```bash
docker run hello-world
node -v
npm -v
docker compose version
```

Si todo responde correctamente, ya tienes un entorno listo para:

- Angular SSR
- NestJS
- FastAPI
- PostgreSQL
- Redis
- MongoDB
- IA local
- Microservicios
- Docker Compose
- Kubernetes local posteriormente (kind/minikube)
