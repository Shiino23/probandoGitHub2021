from csv import writer
import csv
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()

nColumna = int(input("inserte de forma numerica la columna en la cual se encuentra el archivo: "))

nColumna -= 1

#Libro csv con la info
libroCSV = []

#Data a trabajar
datos = []

#Data trabajada
resultado = {}

#Lectura de ruta de archivo desde Tkinter
def openFile():
    file= filedialog.askopenfilename(title="abrir") 
    libroCSV.append(file)

#Lectura de archivo CSV que proporciona la data que se analizara #
def CSVReader(archivo):
    with open(str(archivo), newline = "") as f:
        reader = f.read()
        lines= reader.splitlines()
        lines.pop(0)
        for row in lines: 
            lines = row.split(";")
            datos.append(lines[nColumna])

#Script que valida la conectividad de los equipos
def scriptingIP(lista):
    for ip in datos:
        pingin = os.popen("ping " + ip).read()
        if "recibidos = 4" in pingin or "received = 4" in pingin:
            resultado[str(ip)] = "Responde"
        else:
             resultado[str(ip)] = "No responde"

#Escritura de todo el trabajo realizado en un nuevo csv
def CSVWriter(resultados):
    with open('resultado.csv', 'w') as f:  
        writer = csv.writer(f)
        for k, v in resultados.items():
            writer.writerow([k, v])

#Ejecucion del programa
def execute():
    CSVReader(libroCSV[0])
    scriptingIP(datos)
    CSVWriter(resultado)
    print(resultado)
    
        
frame = ttk.Frame(root, padding = 50).pack()
botonOpen = ttk.Button(frame, text = "Archivo", padding= 10, command=openFile).pack()
botonExecute = ttk.Button(frame, text = "Ejecutar", padding= 10, command= execute).pack()


root.mainloop()