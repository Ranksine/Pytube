"""
    Mini programa para descargar videos de Youtube utilizando la librería Pytube
    (Base back-end lista desarrollarle una interfáz gráfica, bien puede ser en
        web o en android)

    Nota* Es necesario instalar la libreria pytube [pip install pytube]
    Nota* Para crear el ejecutable es necesario lo siguiente:
        - Instalar PyInstaller: [pip install pyinstaller]
        - Ejecutar esta linea en PowerShell:
            Ejecutable directo ->[python -m PyInstaller --onefile main.py]
            Ejecutable con icono ->[python -m PyInstaller --onefile --icon = <<archivoIcono.ico>> main.py]
"""

from pytube import YouTube
import os

try:
    # Crear la carpeta de descargas en el proyecto para almacenar los videos
    carpeta = "Descargas"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    print("Source Library: pytube.io".center(50, '-'), '\n')
    print(" ¡¡Descarga videos de YouTube!! ".center(5,'-'), '\n')

    yt = input('Ingresa el link del video: ')
    yt = YouTube(yt)
    
    print(f"""
          Titulo: {yt.title}
          Autor: {yt.author}
        """)

    # Obtener la duración del video
    duration_sec = int(yt.length)
    mins, secs = divmod(duration_sec, 60)
    print("Duracion: ", "{}:{}".format(mins, secs), "\n")

    # Obtener las calidades de video disponibles para descarga
    calidadesDisponibles = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    print('Selecciona el numero de una de las opciones de calidad disponibles:')
    for x, stream in enumerate(calidadesDisponibles):
        print(f"{x + 1}. {stream.resolution} - {stream.mime_type} - {stream.filesize / (1024*1024):.2f} MB")

    cantidadStreams = len(calidadesDisponibles)
    print(f'{(cantidadStreams + 1)}. Cancelar')

    # Descargar el video
    choice = int(input("Selecciona el número correspondiente a la calidad deseada: "))
    if 1 <= choice <= len(calidadesDisponibles):
        select_stream = calidadesDisponibles[choice - 1]
        select_stream.download(output_path=carpeta)  # output_path establece la ruta en donde se almacenará el video
        print(f'El video: "{yt.title}", se ha descargado correctamente')

        # Informar al usuario la ruta en donde se ha descargado el video
        rutaVideo = os.path.join(carpeta, yt.title + ".mp4")
        print(f"Ruta de descarga: {rutaVideo}")

    elif choice == len(calidadesDisponibles) + 1:
        print("Se ha cancelado el programa, adiós :)")
        exit()
    else:
        print('Selección de calidad inválida')
        
except Exception as e:
    print('Error al realizar la descarga del video: ', e)
    exit()
