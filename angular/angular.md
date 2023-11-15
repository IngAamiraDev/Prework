# Angular
Angular es un framework de desarrollo de aplicaciones web desarrollado y mantenido por Google. Es un framework de código abierto y se utiliza para construir aplicaciones web de una sola página (SPA) y aplicaciones empresariales complejas. Angular proporciona un conjunto de herramientas y bibliotecas que facilitan el desarrollo, la prueba y el mantenimiento de aplicaciones web robustas y escalables.

## Elementos básicos de Angular

## División de responsabilidad
Un componente de Angular se divide en tres archivos: uno para el código TypeScript, otro para el código HTML y uno más para el código CSS.

```sh
// TypeScript

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Hola soy Platzi';
}
```

Angular usa el concepto de decoradores para modificar el comportamiento de las clases. La clase AppComponent implementa el decorador @Component() para indicarle a Angular que esta clase será un componente. Dentro de este decorador, puedes observar el selector del componente (un nombre para el mismo), el template HTML y la hoja de estilos que usará.
Finalmente, dentro de la clase puedes declarar tus propiedades y métodos como en cualquier clase de la programación orientada a objetos. Tenemos una propiedad llamada title que es del tipo string. Podemos mostrar el valor de esta variable en el HTML con una interpolación:

```sh
// HTML

<p>{{ title }}</p>
```

Es importante que tengas en cuenta la visibilidad de los atributos y métodos de una clase. Si estos llegaran a ser private, no podrás usarlo en el HTML Las variables deben ser públicas para poder ser compartidas al template.

```sh
// TypeScript

export class AppComponent {
  // Variable privada, no puede utilizarse en un interpolación
  private title = 'Hola! soy una variable privada';
}
```


## Property Binding 
Es la manera que dispone Angular para controlar y modificar las propiedades de los distintos elementos de HTML. Para esto, simplemente utiliza los corchetes [] para poder modificar dinámicamente ese atributo desde el controlador.

### Utilidades:
- El atributo src de la etiqueta `<img>` para modificar dinámicamente una imagen.
- El atributo href de un `<a>` para modificar un enlace.
- El atributo value de un `<input>` para autocompletar un valor de un formulario.
- El atributo disable de un `<input>` para habilitar/deshabilitar un campo de un formulario.

Si tienes en tu componente:

```sh
// TypeScript

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  empresa = 'Platzi';
  habilitado = true;
}
```

Puedes modificar el value de un campo de un formulario de la siguiente manera:

```sh
// HTML

<input [value]="empresa" [disabled]="habilitado"  />
```

Se imprime el valor de la propiedad empresa como valor de un `<input>` y gracias a la variable habilitado controlas la edición del campo.


## Event Binding
Permite controlar los eventos que suceden en estos elementos. El clic de un botón, detectar cambios en un campo, el envío de un formulario, entre otros eventos. Para esto utiliza los paréntesis () para el bindeo de la propiedad del elemento.

Si tienes en tu componente:

```sh
// TypeScript

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  enviarFormulario() {
    // ...
  }
}
```

Puedes ejecutar el método enviarFormulario() cuando se realiza un clic en un botón de la siguiente manera:

```sh
// HTML

<button (click)="enviarFormulario()" >
```

### String interpolation:

El String Interpolation en Angular es un mecanismo que permite insertar valores de variables o expresiones directamente en las plantillas HTML. Se utiliza con el doble conjunto de llaves {{}} y permite que los valores se muestren dinámicamente en la interfaz de usuario.

Aquí hay un ejemplo sencillo de String Interpolation en Angular:

```sh
// HTML

@Component({
  selector: 'app-ejemplo',
  template: `
    <p>{{ mensaje }}</p>
    <p>{{ 1 + 1 }}</p>
  `,
})
export class EjemploComponent {
  mensaje: string = 'Hola, mundo!';
}
```

En este ejemplo:

`{{ mensaje }}` inserta el valor de la propiedad mensaje del componente en el párrafo.
`{{ 1 + 1 }}` evalúa la expresión `1 + 1` y muestra el resultado en el segundo párrafo.
El String Interpolation se utiliza para representar dinámicamente datos y expresiones en las plantillas de Angular. Los valores pueden provenir de propiedades de componentes, cálculos o funciones, y se actualizan automáticamente cuando cambian los datos subyacentes.

Además del String Interpolation, Angular también ofrece otras formas de enlace de datos, como Property Binding (enlace de propiedades) y Event Binding (enlace de eventos), lo que permite una amplia variedad de interacciones dinámicas en las aplicaciones Angular.


## Two way binding
El two-way binding (enlace bidireccional) en Angular es una característica que combina el enlace de propiedades `([property])` con el enlace de eventos ((event)) en una única notación. Esto permite la actualización bidireccional automática entre la vista (plantilla HTML) y el componente TypeScript.

La sintaxis del two-way binding utiliza `[(ngModel)]` y es comúnmente utilizada con elementos de formulario, como input, textarea, y select. Vamos a ver un ejemplo básico utilizando un input:

```sh
// TypeScript

@Component({
  selector: 'app-ejemplo',
  template: `
    <input [(ngModel)]="nombre" />
    <p>Tu nombre es: {{ nombre }}</p>
  `,
})
export class EjemploComponent {
  nombre: string = '';
}
```
En este ejemplo:

El input está vinculado bidireccionalmente a la propiedad nombre del componente mediante `[(ngModel)]`.
Cuando el usuario escribe en el input, la propiedad nombre se actualiza automáticamente.
La etiqueta `<p>` muestra dinámicamente el valor de la propiedad nombre.
Para usar ngModel, es necesario importar el módulo FormsModule en el módulo de Angular en el que se está utilizando. Por ejemplo:

```sh
// TypeScript

import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    // ... otros módulos
    FormsModule,
  ],
  declarations: [
    // ... componentes, directivas, etc.
  ],
})
export class AppModule {}
```

El two-way binding es una herramienta poderosa para simplificar la gestión de datos en aplicaciones Angular y es particularmente útil en formularios. Sin embargo, es importante utilizarlo con moderación, ya que un uso excesivo puede hacer que el código sea más difícil de entender. En algunos casos, es posible que prefieras utilizar enlaces de propiedades y eventos por separado para mayor claridad.


## Atributo ngModel
El atributo ngModel permite el intercambio de datos de forma bidireccional entre el componente y la vista. Lo que suceda en el componente, se verá reflejado en la vista. Lo que se suceda en la vista, inmediatamente impactará en el componente.

```sh
// HTML

<input [(ngModel)]="name">
```

ngModel usar tanto los corchetes `[]` como los paréntesis `()`. De esta manera, se vuelve bidireccional el intercambio de datos. Si no quieres la bidirección, solo colocamos los corchetes `[ngModel]` para que la comunicación sea unidireccional.Para utilizar ngModel, es necesario hacer uso e importar Angular Forms. Para esto, dirígete al archivo app.module.ts que es el módulo principal de toda aplicación Angular y agrega lo siguiente:

```sh
// TypeScript

import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [ ... ],
  imports: [
    FormsModule
  ],
  providers: [],
  bootstrap: [ ... ]
})
export class AppModule { }
```

De esta manera puedes importar el módulo FormsModule desde @angular/forms y agregarlo a imports para emplear la propiedad `[(ngModel)]`.


## Directivas con Angular
Las directivas en Angular permiten extender el HTML con comportamientos personalizados. Angular incluye directivas integradas y permite la creación de directivas personalizadas.

### *nglf
La directiva `*ngIf` en Angular se utiliza para mostrar u ocultar elementos en función de una condición. Si la condición es verdadera, el elemento asociado a la directiva se muestra; de lo contrario, se oculta.

Ejemplo `*ngIf`:

```sh
// HTM

@Component({
  selector: 'app-ejemplo',
  template: `
    <div *ngIf="mostrarElemento">
      Este elemento se mostrará si mostrarElemento es verdadero.
    </div>

    <div *ngIf="!mostrarElemento">
      Este elemento se mostrará si mostrarElemento es falso.
    </div>
  `,
})
export class EjemploComponent {
  mostrarElemento: boolean = true; // Cambia esto para ver cómo afecta la visualización de los elementos
}
```

En este ejemplo:

- La primera div se mostrará si la propiedad mostrarElemento es verdadera.
- La segunda div se mostrará si mostrarElemento es falsa.

La directiva `*ngIf` puede evaluar cualquier expresión booleana, no solo variables booleanas. Puedes utilizar expresiones más complejas para determinar si se debe mostrar u ocultar un elemento.

Recuerda que cuando el valor de la condición cambia, Angular se encarga automáticamente de mostrar u ocultar el elemento asociado, y el cambio se reflejará en la interfaz de usuario. La directiva `*ngIf` es especialmente útil para gestionar la visibilidad de elementos en función de lógica condicional en tus aplicaciones Angular.


### *ngFor
Al igual que con un If, Angular permite iterar un array de números, de cadenas de caracteres o de objetos usando `*ngFor`. 

Si tienes en tu componente un array de datos:

```sh
// TypeScript

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  myArray: string[] = [
    'Platzi',
    'es',
    'genial!'
  ];
}
```

Puedes mostrar cada elemento iterando el array en un elemento HTML:

```sh
// HTML

<ul>
    <li *ngFor="let str of myArray">
        {{ str }}
    </li>
</ul>
```

El `*ngFor` crea una variable temporal llamada str (o el nombre que más te guste) que contiene cada valor de myArray. Finalmente, utilizando una interpolación, muestras el valor de str.Quedando tu HTML de la siguiente manera:

```sh
// HTML

<ul><li>Platzi</li><li>es</li><li>genial!</li></ul>
```

### Índice de iteración

`ngFor` también cuenta con un índice con el número de iteraciones. Puedes acceder a este número agregando al ngFor index as i de la siguiente manera:

```sh
// HTML

<ul>
    <li *ngFor="let str of myArray; index as i">
        {{ i }}. {{ str }}
    </li>
</ul>
```


Cada iteración contiene una variable i con el índice que le corresponde. Iniciando desde cero, da como resultado:

```sh
// HTML

<ul>
    <li>0. Platzi</li>
    <li>1. es</li>
    <li>2. genial!</li>
</ul>
```


## Características clave de Angular


### Two-Way Data Binding:
Angular ofrece enlace de datos bidireccional, lo que significa que los cambios en el modelo afectan automáticamente a la vista y viceversa.

### Directivas:
Las directivas en Angular permiten extender el HTML con comportamientos personalizados. Angular incluye directivas integradas y permite la creación de directivas personalizadas.

### Inyección de Dependencias:
Angular utiliza un sistema de inyección de dependencias que facilita la gestión de las dependencias y la creación de componentes reutilizables.

### Módulos:
Las aplicaciones Angular están organizadas en módulos, que son bloques funcionales que contienen componentes, servicios y otros recursos relacionados.

### Servicios:
Los servicios en Angular son objetos reutilizables que realizan funciones específicas y se pueden inyectar en componentes y otros servicios.

### Routing:
Angular proporciona un sistema de enrutamiento que permite la navegación entre vistas y la gestión de la aplicación de una sola página.

### HTTP Client:
Facilita la realización de solicitudes HTTP y el manejo de respuestas en aplicaciones web.

### Testing:
Angular está diseñado teniendo en cuenta la prueba desde el principio. Ofrece herramientas y soporte para realizar pruebas unitarias y de integración.

### CLI (Command Line Interface):
Angular CLI es una herramienta de línea de comandos que facilita la creación, la construcción y la gestión de proyectos Angular.

## Instalar y configurar Angular en WSL
Asegurarnos de que todos los paquetes de nuestro sistema estén actualizados.

- `sudo apt update` 
- `sudo apt upgrade`


## Prerequisitos
- NodeJs
    - [Node](/nodejs/nodejs.md)
- NPM
    - [NPM](/nodejs/nodejs.md)


## Extensiones en VSCode
- [Angular Language Service](https://marketplace.visualstudio.com/items?itemName=Angular.ng-template)
- [Angular files](https://marketplace.visualstudio.com/items?itemName=alexiv.vscode-angular2-files)
- [Angular Support](https://marketplace.visualstudio.com/items?itemName=vismalietuva.vscode-angular-support)
- [Angular 2 TypeScript Emmet](https://marketplace.visualstudio.com/items?itemName=jakethashi.vscode-angular2-emmet)
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Bracket Pair Color DLW](https://marketplace.visualstudio.com/items?itemName=BracketPairColorDLW.bracket-pair-color-dlw)
- [Bootstrap 4](https://marketplace.visualstudio.com/items?itemName=thekalinga.bootstrap4-vscode)


## Instalar Angular CLI en Ubuntu
- `node -v` -> Verifica versión de Node
- `npm -v` -> Verifica versión de npm
- `npm i @angular/cli -g` -> Instala el CLI de Angular
- `ng version` -> Verificar instalación


## Recrear la carpeta de node_modules
- `cd <name-project>` -> Nos ubicamos en la carperta del proyecto
- `npm intall` -> Agregar los módulos que se han configurado
- `ng serve -o` -> Iniciar el servidor y abrir el navegador web


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

## Bootstrap en Angular
- `cd <name-project>` -> Nos ubicamos en la carperta del proyecto
- `npm install bootstrap --save` -> Instalar Bootstrap (--save: se guarda en los módulos de node)
- **Nota:** Dependiendo de la versión si es menor a 4.5.3 se requiere "jquery" y "popper"
- `npm install jquery --save` -> Instalar Jquery
- `npm install popper.js --save` -> Instalar Popper

### Configurar el archivo angular.json para Bootstrap
```sh
"styles": [
    "src/styles.css",
    "node_modules/bootstrap/dist/css/bootstrap.min.css"
],
"scripts": [
    "node_modules/jquery/dist/jquery.slim.min.js",
    "node_modules/popper.js/dist/umd/popper.min.js",
    "node_modules/bootstrap/dist/js/bootstrap.min.js"
]
```

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