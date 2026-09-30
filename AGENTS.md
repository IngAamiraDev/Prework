# AGENTS.md

Instrucciones permanentes para agentes que trabajan en este repositorio.

Para el **estado actual** del proyecto (qué se está haciendo, decisiones pendientes, próximo paso) ver `MEMORY.md`. No mezcles ambos archivos: aquí van las reglas, en `MEMORY.md` va la memoria de trabajo.

> Regla base: el código y la configuración reales mandan sobre la documentación. Si un `.md` contradice a un script, gana el script. Verifica antes de afirmar.

---

## 1. Qué es este repositorio

**No es una aplicación.** Es el cuaderno de apuntes y scripts del autor: tutoriales en español sobre el entorno de desarrollo en Windows + WSL (WSL, Git, VSCode, Python, Node.js, Docker, PostgreSQL, MySQL, LocalStack, AWS), más **scripts utilitarios sueltos** de trabajo real con AWS (DynamoDB/S3), scaffolding de Clean Architecture para Angular, y un script de limpieza del sistema.

**El pedido más común no es "arregla el código" sino "dame el script de git para tal cosa", "actualiza esto en python/node", "anota cómo se ejecuta X".** Es un repositorio de consulta: el valor está en que el comando correcto quede escrito y sea copiable. Prioriza la sección 2 para esos casos.

Topología real:

| Ruta | Naturaleza |
|---|---|
| `wsl/ git/ vscode/ python/ nodejs/ postgresql/ mysql/ docker/` | Tutoriales `.md`. Contenido principal del repo. |
| `aws/ local-stack/` | Scripts y runbooks de AWS/LocalStack. |
| `architecture/ python/scripts/` | Generadores de estructura Clean Architecture. |
| `angular/ nestjs/` | Notas de referencia de frameworks. |
| `ia/` | Notas del propio autor sobre uso de IA (incluye este `AGENTS.md`). |
| `git/books/ git/docs/ nestjs/docs/` | PDFs binarios. No editar ni leer como texto. |

---

## 2. Cómo guardar un tema o un script nuevo (el caso habitual)

Cuando el usuario pida un script, un comando o una nota:

1. **Busca antes de escribir.** Es probable que el tema ya esté apuntado: `git/info/commands.md`, `wsl/commands.md`, `angular/*.md`, `docker/docker.md`, `postgresql/postgresql.md`. No dupliques; amplía el archivo existente.
2. **Ubicación:** dentro de la carpeta del tema (`git/`, `python/`, `nodejs/`, `postgresql/`…). No hace falta crear carpeta nueva para un tema suelto: `angular/api-date-holidays.md` es la prueba.
3. **Nombre:** copia el estilo del archivo hermano más cercano. Hay kebab-case (`api-date-holidays.md`) y snake_case (`resolucion_problemas_git.md`). Chuletas de consola → `commands.md`.
4. **`mysql/mysql_v1.md|v2|v3.md` son revisiones sucesivas del mismo documento**, no documentos paralelos. Si piden "actualizar mysql", pregunta cuál sigue vigente antes de tocar v1, v2 o v3.
5. **Los snippets que escribas son autocontenidos y copiables tal cual:** un solo archivo, sin importar módulos del repo, sin rutas absolutas a tu máquina, sin `C:\Users\tu_usuario`. Si el usuario pide "en python" o "en node", respeta ese lenguaje.
6. **Etiqueta siempre el shell**, es el error más fácil de este repo porque todo va de Windows + WSL: ```powershell para Windows (comandos `wsl`, `docker`, `npm` de Windows) y ```bash para WSL/Linux. Nunca mezcles sintaxis de los dos en un mismo bloque.
7. **Escribir un comando no es ejecutarlo.** No corras el snippet para "comprobar que funciona": aquí eso puede ser un `git reset --hard`, un `DROP TABLE` o una llamada a AWS real. Verifica lo verificable (ver sección 4) y dilo.
8. **No añadas tests, linter ni CI** para un snippet: el repo no tiene ninguno (sección 4). Un `.py` o `.js` suelto se valida con `py_compile` / `node --check`.
9. **El `README.md` raíz ya va atrasado**: solo indexa 5 carpetas (wsl, git, vscode, python, nodejs) de las ~11 que existen. No lo trates como índice exhaustivo y pregunta antes de añadir entradas.

Si el tema encaja con los scripts de AWS existentes, el ⛔ de la sección 3 aplica doble: escribe el snippet en un archivo aparte, no lo ejecutes.

---

## 3. ⛔ No ejecutar scripts de AWS sin autorización explícita

Es la regla más importante del repo. Estos scripts **no son idempotentes y borran datos reales**, varios contra **recursos AWS de producción de terceros** (nombres de tablas/buckets reales de clientes bancarios, p. ej. `mi-tabla-eventos`, `mi-bucket-eventos`, `mi-tabla-sesiones`).

Nunca ejecutes, "para probar", "para ver si funciona" ni como validación:

- `python/clean_dynamodb_v2/delete_s3/app.py` — borra objetos S3 reales, sin condiciones.
- `python/clean_dynamodb_v2/delete_dynamodb/app_v1.py` y `app_v2.py` — `batch_writer().delete_item()` sobre DynamoDB real.
- `aws/cloud/src/dynamodb/main_dy.py`, `aws/cloud/src/s3/main_s3.py` — sobrescriben CSV/downloads locales.
- `aws/cloud/src/models/add_extension.py` — renombra **todos** los archivos del directorio (pasa `old_ext=''`).
- `python/clean_system/clean_system.py` — **borrado masivo del sistema**: limpia `/tmp` y `~/.cache` en Linux/WSL; en Windows borra `C:\`, `C:\Windows\System32`, `C:\Windows\Prefetch`, puntos de restauración y WinSxS. No lo ejecutes jamás sin pedido literal del usuario.

Además, los perfiles AWS que necesitan (`mi-perfil-lectura-dy`, `mi-perfil-escritura-dy`, `mi-perfil-escritura-s3`) son **perfiles SSO corporativos conenciales temporales**, no disponibles fuera de la red del autor. No hay forma de probarlos aquí.

Si el usuario pide verificar un cambio en estos scripts, hazlo leyendo el código o con `python -m py_compile <archivo>` / dry-run con datos ficticios en un directorio temporal. **No** inventes credenciales ni ejecutes contra AWS.

`local-stack/localstack_setup.py` es la excepción *relativamente* segura (apunta a `http://localhost:4566` con creds de LocalStack), pero su bloque `__main__` sí lanza `docker run -d -p 4566:4566 localstack/localstack`. Pide confirmación antes de levantar contenedores.

---

## 4. No hay build, tests, lint, typecheck ni CI

**No existe ningún comando de validación en este repositorio.** Verificado: no hay `pyproject.toml`, `setup.cfg`, `Makefile`, `tox.ini`, `pytest.ini`, `mypy.ini`, `.eslintrc`, `.pre-commit-config.yaml`, ni `.github/` / ningún `.yml` de CI. **Cero archivos de test** en todo el repo.

- No hay `package.json` en la raíz. Los dos `package.json` existentes (bajo `*/scan_dynamodb/`) declaran `"test": "echo \"Error: no test specified\" && exit 1"` — **falla por diseño**, no es un suite roto.
- `aws/cloud/requirements.txt` y los otros `requirements.txt` solo contienen `boto3==1.34.76`. **`aws/cloud` usa `pandas` sin declararlo.** `python/clean_dynamodb_v2` no tiene `requirements.txt` pese a necesitar `boto3`.
- Única validación disponible: `python3 -m py_compile <archivo.py>` y `node --check <archivo.js>`.

No inventes pasos de verificación, ni escribas un `Makefile`, ni añadas un linter "porque el proyecto debería tener uno". Si una tarea exige validación, la única honesta es: lectura del código + `py_compile`/`node --check`, y decirlo explícitamente en el reporte.

**Cuidado con `git status`:** el `.gitignore` raíz solo ignora `*.pptx` y `*.docx`. `temp/`, `exports/`, `node_modules/`, `__pycache__` y `venv` **no** están ignorados globalmente (solo hay `.gitignore` puntuales dentro de algunos subdirectorios de `aws/clean_dynamodb/`). No comitees datos generados.

---

## 5. Convenciones de los scripts utilitarios existentes

Un agente nuevo romperá esto con alta probabilidad. Son convenciones reales del código, no estilos opcionales. **Aplica a los scripts de `aws/`, `local-stack/`, `python/clean_dynamodb_v2/` y `python/clean_system/`** — no son una plantilla para los snippets nuevos de la sección 2 (esos llévatelos autocontenidos y legibles).

1. **Todo se ejecuta a nivel de módulo, sin `if __name__ == "__main__":`.** `import`ar cualquiera de los ~15 `app.py` / `app.js` / `main_*.py` dispara llamadas de red, borrados o un `input()` que bloquea. `split_s3/app.py:15` y `merge_s3/app.py:8` hacen `input()` al importar; `merge_s3/app.py:12` hace `sys.exit(1)`. **Nunca importes estos ficheros para inspeccionarlos** — usa `read`/grep, o haz un Extract de las constantes.
2. **Las rutas son relativas al directorio de trabajo (CWD)**, no al del script: `PATH_DATA = "temp/s3"`, `config/config.json`, `./exports/`. Debes ejecutar desde el directorio que el runbook indique (p. ej. `python3 ./s3/app.py` desde `python/download_data_chatbots_aws/`). Inconsistencia real: `split_s3/app.py` usa `PROJECT_ROOT` derivado de `__file__`, mientras el resto usa CWD — mezclarlos reparte los datos en dos sitios.
3. **Los datos de entrada y salida viven en `temp/` y `exports/`, que no existen en el repo** y no están en `.gitignore`. Créalos explícitamente al probar.
4. **Comentarios y documentación en español, identificadores en inglés.** Mantén el idioma al añadir comentarios/`.md`. Los docstrings y mensajes de log también están en español.
5. **No introduzcas un `if __name__ == "__main__":` como "mejora"** sin que esté en el alcance de la tarea: varios scripts dependen de ejecutarse al importarse. Si lo haces, dilo.
6. Los `requirements.txt` fijan `boto3==1.34.76`; `package.json` usa `@shelf/dynamodb-parallel-scan ^3.4.0` y `archiver ^7.0.1`. No actualices versiones sin pedirlo.

---

## 6. Carpetas duplicadas: elige la copia correcta

Hay árboles casi idénticos donde **un arreglo en uno no llega al otro**. Antes de editar, confirma con el usuario cuál es el vigente y aplica el cambio en ambos si es el caso.

| Copia antigua | Copia nueva / canónica |
|---|---|
| `aws/clean_dynamodb/` (v1) | `python/clean_dynamodb_v2/` |
| `aws/download_data_aws/` | `python/download_data_chatbots_aws/` |
| `aws/localstack/` | `local-stack/` |

Solo difieren en 2–3 ficheros (p. ej. `merge_s3/src/merge.py`, `split_s3/src/split_zip.py`; los `localstack_setup.py`). Además la copia `aws/` tiene **nombres de recursos AWS reales** y `config.json` con creds `test_*` de LocalStack ya commiteadas, mientras que la copia `python/` tiene `bucket_name`/`TABLE_NAME` **vacíos** como plantilla. No copies valores de `aws/` a `python/`.

---

## 7. Los scaffolding escriben en el CWD — no los ejecutes en la raíz

`architecture/clean-architecture/create_clean_architecture.py` usa `os.getcwd()` y crea `backend/`, `frontend/` y `etl/` **en el directorio desde el que lo llames**. `python/scripts/clean_architecture_front_angular/create_angular_clean_project.py` ejecuta `ng new <proyecto>` y luego `os.chdir()`.

Ejecútalos siempre en un directorio destino nuevo y vacío, **nunca en la raíz del repo** (dejarían folders sueltos y `git status` lleno de ruido). Ambos requieren `ng` (Angular CLI) en el PATH. `create_angular_clean_project.py` requiere además `<name-project>` como argumento y parchea `tsconfig.json` y `angular.json` con un reemplazo textual frágil: no lo refactorices esperando tests que no existen.

---

## 8. Documentación: idioma, alcance y drift conocido

- **Todo el contenido y los `README.md` están en español.** Respeta el idioma; si un usuario te escribe en inglés, responde en inglés, pero los archivos que escribas deben ir en español.
- Los runbooks operativos de AWS son el lugar correcto para documentar un comando; `README.md` raíz es el índice de tutoriales (licencia **CC BY-SA 4.0**, a diferencia del `MIT` que dice `architecture/clean-architecture/README.md`).
- **Drift verificado** (documentado ≠ real; corrige el doc si te toca esa zona, no lo propagues):
  - `python/clean_dynamodb_v2/README.md:33` manda editar `scan_dynamodb/app_v3.js` — **ese fichero no existe**; el real es `scan_dynamodb/app.js`.
  - Ese mismo README dice que el split escribe en `temp/dynamodb/$(channel)`, pero el código escribe `$(channel)-<index>`.
  - `python/clean_dynamodb_v2/README.md:80` rotula el paso de DynamoDB como "Configurar el perfil de s3".
  - `architecture/clean-architecture/README.md` promete `src/app/...` y "tres módulos" listando dos; el generador real crea frontend en `src/` y añade un tercer módulo `etl` no documentado.
  - `download_data_*/README.md` intercambia "tabla" y "bucket" entre las secciones de S3 y DynamoDB.
  - La subida a S3 es un **paso manual** (`aws s3 sync`); ningún script del repo la hace.
  - `scan_dynamodb/app.js:7-8` asigna `tableName` y `channel` como globals implícitos (sin `const`/`let`).
  - Módulos huérfanos, sin ningún caller: `split_s3/src/delete_files.py` y `scan_dynamodb/src/zipHandler.js` (este último hace `fs.rmSync` recursivo: no lo "conectes" por tu cuenta).

---

## 9. Git

- Rama por defecto: **`trunk`** (no `main`/`master`). `origin/HEAD → origin/trunk`.
- Historial **mixto**: mensajes Conventional Commits (`feat:`, `docs:`, `refactor:`) conviven con mensajes en español libre (`add clean ddb`, `Update features 20260208`). Para trabajo nuevo usa Conventional Commits en inglés; no reescribas historia existente.
- No hay CI ni hooks, así que nada te va a avisar de un error: valida tú.
- Nunca hagas `reset --hard`, `clean -fd` ni `push --force` sin autorización explícita. Este repo tiene contenido no commiteado con facilidad (`AGENTS.md`, `MEMORY.md`, `ia/`, `docker/docker-wsl-install-guide.md` están sin trackear).
- Historial de commits con contenido de tutoriales únicamente: no esperes granularidad por módulo.

---

## 10. Seguridad

- **Ya saneado (rama `feature/audit-secrets`).** `aws/cloud/src/lambdas/ext_lambda_was.py` tuvo una URL prefirmada de S3 con `X-Amz-Security-Token`, un access key temporal `ASIA*` y la firma, más un correo corporativo. Se sustituyeron por `<URL_PRESIGNADA_REMOVIDA>`, `<CORREO_CORPORATIVO_REMOVIDO>`, `<AWS_ACCOUNT_ID>`, `<CENTRO_COSTO_REMOVIDO>`, `<EQUIPO_REMOVIDO>` y `<VPC_ID>`/`<SUBNET_ID>`/`<SECURITY_GROUP_ID>`, y la historia se reescribió sobre los 53 commits. **Ese archivo es una referencia, no una fuente de datos: no lo rellenes con valores reales.**
- **Lo que sigue en el repo y no debe crecer:** nombres de tablas/buckets de clientes (`mi-tabla-*`, `mi-tabla-*`, `mi-bucket-*`), nombres de perfil SSO (`mi-perfil-*`, `mi-perfil-dev-*`) y la URL de SSO `<ID_INSTANCIA_SSO>.awsapps.com`. Son identificadores, no credenciales, pero acotan qué es la empresa y qué proyectos existen. Si vas a publicar el repo, páralos primero.
- `config/config.json` commiteado: solo claves de LocalStack `test_*` o cadenas vacías. **Nunca** introduzcas credenciales reales ahí; el README ya dice que se rellenan tras pedir un perfil temporal.
- Estos scripts manejan datos de clientes reales: nada de volcarlos a logs, outputs de test ni commits.
- **No vuelvas a escribir rutas con tu nombre ni empresa** (`/mnt/c/<USUARIO>/<EMPRESA>/...`). Las de `aws/localstack/` se enmascararon; no las restaures.

**Si alguna vez debes purgar datos del historial**, el procedimiento que funcionó aquí:

```bash
# 1. SIEMPRE backup fuera del repo antes de tocar historia
git clone --mirror /ruta/al/repo /tmp/opencode/backup.git

# 2. Script de reemplazo literal (binarios, para no romper codificacion)
git filter-branch --tree-filter 'python3 /ruta/scrub.py' --tag-name-filter cat -- --branches

# 3. Las refs de backup de filter-branch mantienen vivo el secreto: borralas
git for-each-ref --format='%(refname)' refs/original | while read r; do git update-ref -d "$r"; done

# 4. Verificar (git log NO basta: hay que escanear los objetos)
git reflog expire --expire=now --all && git gc --prune=now
git cat-file --batch-all-objects --batch | grep -c 'PATRON_SECRETO'

# 5. Force-push y purga final
git push --force origin trunk && git fetch origin && git reflog expire --expire=now --all && git gc --prune=now
```

Aviso real de esta operación: hasta que no hagas el force-push (paso 5), `origin/trunk` sigue apuntando a la historia vieja y **los objetos con el secreto siguen vivos en el store local**. Verifícalo siempre con `git cat-file --batch-all-objects`, no solo con `git log`.

---

## 11. Nota operativa: el repo vive en un mount de Windows

Este checkout está en `/mnt/d/...` (disco de Windows montado en WSL). Los propios tutoriales del repo recomiendan trabajar bajo `/home/<user>/...` porque Docker, Node, Angular y Nest son mucho más lentos sobre `/mnt/*`. Si el usuario reporta lentitud o fallos de permisos/velocidad en scripts Node/Docker, esta es la causa probable: repo en el filesystem Linux.

---

## 12. Cómo trabajar aquí

1. Lee `README.md` (índice) y el `README.md` del subdirectorio afectado antes de tocar un runbook.
2. Determina si el cambio es **documentación** (`.md`) o **script** (`.py`/`.js`), y en qué copia duplicada aplica.
3. Si es un script AWS o de limpieza: no lo ejecutes. Verifica con lectura + `py_compile`/`node --check`.
4. Mantén el español en comentarios y docs; el inglés en identificadores.
5. No añadas tooling (lint, tests, CI, gestor de paquetes raíz) salvo petición explícita.
6. Si encuentras discrepancias entre doc y código dentro del alcance de la tarea, corrige el doc y menciónalo.

### Reporte de cierre

Al terminar una tarea relevante, informa en formato breve:

```text
Estado: COMPLETADA | BLOQUEADA | PARCIAL
Objetivo: <qué se pidió>
Implementado: <cambios>
Archivos creados / modificados: <listas>
Validaciones: <comandos realmente ejecutados y su resultado>
Warnings: <problemas existentes o nuevos>
Decisiones: <solo si hubo alguna>
Pendientes: <solo lo que quede real>
Siguiente paso: <si aplica>
```

No afirmes que algo "funciona" si no lo ejecutaste: aquí casi nada es ejecutable sin credenciales. Di explícitamente "verificado por lectura" o "verificado con `py_compile`".
