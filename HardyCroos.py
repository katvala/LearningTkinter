from ast import main
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
# from tkinter.tix import ButtonBox
from tkinter.ttk import *
from turtle import width
from tkinter import messagebox
import math
from math import ceil
from warnings import catch_warnings
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# --inicio--
root=Tk()
root.title('Hardy Cross')
root.iconbitmap('C:/Users/katherine/Documents/LearningTkinter/EXE/usmp.ico')
root.geometry('1080x450+450+150')
root.state('zoomed')

m3=0.0
o3=0.0
q1=0.0
q5=0.0
q8=0.0
s3=0.0
s10=0.0
p7=0.0
q13=0.0
m9=0.0
n10=0.0
m6=0.0

tramo1_km=[]
tramo2_km=[]
tramo1_diametros=[]
tramo2_diametros=[]
tramo1_materiales=[]
tramo2_materiales=[]
entriesMetro1=[]
entriesMetro2=[]
entriesDiametros1=[]
entriesDiametros2=[]
entriesMateriales1=[]
entriesMateriales2=[]


# main frame
main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Canvas 
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add ScrollBar to canvas 
my_scrollbar=Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the canvas 
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
# Another frame inside canvas
second_frame=Frame(my_canvas)
# Add a new frame to a window in the canvas
my_canvas.create_window((0,0),window=second_frame, anchor='nw')

canvasgrafico = Canvas(second_frame, bg='white')
canvasgrafico.grid(column=13,row=0, rowspan=13, columnspan=7, padx=(20,0))
canvasgrafico.create_polygon(105, 150, 135, 80, 255, 80, 285, 150,195,190, outline = 'blue', fill='white') 
canvasgrafico.create_line (195, 190, 195, 80, fill ='blue') 
canvasgrafico.create_line (105, 150, 105, 175, fill ='red') 
canvasgrafico.create_line (135, 80, 110, 60, fill ='red') 
canvasgrafico.create_line (195, 80, 165, 60, fill ='red') 
canvasgrafico.create_line (195, 80, 225, 40, fill ='red') 
canvasgrafico.create_line (255, 80, 285, 60, fill ='red') 
canvasgrafico.create_line (285, 150, 285, 175, fill ='red') 
canvasgrafico.create_line (195, 190, 225, 150, fill ='red') 
canvasgrafico.create_line (195, 190, 225, 215, fill ='red') 
# entradas
e_m9=Entry(canvasgrafico,width='6')
e_m9.place(x=79, y=175)
e_m3=Entry(canvasgrafico,width='6')
e_m3.place(x=85, y=40)
e_o3=Entry(canvasgrafico,width='6')
e_o3.place(x=140, y=40)
e_o5=Entry(canvasgrafico,width='6')
e_o5.place(x=145, y=82)
e_p7=Entry(canvasgrafico,width='6')
e_p7.place(x=152, y=120)
e_q1=Entry(canvasgrafico,width='6')
e_q1.place(x=220, y=20)
e_s3=Entry(canvasgrafico,width='6')
e_s3.place(x=285, y=40)
e_q5=Entry(canvasgrafico,width='6')
e_q5.place(x=205, y=82)
e_s10=Entry(canvasgrafico,width='6')
e_s10.place(x=265, y=175)
e_q8=Entry(canvasgrafico,width='6')
e_q8.place(x=205, y=135)
e_q13=Entry(canvasgrafico,width='6')
e_q13.place(x=225, y=215)


encabezado = Style()
encabezado.configure("encabezado.TLabel", font='arial 10 bold', width='9', anchor='E')

celda=Style()
celda.configure("celda.TLabel", font='arial 10',width='9', anchor='E')

boton =Style()
boton.configure('Boton.TButton', font='arial 10', width='9', background='#003366', foreground='black', refiel='flat')
boton.map('Boton.TButton', background=[("active","#001933")], foreground=[('active','blCK')])

# TODO: Label en Canvas
# def labelCanvas():
def DatosGrafico():
    m9=float(e_m9.get())
    m3=float(e_m3.get())
    o3=float(e_o3.get())
    o5=float(e_o5.get())
    p7=float(e_p7.get())
    q1=float(e_q1.get())
    s3=float(e_s3.get())
    q5=float(e_q5.get())
    q8=float(e_q8.get())
    s10=float(e_s10.get())
    q13=float(e_q13.get())

    lblm6 = Label(canvasgrafico, text=m3-(o5))
    lblm6.place(x=79, y=125)

def GenerarEncabezados(titulos:list, columna:int, fila:int):
    for title in titulos:
        lbl = Label(second_frame, text=title, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S), pady=(30, 0))
        columna+=1

def GenerarColumnaTramo1(columna:int, fila:int):
    tramos=['A-B', 'B-C', 'C-D', 'D-A']
    for tramo in tramos:
        lbl = Label(second_frame, text=tramo, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

def GenerarColumnaTramo2(columna:int, fila:int):
    tramos=['A-D', 'D-E', 'E-F', 'F-A']
    for tramo in tramos:
        lbl = Label(second_frame, text=tramo, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

def LlenarColumna(valores:list,columna:int,fila:int):
    for valor in valores:
        lbl = Label(second_frame, text=valor, style='celda.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

# TRAMO 1

tramo1lbl = Label(second_frame, text='1 Tramo', style='encabezado.TLabel')
tramo1lbl.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

longlbl1 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl1.grid(column=0, row=1, sticky=(W,N,E,S))
mlbl1 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl1.grid(column=1, row=1, sticky=(W,N,E,S))
kmlbl1 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl1.grid(column=2, row=1, sticky=(W,N,E,S))
materiallbl1 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl1.grid(column=3, row=1, sticky=(W,N,E,S))
Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=4, row=1, sticky=(W,N,E,S))
GenerarColumnaTramo1(0,2)

AB_metro = Entry(second_frame,width='8')
AB_metro.grid(column=1, row=2)
entriesMetro1.append(AB_metro)
BC_metro = Entry(second_frame,width='8')
BC_metro.grid(column=1, row=3)
entriesMetro1.append(BC_metro)
CD_metro = Entry(second_frame,width='8')
CD_metro.grid(column=1, row=4)
entriesMetro1.append(CD_metro)
DA_metro = Entry(second_frame,width='8')
DA_metro.grid(column=1, row=5)
entriesMetro1.append(DA_metro)

material_AB = Entry(second_frame,width='8')
material_AB.grid(column=3, row=2)
entriesMateriales1.append(material_AB)
material_BC = Entry(second_frame,width='8')
material_BC.grid(column=3, row=3)
entriesMateriales1.append(material_BC)
material_CD = Entry(second_frame,width='8')
material_CD.grid(column=3, row=4)
entriesMateriales1.append(material_CD)
material_DA = Entry(second_frame,width='8')
material_DA.grid(column=3, row=5)
entriesMateriales1.append(material_DA)



AB_diametro = Entry(second_frame,width='8')
AB_diametro.grid(column=4, row=2)
entriesDiametros1.append(AB_diametro)
BC_diametro = Entry(second_frame,width='8')
BC_diametro.grid(column=4, row=3)
entriesDiametros1.append(BC_diametro)
CD_diametro = Entry(second_frame,width='8')
CD_diametro.grid(column=4, row=4)
entriesDiametros1.append(CD_diametro)
DA_diametro = Entry(second_frame,width='8')
DA_diametro.grid(column=4, row=5)
entriesDiametros1.append(DA_diametro)

# TRAMO 2
tramo2lbl = Label(second_frame, text='2 Tramo', style='encabezado.TLabel')
tramo2lbl.grid(column=6, row=0, columnspan=4)

longlbl2 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl2.grid(column=6, row=1, sticky=(W,N,E,S))
mlbl2 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl2.grid(column=7, row=1, sticky=(W,N,E,S))
kmlbl2 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl2.grid(column=8, row=1, sticky=(W,N,E,S))
materiallbl2 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl2.grid(column=9, row=1, sticky=(W,N,E,S))
Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=10, row=1, sticky=(W,N,E,S))
GenerarColumnaTramo2(6,2)


AD_e = Entry(second_frame,width='8')
AD_e.grid(column=7, row=2)
entriesMetro2.append(AD_e)
DE_e = Entry(second_frame,width='8')
DE_e.grid(column=7, row=3)
entriesMetro2.append(DE_e)
EF_e = Entry(second_frame,width='8')
EF_e.grid(column=7, row=4)
entriesMetro2.append(EF_e)
FA_e = Entry(second_frame,width='8')
FA_e.grid(column=7, row=5)
entriesMetro2.append(FA_e)

material_AD = Entry(second_frame,width='8')
material_AD.grid(column=9, row=2)
entriesMateriales2.append(material_AD)
material_DE = Entry(second_frame,width='8')
material_DE.grid(column=9, row=3)
entriesMateriales2.append(material_DE)
material_EF = Entry(second_frame,width='8')
material_EF.grid(column=9, row=4)
entriesMateriales2.append(material_EF)
material_FA = Entry(second_frame,width='8')
material_FA.grid(column=9, row=5)
entriesMateriales2.append(material_FA)


AD_diametro = Entry(second_frame,width='8')
AD_diametro.grid(column=10, row=2)
DE_diametro = Entry(second_frame,width='8')
DE_diametro.grid(column=10, row=3)
EF_diametro = Entry(second_frame,width='8')
EF_diametro.grid(column=10, row=4)
FA_diametro = Entry(second_frame,width='8')
FA_diametro.grid(column=10, row=5)

# def ObtenerEntradas(entradas, fila, columna):
#     for entry in entradas:
#         fila+=1

def PrimeraTabla():  
    encabezados=['TRAMO','L-Km','D-pulg','C','K','Q-l/s','hf','hf/Q']
    GenerarEncabezados(encabezados, 0, 11)   
    FAlbl2 = Label(second_frame, text=f'{chr(916)} Q-l/s', style='encabezado.TLabel')
    FAlbl2.grid(column=8, row=11, columnspan=2, sticky=(W,N,E,S), pady=(30, 0))    
    encabezados2=['Q-l/s','hf-m']
    GenerarEncabezados(encabezados2,10,11)
    GenerarColumnaTramo1(0,12)

    # graficar km, pulgadas, material
    LlenarColumna(tramo1_km,1,12)
    LlenarColumna(tramo1_diametros,2,12)
    LlenarColumna(tramo1_materiales,3,12)
    # TODO: borrar lbls
    kTramo1=[]
    qls=[]
    for i in range(4):
        k=round(((10**7)*tramo1_km[i]/(5.813*(tramo1_materiales[i]**1.852)*(tramo1_diametros[i]**4.87))),5)
        kTramo1.append(k)

        # ql=round(,2)

    LlenarColumna(kTramo1,4,12)

def GuardarDiametrosMateriales():
    for entry in entriesDiametros1:
        tramo1_diametros.append(float(entry.get()))
    for entry in entriesDiametros2:
        tramo2_diametros.append(float(entry.get()))
    for entry in entriesMateriales1:
        tramo1_materiales.append(float(entry.get()))
    for entry in entriesMateriales2:
        tramo2_materiales.append(float(entry.get()))

def ToKm():
    rowinit=2
    for entry in entriesMetro1:
        km=round(float(entry.get())/1000,2)
        tramo1_km.append(km)
        lbl = Label(second_frame, text=km, style='celda.TLabel')
        lbl.grid(column=2, row=rowinit) 
        rowinit+=1
    print(f'km1:{tramo1_km}')
    rowinit=2
    for entry in entriesMetro2:
        km=round(float(entry.get())/1000,2)
        tramo2_km.append(km)
        lbl = Label(second_frame, text=km, style='celda.TLabel')
        lbl.grid(column=7, row=rowinit) 
        rowinit+=1

    GuardarDiametrosMateriales()
    DatosGrafico()
    
    
def Calcular(*args):
    ToKm()
    PrimeraTabla()

# CALCULAR
btnCalcular = Button(second_frame, text='Calcular', style='Boton.TButton', command=Calcular)
btnCalcular.grid(column=5,row=8, sticky=(W,N,E,S), pady=(20,0))

# keyPress Enter 
root.bind("<Return>", Calcular)

root.mainloop()