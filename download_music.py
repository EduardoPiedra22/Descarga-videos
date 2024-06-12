import  tkinter as tk
from pytube import YouTube


windows = tk.Tk()
windows.title ("Descargar Musicas")
# Configuracion de  Dimensiones:
etiqueta = tk.Label(windows, text="Url de la musica a descargar: ")
etiqueta.pack()
url = tk.Entry(windows, width=30)
url.pack()

windows.geometry("600x300")

def download ():
    try: 
        link = url.get()
        linkyutu = YouTube(link)
        video = linkyutu.streams.get_highest_resolution()
        video.download()
        fini_label.config(text = "Descarga completada")
    except:
        fini_label.config(text = "hubo un error al descargar el video")


boton = tk.Button(windows, text='Descargar', command=download)
boton.pack()
fini_label = tk.Label(windows, text="")
fini_label.pack()
windows.mainloop()
