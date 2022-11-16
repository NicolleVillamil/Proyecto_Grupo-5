from tkinter import ttk
import tkinter as tk
from tkinter import *

proyecto = Tk()
proyecto.title('Calculadora de masa atomica')
proyecto.config(bg="PaleTurquoise1")
proyecto.geometry("1000x260")

#imagenes
frame0 = Frame(proyecto, bg="PaleTurquoise1", width=100, height=260)
frame0.config(bd=6)
frame0.config(relief="groove")
frame0.config(cursor="plus")
frame0.pack(side=LEFT,anchor=NE)
img0 = PhotoImage(file="uno1.png")
widget = Label(frame0, image=img0).pack()


frame1 = Frame(proyecto, bg="peach puff", width=600, height=300)
frame1.config(bd=5)
frame1.config(relief="groove")
frame1.config(cursor="plus")
frame1.pack()
img = PhotoImage(file="dos.png")
widget = Label(frame1, image=img).pack()


frame = Frame(proyecto, bg="peach puff", width=2000, height=2000)
frame.config(bd=10)
frame.config(relief="groove")
frame.config(cursor="plus")
frame.pack()
        
#Textos
elementolabel = Label(frame,text="Elemento",fg="brown4",bg="peach puff",font=("Helvetica",10, "bold"))
elementolabel.grid(row=0,column=0)
masalabel = Label(frame,text="Masa Atmica",fg="brown4",bg="peach puff",font=("Helvetica",10, "bold"))
masalabel.grid(row=0,column=2)
atomolabel = Label(frame,text="N° De Átomos",fg="brown4",bg="peach puff",font=("Helvetica",10, "bold"))
atomolabel.grid(row=0, column=4)

dicc ={"H":1.008,"He":4.003,"Li":6.941,"Be":9.012,"B":10.811,"C":12.011,"N":14.007,"O":15.999,
"F":18.998,"Ne":20.1797,"Na":22.987,"Mg":24.305,"Al":26.981,"Si":28.086,"P":30.9737,
"S":32.066,"Cl":35.453,"Ar":39.948,"K":39.098,"Ca":40.080,"Sc":44.956,"Ti":47.880,
"V":50.941,"Cr":51.996,"Mn":54.938,"Fe":55.847,"Co":58.933,"Ni":58.690,"Cu":63.546,
"Zn":65.390,"Ga":69.723,"Ge":72.610,"As":74.921,"Se":78.98,"Br":79.904,"Kr":83.80,
"Rb":85.468,"Sr":87.620,"Y":88.906,"Zr":91.224,"Nb":92.906,"Mo":95.940,"Tc":98.000,
"Ru":102.905,"Rh":102.905,"Pd":106.420,"Ag":107.868,"Cd":112.411,"In":114.820,"Sn":118.710,
"Sb":121.750,"Te":127.600,"I":126.905,"Xe":131.29,"Cs":132.905,"Ba":137.270,"La":138.905,
"Ce":140.908,"Pr":140.907,"Nd":88.906,"Pm":145,"Sm":150.36,"Eu":151.985,"Gd":157.25,"Tb":158.925,
"Dy":162.50,"Ho":164.930,"Er":167.26,"Tm":168.934,"Yb":173.04,"Lu":174.97,"Hf":178.49,"Ta":180.948,
"W":183.850,"Re":186.207,"Os":190.2,"Ir":192.22,"Pt":195.08,"Au":196.966,"Hg":200.59,"Tl":204.383,
"Pb":207.2,"Bi":208.980,"Po":209,"At":210,"Rn":222,"Fr":223,"Ra":226.025,"Ac":227.078,"Th":232.038,
"Pa":231.035,"U":238.029,"Np":237.048,"Pu":244,"Am":243,"Cm":247,"Bk":247,"Cf":251,"Es":252,
"Fm":257,"Md":258,"No":259,"Lr":260,"Rf":261,"Db":262,"Sg":263,"Bh":264,"Hs":265,"Mt":268}


#Espacios
espacio1 = Label(frame,text="",fg="brown4",bg="peach puff")
espacio1.grid(row=0,column=1)
espacio2 = Label(frame,text="",fg="brown4",bg="peach puff")
espacio2.grid(row=0,column=3)
espacio3 = Label(frame,text="",fg="brown4",bg="peach puff")
espacio3.grid(row=1,column=1)
espacio4 = Label(frame,text="",fg="brown4",bg="peach puff")
espacio4.grid(row=1,column=3)

#Combo Box
opcion = ttk.Combobox(frame, width = 10, values = list(dicc.keys()))
opcion.grid(row = 1, column = 0)
opcion.current()
        
#Cuadro de texto desactivado
cuadromasatomica = Entry(frame)
cuadromasatomica.grid(row=1,column=2)
cuadromasatomica.config(state = tk.DISABLED)

#Cuadro de texto
cuadroatomo = Entry(frame)
cuadroatomo.grid(row=1,column=4)

def seleccionar():
    cuadromasatomica.config(state = tk.NORMAL)
    cuadromasatomica.delete(0,END)
    cuadromasatomica.insert(0,dicc[opcion.get()])
    cuadromasatomica.config(state = tk.DISABLED)

def calcular():
    cuadromasatomica.config(state = tk.NORMAL)
    cuadromasatomica.delete(0, END)
    cuadromasatomica.insert(0, round(float(dicc[opcion.get()])*float(cuadroatomo.get()),2))
    cuadromasatomica.config(state = tk.DISABLED)

#Botones
btn_seleccion = Button(frame, text="Seleccionar")
btn_seleccion.grid(row=3,column=0)
btn_seleccion.config(command=seleccionar)

btn_calcular = Button(frame, text="Calcular")
btn_calcular.grid(row=3,column=2)
btn_calcular.config(command = calcular)

proyecto.mainloop()