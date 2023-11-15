# Instalar y configurar Angular en WSL
Asegurarnos de que todos los paquetes de nuestro sistema estén actualizados.

- `sudo apt update` 
- `sudo apt upgrade`


## Prerequisitos
- NodeJs
    - [Node](/nodejs/nodejs.md)
- NPM
    - [NPM](/nodejs/nodejs.md)


## Instalar CLI Angular en Ubuntu
- `node -v` -> Verifica versión de Node
- `npm -v` -> Verifica versión de npm
- `npm i @angular/cli -g` -> Instala el CLI de Angular
- `ng version` -> Verificar instalación


## Comandos básicos en Angular
- `ng new <name-project>` -> Crear un nuevo proyecto
- `ng new <name-project> --standalone=false` -> Para crear el archivo "app-module.ts"
- `ng new todoapp --skip-tests` -> Para evitar las pruebas unitarias
- **Nota:** Validar los pre-procesadores de CSS: (SCSS, Sass, Less)
- `ng serve` -> Lanzar servidor de desarrollo (Dentro de la carpeta de tu proyecto)
- `ng serve -o` -> Lanzar servidor de desarrollo + abrir navegador
- `ng serve -o --port=` + "num-port (e.g. 3500)" -> Lanzar el servidor en un puerto especifico
**Nota:** Si lanzamos el comando ng version desde la carpeta del proyecto podremos obtener mayor detalle de las tecnologías utilizadas.
- `ng serve --host 0.0.0.0` -> Permitir la conexión desde otras computadoras en la misma red.
- `ng build` -> Compila la aplicación de Angular para producción.
- `ng test` -> Ejecuta las pruebas unitarias de la aplicación de Angular.
- `ng lint` -> Ejecuta el linter de la aplicación de Angular para detectar problemas de estilo y buenas prácticas.
- `ng generate <tipo> <nombre>` -> Genera un componente, servicio u otro tipo de elemento en la aplicación de Angular. (e. g. `ng g c pages/home`)
- `ng add <paquete>` -> Instala un paquete y realiza las configuraciones necesarias para usarlo en la aplicación de Angular.
- `ng update` -> Actualiza los paquetes de la aplicación de Angular a las últimas versiones disponibles.
- `ng update @angular/cli` -> Actualizar la version de angular
- `ng update @angular/core` -> Actualizar la version de angular
- `npm cache clean` -> Limpiar el cache de npm


## Nota sobre CSS, SCSS, Sass, Less
En el contexto de Angular, CSS, SCSS, Sass y Less son diferentes preprocesadores y lenguajes de estilos que puedes utilizar para diseñar y estilizar tus aplicaciones web. Al crear un nuevo proyecto de Angular con el comando `ng new`, puedes elegir el tipo de preprocesador que deseas utilizar para los estilos. 

Aquí hay una breve descripción de cada uno:

1. **CSS (Cascading Style Sheets):**

- **Descripción:** CSS es el lenguaje de estilos estándar utilizado en el desarrollo web. Es un lenguaje simple que define cómo se deben presentar los elementos HTML en una página.
- **Uso en Angular:** Si eliges CSS al crear un nuevo proyecto de Angular, los estilos se escribirán en archivos CSS estándar.

2. **SCSS (Sassy CSS):**

- **Descripción:** SCSS es una extensión de CSS que agrega características como variables, anidación y mixins para hacer el código más modular y fácil de mantener.
- **Uso en Angular:** Si eliges SCSS, los estilos se escribirán en archivos SCSS. Angular automáticamente compilará estos archivos SCSS a CSS durante el proceso de construcción.

3. **Sass:**

- **Descripción:** Sass es otra extensión de CSS, similar a SCSS, pero con una sintaxis diferente. Sass utiliza una sintaxis más concisa y no requiere el uso de llaves ni punto y coma.
- **Uso en Angular:** Al igual que con SCSS, si eliges Sass, los estilos se escribirán en archivos Sass, y Angular los compilará a CSS.

4. **Less:**

- **Descripción:** Less es otro preprocesador de CSS que agrega características como variables, anidación y mixins. Tiene una sintaxis diferente a SCSS y Sass.
- **Uso en Angular:** Si eliges Less, los estilos se escribirán en archivos Less, y Angular los compilará a CSS.

Cuando ejecutas el comando `ng new` para crear un nuevo proyecto de Angular, se te preguntará qué tipo de hojas de estilo deseas utilizar, y puedes seleccionar entre CSS, SCSS, Sass o Less según tus preferencias y necesidades específicas de desarrollo. La elección del preprocesador depende en gran medida de las preferencias del equipo y de las características específicas que ofrezca cada preprocesador.


## Server-Side Rendering (SSR)


## Angular Signals
Es un sistema que rastrea de forma granular cómo y dónde se usa su estado en una aplicación, lo que permite que el marco optimice las actualizaciones de renderizado. [Signals](https://angular.dev/guide/signals#what-are-signals)

### ¿Qué son las signals?
Una signal es un envoltorio alrededor de un valor que notifica a los consumidores interesados ​​cuando ese valor cambia. Las signals pueden contener cualquier valor, desde primitivas simples hasta estructuras de datos complejas. El valor de una signal se lee llamando a su función getter, que permite a Angular rastrear dónde se utiliza la signal. Las signals pueden ser de escritura o de sólo lectura.

## Recursos adicionales
[35 comandos que te ayudarán en tus proyectos](https://codigoencasa.com/los-comandos-de-angular-mas-usados/)