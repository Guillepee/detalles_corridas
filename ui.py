"""
Created on Wed Jun 28 14:00:18 2023

@author: guillermo.palmieri
"""
import tkinter as tk
import glob
import main as formulas
from tkinter import filedialog

carpeta = ""

def select_folder():
    global carpeta
    carpeta = filedialog.askdirectory()
    return carpeta

def submit():
    selected_options = []
    if var_map.get():
        selected_options.append("Opción 1")
    if var_option2.get():
        selected_options.append("Opción 2")
    if var_option3.get():
        selected_options.append("Opción 3")

    print("Opciones seleccionadas:", selected_options)
    
def ejecutar_excel():
    #Creo la Clase Excel...
    excel = formulas.Excel(carpeta)
    
    if var_map.get():
        excel.mapear()
    print(carpeta)

# Crear la ventana principal
window = tk.Tk()
window.title("Selección de carpeta y opciones")

# Etiqueta y entrada para la carpeta
label_folder = tk.Label(window, text="Carpeta:")
label_folder.grid(row=5,column=1,pady=2,padx=2)

button_select_folder = tk.Button(window, text="Seleccionar carpeta", command=select_folder)
button_select_folder.grid(row=5,column=2,pady=2,padx=10)

# Opciones con botones de verificación
var_map = tk.BooleanVar()
var_option2 = tk.BooleanVar()
var_option3 = tk.BooleanVar()

check_option1 = tk.Checkbutton(window, text="¿Crear Mapa?", variable=var_map)
check_option1.grid(row=8,column=1)

check_option2 = tk.Checkbutton(window, text="Opción 2", variable=var_option2)
#heck_option2.grid(row=9,column=1)

check_option3 = tk.Checkbutton(window, text="Opción 3", variable=var_option3)
#check_option3.grid(row=10,column=1)

# Botón de envío
button_submit = tk.Button(window, text="Generar", command=ejecutar_excel)
button_submit.grid(row=20,column=1)

if __name__ == "__main__":
    # Iniciar el bucle principal de la ventana
    window.mainloop()

