# Comandos básicos en Angular

- `ng new <name-project>` -> Crear un nuevo proyecto
- `ng new <name-project> --standalone=false --skip-tests` -> Para crear el archivo "app-module.ts" y evitar archivos de pruebas
- **Nota:** Validar los pre-procesadores de CSS: (SCSS, Sass, Less)

- `ng generate <tipo> <nombre>` -> Genera un componente, servicio u otro tipo de elemento en la aplicación de Angular. (e. g. `ng g c pages/home`)
- `ng g c <name-components>` -> Generar componentes
- `ng g m <name-module>` -> Generar módulos
- `ng g m <name-module> --routing` -> Generar módulos con rutas
- `ng add <paquete>` -> Instala un paquete y realiza las configuraciones necesarias para usarlo en la aplicación de Angular.

- `ng serve` -> Lanzar servidor de desarrollo (Dentro de la carpeta de tu proyecto)
- `ng serve -o` -> Lanzar servidor de desarrollo + abrir navegador
- `ng serve -o --port=` + "num-port (e.g. 3500)" -> Lanzar el servidor en un puerto especifico
**Nota:** Si lanzamos el comando ng version desde la carpeta del proyecto podremos obtener mayor detalle de las tecnologías utilizadas.
- `ng serve --host 0.0.0.0` -> Permitir la conexión desde otras computadoras en la misma red.

- `ng build` -> Compila la aplicación de Angular para producción.
- `ng test` -> Ejecuta las pruebas unitarias de la aplicación de Angular.
- `ng lint` -> Ejecuta el linter de la aplicación de Angular para detectar problemas de estilo y buenas prácticas.
- `ng update` -> Actualiza los paquetes de la aplicación de Angular a las últimas versiones disponibles.
- `ng update @angular/cli` -> Actualizar la version de angular
- `ng update @angular/core` -> Actualizar la version de angular
- `npm cache clean` -> Limpiar el cache de npm

- `npm i` -> Instalar las dependencias del proyecto
- `npm i --save-dev <name-pkg>` (e.g. `npm i --save-dev json-server`) -> Instalar paquetes en modo desarrollo