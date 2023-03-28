import os
import constants
from html2image import Html2Image


"""_summary_
    This script converts html files from a directory and subdirectories to png images.
    The output directory is created in the root directory.
    The output directory is named 'images'.
"""

hti = Html2Image()
hti.output_path = constants.OUTPUT_DIR

if os.path.exists(constants.DATA_DIR):

    print(f"Se encontraron los siguientes directorios en el directorio {constants.DATA_DIR}")
    for dirpath, dirnames, filenames in os.walk(constants.DATA_DIR):
        print(filenames)

    files = [os.path.join(dirpath, f) for dirpath, dirnames, files in os.walk(constants.DATA_DIR)
             for f in files if f.endswith('.html')]

    print(f"\nSe encontraron los siguientes archivos html: {files}")
    
    for file in files:
        path = file
        if not os.path.exists(constants.OUTPUT_DIR):
            os.makedirs(constants.OUTPUT_DIR)
        try:
            hti.from_file(path, size=(1920, 1080))
            output_path = os.path.join(
                constants.OUTPUT_DIR,
                f'{os.path.splitext(os.path.basename(file))[0]}.png',
            )
            os.rename(hti.output_path, output_path)
            print(f"Archivo {output_path} creado correctamente!")
        except Exception as e:
            print(f"Error al convertir el archivo {path}: {e}")
else:
    print(f"No se encontró el directorio {constants.DATA_DIR}")



