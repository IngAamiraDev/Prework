# Comandos básicos en Angular

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