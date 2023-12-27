# Configurar Automática Github Page para Angular

## Prerequisito
- Uso de `resolve` en el archivo `tsconfig.json`

La opción resolve no está directamente disponible en el archivo tsconfig.json de TypeScript. Sin embargo, puedes configurar el compilador TypeScript para que resuelva automáticamente ciertas rutas utilizando la opción baseUrl.

La opción baseUrl establece una ruta base que se utilizará para la resolución de módulos. A partir de TypeScript 2.0, se introdujo esta opción para facilitar la resolución de módulos en proyectos más grandes.

Aquí hay un ejemplo de cómo podrías configurar baseUrl en tu archivo tsconfig.json:

```json
{
  "compilerOptions": {
    "baseUrl": "./src",  // Ruta base desde la raíz del proyecto
    "paths": {
      "@app/*": ["app/*"]  // Opcional: Alias para importar rutas más fácilmente
    }
  },
  // ... otras opciones
}
```

En este ejemplo:

"baseUrl": "./src" establece la carpeta src como la raíz del proyecto.
"paths" es opcional y te permite definir alias para rutas comunes. Por ejemplo, puedes usar @app/ como un alias para la carpeta app.
Luego, puedes utilizar estos alias en tus importaciones TypeScript:

```TypeScript
// Ejemplo de uso de alias
import { SomeComponent } from '@app/components/some-component';
import { SomeService } from '@app/services/some-service';
```

## Configurar Github Pages con Método: main /docs

**1.** Ejecutar `ng build` para generar los archivos de producción.

**2.** Mover la carpeta generada por el Build a la raiz del proyecto y renombrar por "docs".

- **Paso 1:**

![Folder browser](./imgs/browser.png)

- **Paso 2:**

![Move](./imgs/move.png)

- Paso 3: Renombrar carpeta por docs

![Folder Docs](./imgs/docs.png)

**3.** Hacer commit en el remoto con los cambios generados.
- `git add .`
- `git commit -am "Add docs"`
- `git push origin main`

**4.** En el proyecto de [Github](https://github.com/) seguir la ruta: `Settings > Pages`

![Github Pages](./imgs/github-pages.png)

- **Seguir la ruta:**
  - `Build and deployment > Branch`

- Seleccionar las siguientes opciones:
  - **main**
  - **/docs**
  - **Save**

**5.** Instalar unas dependencias de desarrollo en la carpeta del proyecto:
  - Ejecutar `npm i del-cli --save-dev` -> Para eliminar archivos/directorios.
  - Luego, ejecutar `npm i copyfiles --save-dev` -> Para copiar archivos/directorios.

**6.** Modificar el archivo **package.json**, agregar las siguientes líneas en la opción de scripts

```json
  "scripts": {
    "build:href": "ng build --base-href ./",
    "build:github": "npm run delete:docs && npm run build:href && npm run copy:dist",
    "delete:docs": "del docs",
    "copy:dist": "copyfiles dist/gifs-app/* ./docs -f"
  }
```

![Scripts](./imgs/scripts.png)

**7.** Guardar cambios

**8.** Esta sería toda la consiguración ahora, ejecutar el comando `npm run build:github` para correr el proceso automático.

![Run](./imgs/run.png)

![Final](./imgs/final.png)

## Configurar Github Pages con Método: Github Actions

1. En Github Actions crear un nuevo workflow, buscar el `Simple workflow`

2. Configuración del `Simple workflow`

```yml
# Steps represent a sequence of tasks that will be executed as part of the job
steps:
  # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
  - name: Checkout
    uses: actions/checkout@v3
  # Setup nodeJS
  - name: Setup nodejs
    uses: actions/setup-node@v4.0.1
    with:
      node-version: "21"
  # install dependencies
  - name: Install deps
    run: npm i
  # Buil app for production
  - name: Build app bundle
    run: npm run build:prod
  # Route file renaming
  - name: Rename index for routing
    run: mv dist/website-ingaamira-dev/browser/index.html dist/website-ingaamira-dev/browser/404.html
  # Deploy to Github pages
  - name: Deploy to Pages
    uses: crazy-max/ghaction-github-pages@v4.0.0
    with:
      build_dir: dist/website-ingaamira-dev/browser
    env:
      GITHUB_TOKEN: ${{secrets.GITHUB_TOKEN}}
```

3. Configurar el archivo package.json

- En la opción de Scripts, agregar la siguiente línea:

Nota: después de `--base-href` y entre los "//" va el nombre del repositorio `/name-repo/`

```json
"scripts": {
    "build:prod": "ng build --configuration production --base-href /website-ingaamira-dev/",
  },
```

4. Ejecutar el comando para crear el Build
- `npm run build:prod`

5. Hacer el commit en Github

## Configurar Github Pages con Método: Biblioteca "angular-cli-ghpages"

1. Instalar la biblioteca angular-cli-ghpages
`npm install -g angular-cli-ghpages`

2. Construir la aplicación
- `ng build --prod --base-href="https://nombre-de-usuario.github.io/nombre-de-repositorio/"`
  - Asegúrate de reemplazar "nombre-de-usuario" y "nombre-de-repositorio" con tu nombre de usuario de GitHub y el nombre de tu repositorio.
  - E.G: `ng build --configuration=production --base-href="https://IngAamiraDev.github.io/website-ingaamira-dev/"`

3. Desplegar en GitHub Pages
- Ahora, puedes desplegar tu aplicación en GitHub Pages usando angular-cli-ghpages. Ejecuta el siguiente comando: `ngh --dir=dist/nombre-de-tu-proyecto`
  - Reemplaza "nombre-de-tu-proyecto" con el nombre de tu proyecto Angular. Este comando creará una rama llamada `gh-pages` en tu repositorio de GitHub y subirá la carpeta dist a esa rama.
  - E.G: `ngh --dir=dist/website-ingaamira-dev/browser`

4. Configurar la fuente de GitHub Pages
- Ve a la página principal de tu repositorio en GitHub.
- Haz clic en la pestaña "Settings".
- Desplázate hacia abajo hasta la sección "GitHub Pages".
- En la opción "Source", selecciona `gh-pages branch`.

## Recursos Adicionales
- [Deployment](https://angular.io/guide/deployment#deploy-to-github-pages)
- [Angular CLI ghpages](https://www.npmjs.com/package/angular-cli-ghpages)
- [Github Angular CLI ghpages](https://github.com/angular-schule/angular-cli-ghpages)
- [Build&Deploy Angular Apps en GitHub Pages con GitHub Actions](https://medium.com/dottech/build-deploy-angular-apps-en-github-pages-con-github-actions-8213466ef8dc)
- [Github Actions](https://www.youtube.com/watch?v=hnCgPowCu9Y)