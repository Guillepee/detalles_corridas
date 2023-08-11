# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:00:18 2023

@author: guillermo.palmieri
"""
import pandas as pd
import tkinter as tk
import main as formulas
from tkinter import filedialog

carpeta = ""

def select_folder():
    global carpeta
    carpeta = filedialog.askdirectory()
    return carpeta
    
def ejecutar_excel():
    #Creo la clase Excel...
    excel = formulas.Excel(carpeta)
    
    if var_calculos.get():
        excel.iterar_excels()
        excel.crear_base_unificada() #Crea la base unificada con los archivos agregados a la lista datos_excel
        excel.corregir_latitudes()
        
    else: #Agrego a la lista datos_excel la informacion de los excels para unificarla
        for a in excel.archivos_excel:
            corrida = pd.read_excel(a)
            excel.datos_excel.append(corrida) #Agrego las corridas de trenes que me interesa analizar
            
        excel.crear_base_unificada() #Crea la base unificada con los archivos agregados a la lista datos_excel
        excel.corregir_latitudes()
        
    if var_map.get():
        excel.mapear()
    
# Crear la ventana principal
window = tk.Tk()
window.geometry("280x110")
window.title("Selección de carpeta")

# Etiqueta y entrada para la carpeta
label_folder = tk.Label(window, text="Carpeta:")
label_folder.grid(row=5,column=1,pady=2,padx=2,sticky="w")

button_select_folder = tk.Button(window, text="Seleccionar carpeta", command=select_folder)
button_select_folder.grid(row=5,column=2,pady=2,padx=10,sticky="w")

# Opciones con botones de verificación
var_map = tk.BooleanVar()
var_calculos = tk.BooleanVar()
var_option3 = tk.BooleanVar()

check_option1 = tk.Checkbutton(window, text="¿Crear Mapa?", variable=var_map)
check_option1.grid(row=8,column=1,sticky="w",columnspan=3)

check_option2 = tk.Checkbutton(window, text="¿Agregar Calculos?", variable=var_calculos)
check_option2.grid(row=9,column=1,sticky="w",columnspan=3)

# Botón de envío
button_submit = tk.Button(window, text="Generar", command=ejecutar_excel)
button_submit.grid(row=20,column=1,pady=2,padx=20)

if __name__ == "__main__":
    # Iniciar el bucle principal de la ventana
    window.mainloop()

