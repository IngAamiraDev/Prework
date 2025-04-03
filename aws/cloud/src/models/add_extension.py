import os

def change_extension(directory, old_ext, new_ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(old_ext):
                base = os.path.splitext(file)[0]
                new_file = base + new_ext
                os.rename(os.path.join(root, file), os.path.join(root, new_file))

# Cambia la extensión de .txt a .md en la carpeta unprocessed/
change_extension('../../exports/Wenbot-events/webchat/unprocessed/', '', '.csv')

print("Extensiones agregadas y removidas exitosamente.")