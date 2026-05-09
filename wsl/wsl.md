# Instalación y Configuración de WSL en Windows 🌐

**Tabla de Contenido**

1. [Introducción](#1-introducción)
2. [Preguntas Frecuentes](#2-preguntas-frecuentes)
   - [¿Qué es Windows Subsystem para Linux (WSL)? 🔎](#¿qué-es-windows-subsystem-para-linux-wsl-)
   - [¿Para qué nos sirve Windows Subsystem for Linux? ⚙](#¿para-qué-nos-sirve-windows-subsystem-for-linux-)
   - [¿Qué tecnologías implementa Windows para desarrollar WSL? 🖱](#¿qué-tecnologías-implementa-windows-para-desarrollar-wsl-)
   - [¿Qué es un Power User? 🎎](#¿qué-es-un-power-user-)
   - [¿Qué puedo hacer si no puedo instalar WSL en mi computador? 💻](#¿qué-puedo-hacer-si-no-puedo-instalar-wsl-en-mi-computador-)
3. [Configuración de Windows para Soportar la Instalación de WSL](#3-configuración-de-windows-para-soportar-la-instalación-de-wsl-)
   - [Requisitos Previos](#requisitos-previos)
   - [Pasos para la Instalación Automática](#pasos-para-la-instalación-automática)
   - [Instalación de una Distribución Específica](#instalación-de-una-distribución-específica)
   - [Opción Adicional para la Instalación de WSL](#opción-adicional-para-la-instalación-de-wsl)
4. [Uso Básico](#4-uso-básico)
5. [Interconexión entre WSL y Windows](#5-interconexión-entre-wsl-y-windows)
6. [Uso Avanzado (opcional)](#6-uso-avanzado-opcional)
7. [Solución de Problemas Comunes](#7-solución-de-problemas-comunes)
8. [Corrección de Errores de Instalación](#8-corrección-de-errores-de-instalación)
9. [Comandos Después de Instalar WSL Correctamente](#9-comandos-después-de-instalar-wsl-correctamente)
10. [Recursos Adicionales](#10-recursos-adicionales)
11. [Conclusión](#11-conclusión)

## 1. Introducción

Windows Subsystem for Linux (WSL) es una característica de Windows que permite a los desarrolladores ejecutar un sistema operativo Linux en paralelo con Windows. Esto es útil para ejecutar herramientas de desarrollo basadas en Linux en un entorno de Windows. Asegúrate de que tu sistema cumple con los requisitos previos antes de continuar.

## 2. Preguntas Frecuentes

### ¿Qué es Windows Subsystem para Linux (WSL)? 🔎

Es el desarrollo que ha creado Microsoft para hacer de Windows 11 un entorno amigable para el desarrollo de software. Tiene un kernel (núcleo) de Linux que combina tecnologías de virtualización que permiten ejecutarse rápidamente en Windows.

### ¿Para qué nos sirve Windows Subsystem for Linux? ⚙

Nos permite tener un kernel de Linux en Windows.

### ¿Qué tecnologías implementa Windows para desarrollar WSL? 🖱

Tecnologías de virtualización.

### ¿Qué es un Power User? 🎎

Es un usuario que tiene más conocimientos que el promedio de las personas.

### ¿Qué puedo hacer si no puedo instalar WSL en mi computador? 💻

Puedes instalar Linux en una máquina virtual.

## 3. Configuración de Windows para Soportar la Instalación de WSL ⚙

### Requisitos Previos

Asegúrate de que tu sistema cumple con estos requisitos antes de continuar:

- Windows + r
- `winver`: Valida la versión de Windows
- **Nota:** La versión de Windows debe ser 2004 – compilación 19041 o superior.
- `winget update --all`: Para verificar que Windows tenga todas las actualizaciones.
- Validar la aplicación Terminal; en caso contrario, descarga la aplicación de Windows Terminal desde la Microsoft Store.

### Pasos para la Instalación Automática

Abre PowerShell como administrador y sigue estos pasos:

1. Ejecuta `wsl -l -v` para saber la versión de Ubuntu a instalar.
2. Ejecuta `wsl --install` para instalar automáticamente todos los elementos necesarios. (Si no se instala, se debe actualizar la versión `wsl --update`)
3. Si la opción anterior no funciona, prueba con `wsl.exe --install Ubuntu`.
4. Reinicia la máquina.

### Instalación de una Distribución Específica

Si deseas instalar una distribución de Linux en particular, sigue estos pasos:

1. Busca PowerShell y ejecútalo como administrador.
2. Ejecuta `wsl --list --online` para listar las distribuciones disponibles en línea.
3. Ejecuta `wsl --install` seguido del nombre de la distribución que desees instalar.
4. Reinicia la máquina.

### Opción Adicional para la Instalación de WSL

Para habilitar WSL en Windows manualmente, sigue estos pasos:

1. Abre PowerShell como administrador.
2. Ejecuta `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` para habilitar WSL.
3. Una vez que el proceso se complete, reinicia tu computadora.

## 4. Uso Básico

Ahora que has instalado una distribución de Linux, puedes ejecutar comandos y realizar tareas básicas en ella. Algunos comandos esenciales incluyen:

- `ls`: Listar archivos y directorios.
- `cd`: Cambiar de directorio.
- `sudo`: Ejecutar comandos con privilegios de administrador.

## 5. Interconexión entre WSL y Windows

WSL y Windows pueden compartir archivos y ejecutar aplicaciones. Los archivos de Windows se encuentran en `/mnt/c/`, donde `/c/` representa la unidad de disco C. Puedes abrir archivos de Windows con aplicaciones de Linux y viceversa.

Por ejemplo, para abrir un archivo de Windows con el editor de texto `nano`, ejecuta: `nano /mnt/c/ruta/al/archivo.txt`

## 6. Uso Avanzado (opcional)

Si deseas personalizar aún más tu entorno de WSL, puedes investigar cómo instalar software específico o configurar entornos de desarrollo. Esto puede incluir la instalación de servidores web, bases de datos o herramientas de desarrollo.

## 7. Solución de Problemas Comunes

Si te encuentras con problemas, consulta la documentación oficial de WSL y la comunidad en línea para solucionarlos. Los problemas comunes pueden incluir problemas de red, acceso a archivos o problemas de inicio.

## 8. Corrección de Errores de Instalación

**Nota 1:** 📝 A veces, el computador no soporta este tipo de comandos de instalación, a pesar de contar con una versión de Windows actualizada. Si es así, sigue estos pasos para realizar la instalación manual de WSL.

**Nota 2:** Debes ejecutar PowerShell como Administrador.

### Habilitación del Subsistema de Windows para Linux:

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

### Habilitación de la característica Máquina virtual:

```bash
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

### Validación en "Turn Windows features on or off"

Asegúrate de que las siguientes opciones estén activadas:

- Virtual Machine Platform
- Windows PowerShell 2.0
- Windows Subsystem for Linux

## 9. Otros comandos usados:

### Cerrar WSL completamente
```bash
wsl --shutdown
```

### Ver distribuciones dañadas
```bash
wsl -l -v
```

### Eliminar distribuciones
```bash
wsl --unregister Ubuntu
```

### Reiniciar servicios WSL
```bash
net stop LxssManager
net start LxssManager
```

### Actualizar WSL
```bash
wsl --update
```

### Vaer estado de las distribuciones
```bash
wsl --status
```


## 9. Comandos Después de Instalar WSL Correctamente

Una vez que hayas instalado WSL, ejecuta los siguientes comandos para mantener tu sistema actualizado:

- `sudo apt update && sudo apt upgrade`

## 10. Recursos Adicionales

- [Documentación oficial de WSL](https://docs.microsoft.com/en-us/windows/wsl/)
- [Comunidad de WSL en Reddit](https://www.reddit.com/r/bashonubuntuonwindows/)


## 11. Conclusión
Has configurado con éxito WSL en Windows, lo que te permitirá ejecutar aplicaciones y herramientas de desarrollo basadas en Linux en tu sistema Windows. ¡Ahora estás listo para comenzar a aprovechar al máximo esta poderosa herramienta!

Recuerda que WSL es una característica en constante evolución, por lo que siempre es bueno mantenerse actualizado con las últimas mejoras y características.