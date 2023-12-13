# Bootstrap Nativo en Angular
- `cd <name-project>` -> Nos ubicamos en la carperta del proyecto
- `npm install bootstrap --save` -> Instalar Bootstrap (--save: se guarda en los módulos de node)
- **Nota:** Dependiendo de la versión si es menor a 4.5.3 se requiere "jquery" y "popper"
- `npm install jquery --save` -> Instalar Jquery
- `npm install popper.js --save` -> Instalar Popper

## Configurar el archivo angular.json para Bootstrap
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