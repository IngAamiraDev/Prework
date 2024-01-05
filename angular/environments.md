# Ambientes en Angular
- Se usa para crear y/o configurar diferentes procesos en ambientes de dev, prod o text.
- **Nota:** Se puede ver en v15 anteriores, el cual ya venía por defecto.
- Ruta del directorio `./src/environments`.
- Se debe agregar la configuración en el archivo `angular.json` en la apartado de `configurations`.

```json
"configurations": {
"production": {
    "fileReplacements": [
    {
        "replace": "src/environments/environments.ts",
        "with": "src/environments/environments.prod.ts"
    }
    ],
```