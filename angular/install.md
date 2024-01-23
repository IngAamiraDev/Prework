# Instalar y configurar Angular en WSL

Asegurarnos de que todos los paquetes de nuestro sistema estén actualizados.

- `sudo apt update & sudo apt upgrade`

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
- `ng serve` -> Iniciar el servidor

## Crear proyectos (v17) anteriores
- `ng new <name-project> --standalone=false --skip-tests`

## Recrear proyecto a la nueva sintaxis (v17)
- `ng g @angular/core:control-flow`