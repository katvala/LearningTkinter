import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
import math
from turtle import width
from tkinter import messagebox

# --inicio--
root=Tk()
root.title('Población futura')
root.geometry('900x700+450+150')

anios=[]
poblaciones=[]
refAnio=[]
refPoblacion=[]
refLbls=[]
tiempo=0

def graficar():
    try:
        rvalores=[]
        tiempo=int(e_tiempo.get())
        # no me juzguen
        l1 = Label(root, text='r =', font='Arial 15 bold')
        l1.place(x=310, y=140)
        l2 = Label(root, text='(Población actual - Población anterior)', font='Arial 15 underline bold')
        l2.place(x=350, y=130)
        l3 = Label(root, text='   (Tiempo actual - Tiempo anterior)', font='Arial 15 bold')
        l3.place(x=350, y=150)

        ejey=170
        # limpiar cálculo, ref labels
        if(len(refLbls)!=0):
            for ref in refLbls:
                ref.destroy()
        
            refLbls.clear()
            rvalores.clear()
        #TODO: barra lateral en ventana

        for i in range(len(anios)-1):
            l4 = Label(root, text=f'r{i+1} = ', font='Arial 15')
            l4.place(x=310, y=ejey+30)
            refLbls.append(l4)
            # numerador
            l5 = Label(root, text=f'{poblaciones[i+1]} - {poblaciones[i]}', font='Arial 15 underline')
            l5.place(x=350, y=ejey+20)
            refLbls.append(l5)

            # denominador
            l6 = Label(root, text=f'{anios[i+1]} - {anios[i]}', font='Arial 15')
            l6.place(x=350, y=ejey+40)
            refLbls.append(l6)

            # respuesta 
            r=(float(poblaciones[i+1]) - float(poblaciones[i]))/(float(anios[i+1]) - float(anios[i]))
            rRound=format(round(r, 3))
            rlabel=Label(root, text=f'= {rRound}', font='Arial 15')
            rlabel.place(x=450, y=ejey+30)
            refLbls.append(rlabel)
            rvalores.append(float(rRound))

            ejey=ejey+50
        print(f'rvalores: {rvalores}')

        # graficando rp 
        ejex=350
        l7 = Label(root, text=f'rp = ', font='Arial 15')
        l7.place(x=310, y=ejey+30)
        refLbls.append(l7)

        for i in range(len(rvalores)):
            l8 = Label(root, text=f'{rvalores[i]}', font='Arial 15 underline')
            l8.place(x=ejex, y=ejey+20)
            refLbls.append(l8) 
            if(i+1<len(rvalores)):
                l9 = Label(root, text='+', font='Arial 15 underline')
                l9.place(x=ejex+50, y=ejey+20)
                refLbls.append(l9)
            ejex=ejex+60 

        # denominador
        l10 = Label(root, text=f'{len(rvalores)}', font='Arial 15')
        l10.place(x=150+ejex/2, y=ejey+40)
        refLbls.append(l10)

        # respuesta 
        rp=float(format(round(sum(rvalores)/len(rvalores), 3)))
        rlabel=Label(root, text=f'= {rp}', font='Arial 15')
        rlabel.place(x=ejex, y=ejey+30)
        refLbls.append(rlabel)

        # Pf
        Pf_ma=poblaciones[-1]+rp*tiempo 
        print(f'Pf Método Aritmético: {Pf_ma}')
        rlabel=Label(root, text='Pf= Pa + r * t', font='Arial 15 bold')
        rlabel.place(x=650, y=200)
        refLbls.append(rlabel)

        rlabel1=Label(root, text=f'Pf= {poblaciones[-1]} + {rp} * {tiempo} = {Pf_ma}', font='Arial 15')
        rlabel1.place(x=630, y=250)
        refLbls.append(rlabel1)      

        rlabel1=Label(root, text=f'Pf= {int(Pf_ma)}', font='Arial 15 bold')
        rlabel1.place(x=630, y=290)
        refLbls.append(rlabel1)         


    except:
        messagebox.showerror(message='Algo salió mal',title="Error")



def guardarData():
    # bloquear
    # for ref in refAnio:
    #     ref.config(state= "disabled")
    # for refP in refPoblacion:
    #     refP.config(state= "disabled")
    # e_tiempo.config(state='disabled')

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
    # e_tiempo.config(state='normal')
    numData = int(e_data.get())
    if(e_tiempo.get()==''):
        messagebox.showinfo(title='Tiempo', message='Recuerda colocar un periodo antes de presionar el botón calcular')
    label_anio = Label(root, text='Año', font='Arial 20')
    label_anio.place(x=20, y=100)
    label_poblacion = Label(root, text='Población',font='Arial 20')
    label_poblacion.place(x=150, y=100)
    label_metodo1 = Label(root, text='Método Aritmético', font='Arial 25 bold')
    label_metodo1.place(x=300, y=100)
    btnCalcular = Button(root, text="Calcular", width=10, command=guardarData)
    btnCalcular.place(x=650, y=100)
    ejey=130
    
    if(len(refPoblacion)!=0):
        for ref in refAnio:
            ref.destroy()
        for refP in refPoblacion:
            refP.destroy()          
        refPoblacion.clear()
        refAnio.clear()

    for j in range(numData):
        e_anio=Entry(root, width=10)
        e_anio.place(x=20, y=ejey+30*j+1)
        e_poblacion=Entry(root, width=10)
        e_poblacion.place(x=150, y=ejey+30*j+1)
        refAnio.append(e_anio)
        refPoblacion.append(e_poblacion)


l_datos = Label(root, text='¿Cuántos datos tiene?')
l_datos.place(x=150,y=25)
e_data=Entry(root, width=20)
e_data.place(x=300, y=25)
botonGenerar = Button(root, text="Generar", command=EnterNumData)
botonGenerar.place(x=500, y=25)
# botonLimpiar = Button(root, text="Borrar", command=borrar)
# botonLimpiar.place(x=600, y=25)

l_tiempo = Label(root, text='Tiempo')
l_tiempo.place(x=150, y=50)
e_tiempo=Entry(root, width=20)
e_tiempo.place(x=300, y=50)




root.mainloop()