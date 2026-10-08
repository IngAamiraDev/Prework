# Winget

Stack de texto, imágenes y audio para Windows.

## Actualizar todo sin pedir confirmaciones

```powershell
winget upgrade --all --accept-source-agreements --accept-package-agreements
```

## Texto

```powershell
winget install Python.Python.3.13
winget install OpenJS.NodeJS.LTS
winget install Git.Git
```

Instala:
- `python` → scripting y procesamiento de texto
- `node` / `npm` → herramientas y scripts de JavaScript
- `git` → control de versiones

## Imágenes

```powershell
winget install ImageMagick.ImageMagick
winget install GIMP.GIMP
```

Instala:
- `magick` / `convert` → conversión y edición de imágenes por línea de comandos
- GIMP → edición de imágenes (GUI)

## Audio

```powershell
winget install Gyan.FFmpeg
winget install Audacity.Audacity
winget install VideoLAN.VLC
```

Instala:
- `ffmpeg` → procesamiento y conversión multimedia
- `ffprobe` → inspección de metadata de videos/audio
- `ffplay` → reproducción rápida para pruebas
- Audacity → edición y grabación de audio (GUI)
- VLC → reproducción de audio y video

## Extras para texto (opcional)

```powershell
winget install JohnMacFarlane.Pandoc
winget install BurntSushi.ripgrep.MSVC
winget install Notepad++.Notepad++
```

Instala:
- `pandoc` → conversión entre formatos de documento (md, docx, html, pdf…)
- `rg` (ripgrep) → búsqueda de texto recursiva y rápida
- Notepad++ → editor de texto ligero

## Buscar un paquete

```powershell
winget search <nombre>
```
