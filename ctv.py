import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
import math
from turtle import width
from tkinter import messagebox
from math import floor

# --inicio--
root=Tk()
root.title('Población futura')
root.geometry('1300x950')

anios=[]
poblaciones=[]
refAnio=[]
refPoblacion=[]
refLbls=[]

def aritmetico():
    rvalores=[]
    tiempo=int(e_tiempo.get())
    for i in range(len(anios)-1):
        r=(float(poblaciones[i+1]) - float(poblaciones[i]))/(float(anios[i+1]) - float(anios[i]))
        rRound=format(round(r, 3))
        rvalores.append(float(rRound))
    
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_ma
    Pf_ma=round(poblaciones[-1]+rp*tiempo,3)
    print(f'Método Aritmético: {Pf_ma}')
    return Pf_ma


def interes():
    rvalores=[]
    tiempo=int(e_tiempo.get())

    for i in range(len(anios)-1):
        r=(poblaciones[i+1] - poblaciones[i])/(poblaciones[i]*((anios[i+1]) - anios[i]))
        rRound=format(round(r, 3))
        rvalores.append(float(rRound))
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_mi
    Pf_mi=round(poblaciones[-1]*(1+rp*tiempo),3)
    print(f'Método Interés: {Pf_mi}')
    return Pf_mi

def geometrico():
    rvalores=[]
    tiempo=int(e_tiempo.get())

    for i in range(len(anios)-1):
        r=((poblaciones[i+1]/poblaciones[i])**(1/(anios[i+1] - anios[i])))-1
        rRound=round(r, 3)
        rvalores.append(rRound)
        print(f'r: {r}')
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_mg
    Pf_mg=round(poblaciones[-1]*((1+rp)**tiempo),3)
    print(f'Método Geométrico: {Pf_mg}')
    return Pf_mg

def graficar():
    # debería ser int Habitantes...
    try:
        ma = aritmetico()
        mi = interes()
        mg = geometrico()
        Lbl1 = Label(root, text=f'Método Aritmético:', font='Arial 17')
        Lbl1.place(x=310, y=130)
        lma = Label(root, text=f'Pf= {floor(ma)} habitantes', font='Arial 17 bold')
        lma.place(x=500, y=130)
        Lbl1 = Label(root, text=f'Método Interés Simple:', font='Arial 17')
        Lbl1.place(x=310, y=160)
        lmi = Label(root, text=f'Pf= {floor(mi)} habitantes', font='Arial 17 bold')
        lmi.place(x=500, y=160)
        Lbl1 = Label(root, text='Método Geométrico: ', font='Arial 17')
        Lbl1.place(x=310, y=190)
        lmg = Label(root, text=f'Pf= {floor(mg)} habitantes', font='Arial 17 bold')
        lmg.place(x=500, y=190)
        lPf = Label(root, text=f'Pf= {floor((mi+mg)/2)} habitantes', font='Arial 17 bold')
        lPf.place(x=320, y=220)
        refLbls.append(lma)
        refLbls.append(lmi)
        refLbls.append(lmg)
        refLbls.append(lPf)

        # limpiar cálculo, ref labels
        # if(len(refLbls)!=0):
        #     for ref in refLbls:
        #         ref.destroy()
        
        #     refLbls.clear()
        #     rvalores.clear()


    except NameError as e:
        messagebox.showerror(message=e,title="Error")

def guardarData():
    anios.clear()
    poblaciones.clear()

    for x in refAnio:
        anios.append(int(x.get()))
    
    for y in refPoblacion:
        poblaciones.append(int(y.get()))

    print(f'Anio: {anios}')
    print(f'Poblacion: {poblaciones}')

    graficar()

def EnterNumData():
    numData = int(e_data.get())
    if(e_tiempo.get()==''):
        messagebox.showinfo(title='Tiempo', message='Recuerda colocar un periodo antes de presionar el botón calcular')
    label_anio = Label(root, text='Año', font='Arial 20')
    label_anio.place(x=50, y=100)
    label_poblacion = Label(root, text='Población',font='Arial 20')
    label_poblacion.place(x=155, y=100)
    ejey=130
    
    if(len(refPoblacion)!=0):
        for ref in refAnio:
            ref.destroy()
        for refP in refPoblacion:
            refP.destroy()    
        for refL in refLbls:
            refL.destroy() 
        refLbls.clear()    
        refPoblacion.clear()
        refAnio.clear()

    for j in range(numData):
        e_anio=Entry(root, width=10)
        e_anio.place(x=20, y=ejey+30*j+1)
        e_poblacion=Entry(root, width=10)
        e_poblacion.place(x=150, y=ejey+30*j+1)
        refAnio.append(e_anio)
        refPoblacion.append(e_poblacion)
        if(j+1==numData):
            btnCalcular = Button(root, text="Calcular", width=10, command=guardarData)
            btnCalcular.place(x=65, y=ejey+(30*numData))
            refLbls.append(btnCalcular)


l_datos = Label(root, text='¿Cuántos datos tiene?')
l_datos.place(x=150,y=25)
e_data=Entry(root, width=20)
e_data.place(x=300, y=25)
botonGenerar = Button(root, text="Generar Espacios", command=EnterNumData)
botonGenerar.place(x=500, y=25)
# botonLimpiar = Button(root, text="Borrar", command=borrar)
# botonLimpiar.place(x=600, y=25)

l_tiempo = Label(root, text='Tiempo')
l_tiempo.place(x=150, y=50)
e_tiempo=Entry(root, width=20)
e_tiempo.place(x=300, y=50)




root.mainloop()