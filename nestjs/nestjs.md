# Nest JS

## Liberar puerto en Windows

### Identificar el proceso que está usando el puerto
`netstat -ano | findstr :6001`

### Liberar el proceso
`taskkill /PID <PID> /F` -> Reemplazar `<PID>` con el número del proceso.

### Verificar que el puerto esté libre
`netstat -ano | findstr :6001`

## Liberar puerto en WSL

### Identificar el proceso que está usando el puerto
`netstat -tuln | grep :6001` || `lsof -i :6001`

### Liberar el proceso
`kill -9 <PID>` -> Reemplazar `<PID>` con el número del proceso.

### Verificar que el puerto esté libre
`netstat -tuln | grep :6001`