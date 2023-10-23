# 🐍 Instalación de Python 🐍

## Tabla de Contenido
1. [¿Qué es Python?](#qué-es-python)
2. [Instalación de Python](#instalación-de-python)
3. [Entornos virtuales en WSL](#entornos-virtuales-en-wsl)
4. [Gestión de dependencias con requirements.txt](#gestión-de-dependencias-con-requirementstxt)
5. [Conclusión](#conclusión)

## 1. ¿Qué es Python? <a name="qué-es-python"></a>
Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se utiliza en una amplia variedad de aplicaciones, incluyendo gigantes de la industria como Instagram, Netflix, Spotify, Panda3D, entre otros.

## 2. Instalación de Python <a name="instalación-de-python"></a>
Asegurémonos de que Python esté instalado en tu sistema y configuremos el entorno para trabajar con él.

- `python` / `python3` -> Validar si ya está instalado
- `sudo apt update` -> Comando de actualización
- `sudo apt install software-properties-common` -> Instalar el software de Python en su versión actual
- `sudo add-apt-repository ppa:deadsnakes/ppa` -> Actualizar a los lanzamientos de repositorios más recientes
- `sudo apt update` -> Se actualiza de nuevo ya que se agregó un repositorio
- `sudo apt install python3` -> Instalar Python
- `sudo apt install -y python3-pip` -> Instalación de gestor de paquetes de dependencias
- `pip3 -V` -> Verificar Instalación del gestor
- `apt install -y build-essential libssl-dev libffi-dev python3-dev` -> Dependencias en entorno profesional
- `python3 -V` -> Para verificar la versión que se instaló

## 3. Entornos virtuales en WSL <a name="entornos-virtuales-en-wsl"></a>
- `which python3` -> Verificar donde esta python
- `which pip3` -> Verificar donde esta pip
- `sudo apt install -y python3-venv` -> Para instalar el entorno virtual
- `python3 -m venv env` -> Poner cada proyecto en su propio ambiente, se debe entrar en cada carpeta para crear el ambiente
- `source env/bin/activate` -> Activar el ambiente
- `alias avenv="source env/bin/activate"` -> Crear un alias para activar el ambiente
- `deactivate` -> Salir del ambiente virtual
- `pip3 install` ... -> Instalar las librerías necesarias en el ambiente virtual (e.g. pip3 install matplotlib==3.5.0)
- `pip3 freeze` -> Verificar las instalaciones

## 4. Gestión de dependencias con requirements.txt <a name="gestión-de-dependencias-con-requirementstxt"></a>
- `pip3 freeze > requirements.txt` -> Generar el archivo
- `cat requirements.txt` -> Revisar lo que hay dentro del archivo
- `pip3 install -r requirements.txt` -> Instalar las dependencias necesarias para contribuir más rápido en proyectos

## 5. Conclusión <a name="conclusión"></a>
En este tutorial, has aprendido a instalar Python en Windows Subsystem for Linux (WSL) y a configurar entornos virtuales para tus proyectos. También has visto cómo gestionar las dependencias con requirements.txt, lo que te ayudará a contribuir más rápido en proyectos y mantener un entorno limpio y organizado.

¡Ahora estás listo para comenzar a programar con Python en WSL!