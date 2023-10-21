# Intlación de WSL? 🌐

## Preguntas frecuentes

### ¿Qué es Windows Subsystem para Linux (WSL)? 🔎
- Es el desarrollo que ha creado Microsoft para hacer de Windows 11 un entorno amigable para el desarrollo de software. Tiene un kernel (núcleo) de Linux que combina tecnologías de virtualización que permiten ejecutarse rápidamente en windows.

### ¿Para qué nos sirve Windows Subsystem for Linux? ⚙
- Nos permite tener un kernel de Linux en Windows.

### ¿Qué tecnologías implemento Windows para desarrollar WSL? 🖱
- Tecnologías de virtualización.

### ¿Qué es un Power User? 🎎
- Es un usuario que tiene más conocimientos que el promedio de las personas.

### ¿Qué puedo hacer si no puedo instalar WSL en mi computador? 💻
- Instalar Linux en una máquina virtual.

## Configurar Windows 10/11 para soportar la instalación de WSL ⚙

## Prerequisitos:
- Windows + r
- `winver` -> Validar la versión de Windows
- **Nota:** La versión de Windows debe ser 2004 – compilación 19041 o superior.
- `winget update --all` -> Para verificar que Windows tenga todas las actualizaciones
- Validar la aplicación Terminal, en caso contrario Descargar por Store la aplicación de Windows Terminal

## Pasos Instalación Automática
- Buscar PowerShell
- Ejecutar PowerShell como administrador
- `wsl -l -v` -> Para saber la versión de Ubuntu a instalar
- `wsl –install` -> Instalar todos los elementos necesarios de forma automática
- Reiniciar la máquina

## Instalar alguna versión en particular
- Buscar PowerShell
- Ejecutar PowerShell como administrador
`wsl --list –online` -> Para listar en linea de comandos las distribuciones disponibles de Linux
`wsl --install` + "nombre_distribucion" -> Para instalar alguna distribución en especifico
- Reiniciar la máquina

## Corregir algunos errores de instalación 
**Nota 1:** 📝 A veces el computador no soporta este tipo de comandos de instalación, a pesar de contar con una versión de Windows actualizada. Si es así, se deben seguir los siguientes pasos, que corresponde con la forma manual de hacer la instalación de WSL.

**Nota 2:** Se debe ejecutar PowerShell como Administrador:

### Habilitación del Subsistema de Windows para Linux:
`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

### Habilitación de la característica Máquina virtual:
`dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

### Validar en Turn Windows features on or off
- Buscar Turn Windows features on or off
- Activo Virtual Machine Platform
- Activo Windows PowerShell 2.0
- Activo Windows Subsystem for Linx

## Comandos después de instalar WSL correctamente
`sudo apt update`
`sudo apt upgrade`