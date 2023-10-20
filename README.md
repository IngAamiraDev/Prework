# Configuración de Entorno de Desarrollo en Windows


## 💻 Descargar e instalar un navegador web: Chrome 💻

### Conceptos Básicos 🧮

#### Navegador 🌎
 
El navegador web (en inglés: web browser) es un software que permite al usuario acceder a sitios web y visualizarlos. También conocido como navegador de internet, su nombre más común es simplemente “navegador”. En sus inicios, los navegadores web se utilizaban solamente para localizar y mostrar contenido de internet, pero con su evolución y la de los sitios web, se han convertido en herramientas potentes para realizar todo tipo de actividades que antes estaban solamente restringidas al entorno local de un computador. Además, se encuentran disponibles actualmente para todo tipo de dispositivos, como computadores, teléfonos, tablets e incluso televisores inteligentes.


### ¿Cómo funcionan los navegadores web? 🕹
 
Cuando ingresas una URL o dirección del sitio web (por ejemplo: platzi.com), este programa se encarga de localizar el servidor correspondiente a esa dirección y enviarle una solicitud mediante el Protocolo de Transferencia de Hipertexto (HTTP). El servidor envía la respuesta y el navegador convierte este código en un sitio web entendible para el usuario.
Para presentar el contenido de forma visual, el navegador se vale del lenguaje de marcado de hipertexto (HTML) y el lenguaje de estilo en cascadas (CSS), que dan un estilo visual a la información que se presentará en el navegador mediante etiquetas. Para que el usuario pueda interactuar con el contenido que se presenta en el sitio web, usualmente se utiliza el lenguaje de JavaScript, que se encarga de manejar toda esta interacción en su código y enviarla de vuelta al servidor.

Los navegadores también tienen la capacidad de mostrar otros protocolos y prefijos, como HTTPS, que es HTTP seguro (el estándar utilizado prácticamente en todos los sitios web actualmente), el Protocolo de Transferencia de Archivos (FTP), la gestión del correo electrónico (mailto) y los archivos (file).
 
Además, la mayoría de los navegadores también admiten los complementos externos necesarios para mostrar contenidos activos, como vídeos, audio, archivos PDF y juegos dentro de la página.


## Manejo básico de las DevTools

### Usando DevTools de los navegadores 🪛


#### ¿En qué idioma deberíamos de tener configurado nuestro computador y por qué? 🆗
 
- Deberíamos de tener nuestro computador configurado en inglés ya que la industria del desarrollo web gira en este idioma.

#### ¿En dónde podemos descargar las DevTools de Microsoft Edge? ❓
 
- En la Microsoft Store.

#### ¿Qué es Microsoft Edge DevTools? 🔵
 
- El explorador Microsoft Edge incluye herramientas de desarrollo web integradas, denominadas Microsoft Edge DevTools. DevTools es un conjunto de herramientas de desarrollo web que aparece junto a una página web representada en el explorador. Fuente: aquí 

#### ¿Cómo accedemos a las DevTools de Google Chrome? 🟡
 
- F12
- CTRL + Shift + I
- Clic derecho -> Inspeccionar
 
#### ¿Cómo instalar extensiones en Google Chrome?
 
- Dar click a los 3 puntos alineados en forma vertical (están en la esquina superior derecha del navegador), aparece un menú al lado izquierdo, desplazar hasta abajo y seleccionar a Extensiones.
 
- Se puede buscar las extensiones cuado se da click al recuadro de líneas horizontales (esquina superior izquierda) y dar click en Abrir Chrome Web Store, aparece otra página y en el cuadro del buscador se puede poner por ejemplo Lighthouse (Google Lighthouse es una herramienta automatizada de código abierto para medir la calidad de las páginas web, fuente: aquí), seleccionar entre los resultados el que queremos instalar, luego dar en el botón azul que dice Agregar a Chrome, aparece un cuadro de dialogo y hay que confirmar la instalación, esperar y listo.

#### ¿Con cuales Navegadores deberíamos de quedarnos para desarrollar web? ☯
 
- Google Chrome Dev.
- Firefox Developer Edition. 

#### ¿Cómo hacer un Shortcut? ✂
 
- Presonar teclas Windows + Mayús + S


## Instalar VSCode 🪛
 

### IDE 📓
 
Un IDE (Integrated Development Environment) representa un entorno de desarrollo integrado, un ambiente en donde puedes programar. Este IDE trae consigo herramientas que ayudan al desarrollador, como: debugger (depurador), consola, GIT, inteligencia (la cual te ayuda a corregir la sintaxis cuando estás escribiendo código), etc.
 
Lo que hace ser código al código es la sintaxis y el formato del archivo (.js , .css) etc.
 
Existen diferentes tipos de IDE, como por ejemplo:
 
- Visual Studio Code: “Edición de código redefinida”, es totalmente gratuito, está construido encima de open source, es decir que es de código libre y se ejecuta o corre en cualquier sistema operativo. Es muy versátil y puede servir con muchos lenguajes de programación.
 
- WebStorm: Se venden a sí mismos como “El IDE más inteligente para JavaScript”.
 
- Eclipse: es un IDE para el desarrollo de Java, sin embargo, admite varios lenguajes como C / C ++, PHP, ColdFusion, Python, Scala y la plataforma Android. Fue desarrollado en Java y sigue el modelo de código abierto.
 
- Atom: se venden a sí mismos como “El editor de texto hackeable”, es decir que nos dejan construir herramientas, modificarlo, hacerle variaciones a su código para adaptarse a lo que necesitamos.
 
- Editor de texto: Existen editores de texto / editores de código, las cuales son herramientas más minimalistas donde puedes programar pero con ciertos límites. Como el Bloc de Notas.
 
```sh
<!DOCTYPE html>
<html>
	<head>
		<title>Página ejemplo</title>
	</head>
</html>
``` 

## Extensiones de VSCode 🪄

Extensiones y personalización de Visual Studio Code 💇‍♀

### ¿Cuál es el atajo de teclado para abrir el menú de extensiones en VSC? ⌨
 
- CRTL + Shift + I
 
### ¿Cuál es el atajo de teclado para guardar un archivo en VSC? ⌨
 
- CRTL + S 

### ¿Cómo realizar una búsqueda de palabras en VSC? 🔍
 
- VSC puede usar el mismo comando para buscar, con Ctrl + F te habilita la búsqueda.
 
- Además hay algunos plug-ins para realizar búsquedas más avanzadas.

### ¿Cómo llamamos a nuestro primer archivo HTML? 🔎
 
- index.html 

### ¿Desde dónde deberíamos crear un proyecto web? 📲
 
- Desde nuestro editor de código. 

### ¿Por qué debemos crear un proyecto web desde el editor de código y no desde Windows? ❔❓
 
- Porque si nuestro Windows no está configurado para mostrar las extensiones de los archivos, estos aparecerán con una extensión .txt y deberemos renombrarlos. 

### Extensiones de VSC 🧰

#### Extensión Auto Rename Tag
 
- Esta extensión nos ayuda a renombrar la pareja de una etiqueta cuando estemos cambiando estemos cambiando el nombre de una de las parejas. 

#### Extensión Better Comments
 
- Pinta de distintos colores tus comentarios según su tipo de acuerdo a como hayas empezado tu comentario, los categoriza en alertas, queries, TODO’s, importantes y puedes personalizar estas categorías o sus colores. 

#### Extensión Bracket Pair Colorizer
 
- Ésta les pinta los brakets que abren y cierran funciones, así, pueden darse cuenta si les falta algo por cerrar. 

#### Extensión Code Spell Checker
 
- Es una herramienta que sirve como corrector ortográfico del código fuente. 

#### Extensión Color Highlight

- Esta extensión nos ayudara a detectar los coleres que vayamos implementando en nuestro sitio web. Esto lo hace dibujando un recuadro al código hexadecimal del mismo color que especificamos. Muestra los colores en .css para verlos. 

#### Extensión Color Picker
 
- Genera códigos de color como notaciones de color CSS.

#### Extensión CSS Flexbox Cheatsheet</h5>
 
• Permite ver en una hoja los tipos de flexbox y las posiciones que puede tomar.
 

<h5>Extensión CSS Grid Snippets</h5>
 
• Trae un conjunto de atajos para configurar el Grid:
◦ dg – display grid
◦ dig – display inline-grid
◦ gg – grid gap
◦ gtc – grid-template-columns
◦ gta – grid-template-areas
 

<h5>Extensión CSS Peek</h5>
 
• Para que puedas echar un vistazo a los estilos CSS de cada clase, id o etiqueta HTML.
 

<h5>Extensión ESLint</h5>
 
Sirve para filtrar código TypeScript o JavaScript con el objetivo de escribir un código más óptimo y limpio.
 

<h5>Extensión GitLens</h5>
 
• Les dará todas las herramientas de git para tener un mejor orden y llevar mejor el flujo de desarrollo.
 

<h5>Extensión Highlight Matching Tag</h5>
 
Resalta las etiquetas de apertura y/o cierre. Opcionalmente, también muestra la ruta a la etiqueta en la barra de estado.
 

<h5>Extensión Icon Material Theme</h5>
 
• Nos permite agregar un icono distintivo a los archivos para poder identificarnos.
 

<h5>Extensión Indent-rainbown</h5>
 
• Es para orientarnos en las indentaciones y no confundirnos al indentar u ordenar nuestro código.
 

<h5>Extensión Live Server</h5>
 
• Esta extensión nos ayudara a actualizar automáticamente la página en donde estamos viendo cómo va quedando nuestro sitio web. Esto lo hacemos con el fin de no refrescar la página cada vez que hagamos un cambio en el código de manera manual.
 

<h5>Extensión Material Icon Theme</h5>
 
• Nos permite cambiar el estilo de algunos íconos de acuerdo con el tipo de archivo. Para activarlo, presionamos las tecla Ctrl + Shift + p y al salir el cuadro ingresamos: Material Icon Theme, al seeccionarlo se activa la extensión.
 

<h5>Extensión Node Require</h5>
 
• Nos indica automáticamente qué módulos de nodejs nos hace falta y tener menor errores posibles por no instalar o importar los paquetes necesarios.
 

<h5>Extensión Path Intellisense</h5>
 
• Esta extensión nos ayudara a autocompletar las rutas de los archivos que necesitemos en nuestro sitio web.
 

<h5>Extensión Polacode</h5>
 
Que genera bonitas screenshots de tu código.
 

<h5>Extensión Prettier</h5>
 
• Nos ayuda a identar nuestro código para que sea más legible. Mejora como se visualiza el código y ayuda a que sea más legible.
 

<h5>Extensión Project Dashboard</h5>
 
• Te permite organizar tus proyectos por grupos en un dashboard visualmente simple y personalizable.
 

<h5>Extensión Settings Sync</h5>
 
• Ésta sirve para guardar de forma automática su configuración de VSC en su cuenta de github, de esta forma pueden usar VSC en diferentes computadoras sin tener que preocuparse de tener que actualizar su configuración en cada pc.
 

<h5>Extensión Todo Tree</h5>
 
• Que filtra todos los comentarios que comiencen con TODO o con FIXME y los muestra en una vista de árbol, desde el que puedes acceder fácilmente a visualizar donde están tus pendientes.
 

<h5>Extensión Trailing Spaces</h5>
 
• Con esta extensión se resaltarán todos los espacios de más que se te pueden ir al final de una línea. Aunque también puedes habilitar esta funcionalidad directamente en las configuraciones de VSC.
 

<h5>Extensión Turbo Console Log</h5>
 
• Ésta extensión te permite que seleccionando tu variable y con un solo atajo de teclado, generes un línea de console.log con un mensaje significativo y más entendible a la hora de debuggear o examinar tus variables.
 

<h5>Extensión WSL</h5>
 
• Le permite usar el Subsistema de Windows para Linux (WSL) como su entorno de desarrollo de tiempo completo directamente desde VSC.
 

<h5>Listado de extensiones para PHP</h5>
 
• Laravel Extension Pack
• Laravel Blade Snippets
• Laravel 5 Snippets
• PHP Itellisense
• PHP Formatter
• PHP IntelliSense -> completa los path de los use
• PHP PHP Intelephense -> completa los path de los use
• Vetur -> Para ver las plantillas .VUE
• Beautify Blade
 

<h5>Listado para Agilidad al codificar</h5>
 
• AutoFileName
• FileNameComplete
• Auto Close Tag
• Auto Rename Tag
• seti-icons y vscode-icons
• Duplicate selection or line
• Git Graph
• Material Icon Theme
• Color Highlight
• Bracket Pair Colorizer
• Tailwind CSS IntelliSense
• shell-format
• HTML Snippets
• Salesforce Docum -> SFDoc -> Para documentar tu codigo
• CODESNAP -> Tomar Fotos de tu codigo
• Live Server
 

<h5>Listado Para JS</h5>
 
• indent-rainbow
• Color Highlight -
• Path Intellisense -
• Auto Rename Tag -
• Material Icon Theme -
• Prettier - Code formatter -
• vscode-icons -
• Bracket Pair Colorizer
• Babel
• npm intellinsense
• typeScript import
• Simple React Snippets
 

¿Cómo usar Live Server en proyectos reales de HTML y CSS? 🎥
 

Los pasos son: 📝
 
• Creamos una carpeta para nuestro proyecto.
• Damos clic derecho y abrimos Visual Studio Code.
• En caso no poder hacer el paso anterior, esto se configura durante al instalación, entonces abrimos VSC y arrastramos nuestra carpeta al editor.
• Desde el VSC creamos los archivos index.html ( se nombra de esta forma al primer archivo html del proyecto) y un archivo basic.css.
• Si lo creas desde la carpeta en Windows se va a crear con la extensión de archivo .txt (pues lo estamos creando como un archivo de block de notas, de texto plano).
• De no haber instalado la extensión Live Server, se instala presionando las teclas Ctrl + Shift + x y luego buscarla. Luego instalar y esperar.
• Una vez instalada, buscamos Go Live en la esquina inferior derecha.
• Permitimos el acceso de salir algún cuadro.
• Se abrirá una pestaña en nuestro navegador con nuestro sitio.
• Si hacemos un cambio en el código y guardamos nuestro sitio se va a recargar solo sin necesidad de abrir de nuevo el navegador.


## Fuentes Adicionales
[Markdown](https://platzi.com/tutoriales/1344-storytelling-2018/6430-escribe-historias-geniales-con-markdown/)