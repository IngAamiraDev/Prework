# Resolución de Problemas Comunes con Git

En el desarrollo con Git, es común encontrarse con ciertos problemas y obstáculos. Aquí se describen algunos problemas comunes y las soluciones para abordarlos:

## Problema 1: Conflictos de Fusión (Merge Conflicts)

Los conflictos de fusión ocurren cuando dos ramas contienen cambios en las mismas líneas de código. Git no puede determinar automáticamente cuál es la versión correcta. Para resolver estos conflictos:

1. Ejecuta `git status` para identificar los archivos con conflictos.
2. Abre los archivos conflictivos en un editor de texto y resuelve manualmente los conflictos.
3. Una vez resueltos, ejecuta `git add` para marcar los archivos como resueltos.
4. Realiza un commit para confirmar los cambios resueltos.

## Problema 2: Archivos no Seguidos (Untracked Files)

Los archivos no seguidos son archivos que no están bajo control de versión. Para empezar a rastrearlos:

1. Ejecuta `git status` para ver los archivos no seguidos.
2. Usa `git add` para empezar a rastrear los archivos: `git add nombre_del_archivo`.
3. Realiza un commit para incluir los archivos rastreados en la historia del repositorio.

## Problema 3: Archivos Grandes o Datos Sensibles

En algunos casos, es necesario evitar el seguimiento de archivos grandes o datos sensibles en Git. Puedes utilizar archivos `.gitignore` para excluirlos. Si ya han sido cometidos, puedes utilizar [Git LFS](https://git-lfs.github.com/) para administrar archivos grandes.

## Problema 4: Pérdida de Commits Locales

Si has realizado commits locales que deseas recuperar después de un reinicio o error, puedes utilizar `git reflog` para ver un registro de los commits eliminados y restaurarlos utilizando `git cherry-pick` o `git reset`.

## Problema 5: Olvido de Commits

Si has olvidado hacer un commit y has realizado más cambios, puedes utilizar `git commit --amend` para agregar los cambios olvidados al commit anterior.

## Problema 6: Rama Equivocada

Si has trabajado en la rama equivocada y deseas cambiar a otra rama:

1. Asegúrate de que tus cambios estén confirmados o guardados en un stash.
2. Ejecuta `git checkout nombre_de_la_rama` para cambiar a la rama correcta.

Estos son solo algunos de los problemas comunes que los desarrolladores pueden enfrentar al usar Git. La resolución de problemas en Git es una habilidad esencial en el desarrollo de software, y conocer estas soluciones puede ayudarte a mantener un flujo de trabajo más efectivo.

Si experimentas problemas adicionales, no dudes en buscar ayuda en la comunidad de Git o en recursos en línea. La comunidad de Git es amigable y está dispuesta a ayudar a resolver problemas específicos.

## Problema 7: Host key verification failed

**Error:** Host key verification failed. fatal: Could not read from remote repository. Please make sure you have the correct access rights and the repository exists.
- Agregar a GitHub a la lista de Hosts conocidos
- `ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts`
- `git branch -M main`
- `git push -u origin main`

## Problema 8: You have divergent branches and need to specify how to reconcile them.
**fatal:** Need to specify how to reconcile divergent branches.

- Merge (Combinar): Esta es la estrategia predeterminada y realiza un merge (combinación) de las ramas divergentes, creando un nuevo commit de fusión para incorporar los cambios en ambas ramas. Puedes configurarlo con el siguiente comando:

```sh
git config pull.rebase false
git pull origin main
```

- Rebase (Rebasar): Con esta estrategia, tus cambios locales se aplicarán uno por uno encima de los cambios remotos. Esto reorganiza la historia del proyecto y puede hacer que la línea de tiempo sea más limpia. Puedes configurarlo con el siguiente comando:

```sh
git config pull.rebase true
git pull origin main
```

- Fast-Forward Only (Solo Avance Rápido): Con esta estrategia, se permitirá solo avances rápidos, lo que significa que Git solo permitirá fusionar si no hay cambios en la rama local desde la última sincronización. Puedes configurarlo con el siguiente comando:

```sh
git config pull.ff only
git pull origin main
```

**Nota:** Elige la estrategia que mejor se adapte a tus necesidades y configúrala usando uno de los comandos mencionados anteriormente. Luego, vuelve a ejecutar git pull para traer los cambios y reconciliar las ramas de acuerdo con la estrategia seleccionada.


## Problema 9: failed to push some refs to github.com(...)

1. Realizar un Pull para Sincronizar:
    - `git pull origin main` -> Este comando traerá los cambios desde la rama remota "main" y fusionará esos cambios con tu rama local "main". Si hay conflictos, Git te pedirá que los resuelvas.

2. Resolver Conflictos (si es necesario):
    - Si hay conflictos durante el paso anterior, Git te mostrará los archivos en conflicto. Deberás abrir esos archivos, resolver los conflictos manualmente, y luego hacer un commit para confirmar las resoluciones.

3. Realizar un Push después de Sincronizar:
    - Después de sincronizar y resolver conflictos (si los hay), puedes intentar realizar el push nuevamente:
`git push origin main` Este comando enviará tus cambios locales a la rama "main" en el repositorio remoto.

4. Consideraciones:
    - Si otros colaboradores también están trabajando en la rama "main", es posible que necesites realizar este proceso más a menudo para mantener tu rama local actualizada.
    - Asegúrate de estar trabajando en la rama correcta (main) y de que todos los cambios locales estén comprometidos antes de realizar el pull y push.

Al seguir estos pasos, deberías poder sincronizar tu rama local con la rama remota y realizar el push exitosamente. Si persisten los problemas, asegúrate de revisar los mensajes de error y cualquier indicación adicional proporcionada por Git para obtener más detalles sobre la causa del problema.


## Problema 10: no branch, rebasing main
Indica que actualmente te encuentras en un estado de rebasing (rebase) y no en una rama específica. Esto significa que estás en medio de un proceso de rebase en la rama main. Durante un rebase, Git está reorganizando tus cambios locales sobre la base de los cambios más recientes en la rama remota main.

1. Completar el Rebase:
    - Si Git está en medio de un rebase, puedes completarlo ejecutando: `git rebase --continue`
    - Si hay conflictos durante el rebase, Git te pedirá que los resuelvas antes de continuar con el rebase. En ese caso, utiliza:
    - `git rebase --skip` -> si deseas omitir los cambios en conflicto
    - `git rebase --abort`  -> si deseas cancelar el rebase por completo
    - Luego, vuelve a intentar el proceso de rebase desde el principio.

2. Hacer Pull para Sincronizar:
    - Después de completar el rebase, realiza un pull para asegurarte de tener los cambios más recientes de la rama remota main: `git pull origin main`
    - Esto asegurará que estés completamente sincronizado antes de intentar el push.

3. Hacer Push:
    - Finalmente, después de completar el rebase y asegurarte de que estás sincronizado, intenta hacer push nuevamente: `git push origin main`
    - Esto debería permitirte enviar tus cambios actualizados a la rama remota main.

Recuerda que es importante tener cuidado al realizar rebase, especialmente si estás trabajando en una rama compartida con otros colaboradores. El rebase reescribe la historia del repositorio, y puede causar conflictos si otros colaboradores también han realizado cambios en la misma rama. En entornos colaborativos, la preferencia puede ser usar merge en lugar de rebase para evitar complicaciones.