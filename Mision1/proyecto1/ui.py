# https://docs.python.org/es/3/library/tkinter.html

import tkinter as tk
from tkinter import filedialog, messagebox # Importa el módulo de cuadros de diálogo y mensajes de tkinter
from proccesor import proccess_excel_safe # Importa la función proccess_excel_safe desde el módulo proccesor

def seleccionar_excel(): # Función para seleccionar un archivo Excel 
    return filedialog.askopenfilename( # Abre un cuadro de diálogo para seleccionar un archivo
    title = "Seleccionar archivo Excel", # Título del cuadro de diálogo 
    filetypes = [("Archivos Excel", "*.xlsx *.xls")]  # Filtra para mostrar solo archivos Excel
    )
    

def on_click_procesar():
    archivo = seleccionar_excel() # Llama a la función para seleccionar un archivo Excel y lo guarda en la variable archivo
    exito, mensaje = proccess_excel_safe(archivo) # Llama a la función para procesar el archivo Excel y guarda el resultado en las variables exito y mensaje
    if exito:
        messagebox.showinfo("Éxito", mensaje) # Muestra un mensaje de éxito si el procesamiento fue exitoso
    else:
        messagebox.showerror("Error", mensaje) # Muestra un mensaje de error si hubo un problema durante el procesamiento

# Configuración de la ventana principal
def iniciar_app():
    root = tk.Tk() # Crea la ventana principal de la aplicación
    root.title("Procesador de Excel") # Establece el título de la ventana
    root.geometry("400x400") # Establece el tamaño de la ventana
    root.resizable(False, False) # Deshabilita el redimensionamiento de la ventana

    boton = tk.Button( # Crea un botón para procesar el archivo Excel
        root,
        text="Seleccionar y Procesar Excel", # Texto del botón
        command=on_click_procesar, # Asigna la función on_click_procesar al evento de clic del botón
        width=30, # Ancho del botón
        height=2, # Alto del botón
    )
    boton.pack(pady=20) # Empaqueta el botón en la ventana con un margen vertical
    root.mainloop() # Inicia el bucle principal de la aplicación