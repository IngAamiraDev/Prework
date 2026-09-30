Ejecutar `python3 create_angular_clean_project.py <name-project>`

El script requiere Angular CLI (`ng`) en el PATH. Ejecuta `ng new <name-project>` y luego
genera la estructura de Clean Architecture dentro de `src/` del proyecto creado.

## Estructura generada

```txt
src
├── app                                # app por defecto de `ng new`
│   ├── app.component.ts
│   ├── app.config.ts
│   └── app.routes.ts
├── domain
│   ├── models
│   │   └── index.ts
│   ├── repositories
│   │   └── index.ts
│   └── use-cases
│       └── index.ts
├── infrastructure
│   ├── datasource
│   │   └── index.ts
│   └── repositories
│       └── index.ts
├── presentation
│   ├── features
│   │   └── intelligent-invoice-processing
│   │       ├── components
│   │       │   └── index.ts
│   │       ├── facades
│   │       │   └── index.ts
│   │       ├── pages
│   │       │   └── index.ts
│   │       └── view-models
│   │           └── index.ts
│   └── shared
│       └── components                 # Componentes generados con `ng g component`
│           ├── navbar
│           ├── footer
│           └── layout
├── shared
│   ├── components
│   │   └── index.ts
│   ├── services
│   │   └── index.ts
│   └── utils
│       └── index.ts
├── index.html
├── main.ts
└── styles.css
```

Cada carpeta creada lleva un `index.ts` con el comentario `// Barrel export file` (barrel export),
generado solo si el archivo no existe previamente.

## Lo que también modifica el script

- **`tsconfig.json`**: agrega alias de ruta en `compilerOptions`, solo si `"paths"` no existe ya.
  Si ya está configurado, avisa y no lo toca (no actualiza los alias a los nuevos valores).

  ```json
  "paths": {
    "@domain/*": ["src/domain/*"],
    "@infrastructure/*": ["src/infrastructure/*"],
    "@presentation/*": ["src/presentation/*"]
  }
  ```

  Nota: no hay alias para `shared/`, que no queda cubierta.

- **`angular.json`**: reemplaza la configuración de assets del proyecto por
  `src/favicon.ico`, `src/assets`, `src/robots.txt` y `src/sitemap.xml`.
  Verifica que esos archivos existan después de `ng new`, según la versión de Angular CLI.
