import os
import shutil
import subprocess
from pathlib import Path
import platform
import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

IS_WINDOWS = platform.system() == "Windows"
IS_WSL = "microsoft" in platform.uname().release.lower() and not IS_WINDOWS

if IS_WINDOWS:
    import ctypes

def delete_files_in_folder(folder):
    folder = Path(folder)
    if folder.exists():
        for file in folder.glob("*"):
            try:
                if file.is_dir():
                    shutil.rmtree(file, ignore_errors=True)
                else:
                    file.unlink(missing_ok=True)
            except Exception as e:
                logging.warning(f"Error eliminando {file}: {e}")

def delete_files_by_pattern(folder, patterns):
    folder = Path(folder)
    if folder.exists():
        for pattern in patterns:
            for file in folder.glob(pattern):
                try:
                    if file.is_dir():
                        shutil.rmtree(file, ignore_errors=True)
                    else:
                        file.unlink(missing_ok=True)
                except Exception as e:
                    logging.warning(f"Error eliminando {file}: {e}")

def get_free_space_gb(drive=None):
    """Retorna el espacio libre en GB del disco especificado"""
    if drive is None:
        if IS_WINDOWS:
            drive = "C:\\"
        elif IS_WSL:
            drive = "/mnt/c"
        else:
            drive = "/"
    total_bytes, free_bytes = shutil.disk_usage(drive)[0:3:2]
    return round(free_bytes / (1024 ** 3), 2)

def empty_recycle_bin():
    if IS_WINDOWS:
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
            logging.info("Papelera vaciada (Windows).")
        except Exception as e:
            logging.warning(f"Error vaciando papelera: {e}")
    elif IS_WSL:
        logging.info("Vaciar papelera no es compatible con WSL/Linux.")
    else:
        logging.info("Vaciar papelera solo es compatible con Windows.")

def clean_windows_update_cache():
    if IS_WINDOWS:
        delete_files_in_folder("C:\\Windows\\SoftwareDistribution\\Download")
        logging.info("Caché de Windows Update limpiada (Windows).")
    elif IS_WSL:
        logging.info("Limpieza de caché de Windows Update no disponible en WSL/Linux.")

def clean_logs():
    if IS_WINDOWS:
        delete_files_by_pattern("C:\\Windows\\Logs", ["*.log", "*.bak", "*.tmp"])
        logging.info("Logs de Windows limpiados (Windows).")
    elif IS_WSL:
        logging.info("Limpieza de logs de Windows no disponible en WSL/Linux.")

def clean_thumbnails_and_iconcache():
    if IS_WINDOWS:
        localappdata = os.getenv('LOCALAPPDATA')
        if localappdata:
            explorer_path = Path(localappdata) / "Microsoft" / "Windows" / "Explorer"
            delete_files_by_pattern(explorer_path, ["thumbcache_*"])
            iconcache = Path(localappdata) / "IconCache.db"
            if iconcache.exists():
                try:
                    iconcache.unlink()
                    logging.info(f"IconCache.db eliminado (Windows).")
                except Exception as e:
                    logging.warning(f"No se pudo eliminar IconCache.db: {e}")
    elif IS_WSL:
        logging.info("Limpieza de thumbnails e iconcache no disponible en WSL/Linux.")

def clean_restore_points():
    if IS_WINDOWS:
        try:
            result = subprocess.run(
                ["vssadmin", "delete", "shadows", "/for=C:", "/oldest", "/quiet"],
                capture_output=True, text=True
            )
            if "No se encuentra" in result.stdout or "not found" in result.stdout:
                logging.info("No se encontraron puntos de restauración para eliminar (Windows).")
            else:
                logging.info("Puntos de restauración antiguos eliminados (Windows).")
        except FileNotFoundError:
            logging.warning("vssadmin no encontrado. Solo disponible en Windows con permisos de administrador.")
        except Exception as e:
            logging.warning(f"Error eliminando puntos de restauración: {e}")
    elif IS_WSL:
        logging.info("Eliminación de puntos de restauración no disponible en WSL/Linux.")

def clean_winsxs():
    if IS_WINDOWS:
        try:
            result = subprocess.run(
                ["dism.exe", "/Online", "/Cleanup-Image", "/StartComponentCleanup"],
                capture_output=True, text=True
            )
            if "Error: 740" in result.stdout or "Error: 740" in result.stderr:
                logging.warning("Permisos elevados requeridos para limpiar WinSxS. Ejecuta el script como administrador.")
            else:
                logging.info("WinSxS limpiado (Windows).")
        except FileNotFoundError:
            logging.warning("dism.exe no encontrado. Solo disponible en Windows.")
        except Exception as e:
            logging.warning(f"Error limpiando WinSxS: {e}")
    elif IS_WSL:
        logging.info("Limpieza de WinSxS no disponible en WSL/Linux.")

def clean_browser_cache():
    if IS_WINDOWS:
        localappdata = os.getenv('LOCALAPPDATA')
        if localappdata:
            # Chrome
            chrome_cache = Path(localappdata) / "Google" / "Chrome" / "User Data" / "Default" / "Cache"
            delete_files_in_folder(chrome_cache)
            # Edge
            edge_cache = Path(localappdata) / "Microsoft" / "Edge" / "User Data" / "Default" / "Cache"
            delete_files_in_folder(edge_cache)
            # Firefox
            mozilla_path = Path(localappdata) / "Mozilla" / "Firefox" / "Profiles"
            if mozilla_path.exists():
                for profile in mozilla_path.iterdir():
                    delete_files_in_folder(profile / "cache2")
            logging.info("Caché de navegadores limpiada (Windows).")
    elif IS_WSL:
        logging.info("Limpieza de caché de navegadores de Windows no disponible en WSL/Linux.")

def clean_linux_temp():
    # Limpieza básica de /tmp y ~/.cache en Linux/WSL
    tmp_dir = Path("/tmp")
    home_cache = Path.home() / ".cache"
    if tmp_dir.exists():
        delete_files_in_folder(tmp_dir)
        logging.info("Carpeta /tmp limpiada (Linux/WSL).")
    if home_cache.exists():
        delete_files_in_folder(home_cache)
        logging.info("Carpeta ~/.cache limpiada (Linux/WSL).")

def main():
    logging.info("Limpieza avanzada iniciada...")

    before = get_free_space_gb()
    logging.info(f"Espacio libre antes: {before} GB")

    if IS_WINDOWS:
        # Limpiar carpetas temporales del usuario y del sistema
        temp_folder = os.getenv('TEMP')
        local_temp = os.getenv('LOCALAPPDATA')
        if temp_folder:
            delete_files_in_folder(temp_folder)
            logging.info("Carpeta TEMP del usuario limpiada (Windows).")
        else:
            logging.info("Variable de entorno TEMP no encontrada, omitiendo limpieza de TEMP.")
        if local_temp:
            delete_files_in_folder(os.path.join(local_temp, "Temp"))
            logging.info("Carpeta LOCALAPPDATA\\Temp limpiada (Windows).")

        delete_files_in_folder("C:\\Windows\\Temp")
        delete_files_in_folder("C:\\Windows\\Prefetch")

        # Limpiar archivos temporales y logs en todo el disco C:
        for folder in ["C:\\", "C:\\Windows", "C:\\Windows\\System32"]:
            delete_files_by_pattern(folder, ["*.tmp", "*.log", "*.bak"])

        clean_windows_update_cache()
        clean_logs()
        clean_thumbnails_and_iconcache()
        clean_browser_cache()
        clean_restore_points()
        clean_winsxs()
        empty_recycle_bin()

        try:
            subprocess.run(["cleanmgr.exe", "/sagerun:1"], check=False)
            logging.info("Liberador de espacio ejecutado (Windows).")
        except FileNotFoundError:
            logging.info("cleanmgr.exe no encontrado.")
    elif IS_WSL:
        logging.info("Modo WSL/Linux detectado. Solo se limpiarán carpetas temporales estándar.")
        clean_linux_temp()
    else:
        logging.info("Sistema no soportado para limpieza avanzada. Solo se limpiarán carpetas temporales estándar.")
        clean_linux_temp()

    after = get_free_space_gb()
    logging.info(f"Espacio libre después: {after} GB")
    logging.info(f"Espacio recuperado: {after - before} GB")

if __name__ == "__main__":
    main()