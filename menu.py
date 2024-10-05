from tkinter import *
from PIL import Image,ImageTk



def seleccionar():
    ###1
    valor = lista.curselection()# curselection es el nombre predeterminado para agarrar el valor 
    print (valor)
    mostrar = lista.get(valor[0])
    
#    for elemento in valor:
#        print(lista.get(elemento)) #creo q con una lista podrias mostrar todo
    valor2 = lista2.curselection()
    mostrar2 = lista2.get(valor2[0])
    #boton 2
     
    #boton 
    valor3 = lista3.curselection()
    mostrar3 = lista3.get(valor3[0])
    #bebidas
    valor4=listaB.curselection()
    mostrar4= listaB.get(valor4[0])
    # sabor de la bebida
    valor5=listaB2.curselection()
    mostar5=listaB2.get(valor5[0])
    #Elegir
    valor6=ListaElegir.curselection()
    mostrar6=ListaElegir.get(valor6[0])
    #etiqueta
    etiqueta.config(fg="yellow",text=f"""Seleccion:
    Pizza {mostrar}
tipo: {mostrar2} 
con {mostrar3} adicional
1 bebida {mostrar4} sabor {mostar5}
para {mostrar6}""")
    
root =Tk()

img=Image.open("pizza3.jpg")
img=img.resize((900,500))
img= ImageTk.PhotoImage(img)

img2=Image.open("pizza4.jpg")
img2=img2.resize((700,500))
img2=ImageTk.PhotoImage(img2)

img3=Image.open("pizza4.jpg")
img3=img3.resize((200,200))
img3=ImageTk.PhotoImage(img3)

etiquetaROOT=Label(root,image=img)
etiquetaROOT.config(bg="grey10",width=20)
etiquetaROOT.grid()
etiquetaTamaño=Label(etiquetaROOT)
etiquetaTamaño.config(width=0,height=15,bg="grey10")
etiquetaTamaño.grid(row=4)

  ################################  Pizza ################################
###Cuadro Pizza
pizza=Label(etiquetaROOT,image=img2)
pizza.config(bg="azure2",width=30)
pizza.grid(row=0,column=0)
#### titulo
tituloPizza=Label(pizza)
tituloPizza.config(width=6,text="PIZZA",height=2,bg="grey10",fg="yellow",
font=("arial",14))
tituloPizza.grid(row=0,column=1)

### cuadro uno 
cuadro1=Label(pizza)
cuadro1.config(width=1,height=10,bg="green",padx=5)
cuadro1.grid(row=1,column=0)
elementos=["Pequeña","Media","Grande"]
lista= Listbox(cuadro1,exportselection=0)
lista.insert(0,*elementos)
lista.config(selectmode=EXTENDED,selectbackground="green",selectforeground="white",
selectborderwidth=3,width=20,height=7,bg="azure2") # te deja seleccionar miultiples con control
# * para q ponga cada uno como un elemento
lista.grid(row=1,column=0)
titulo1=Label(cuadro1)

titulo1.config(text="Tamaño",width=25,height=1,bg="green")
titulo1.grid(row=0,column=0)

boton1=Button(etiquetaROOT,text="seleccionar",command=seleccionar)
boton1.config(height=1)
boton1.grid(row=2,column=0)

etiqueta=Label(etiquetaROOT)
etiqueta.config(width=45,height=10,bg="grey10")
etiqueta.grid(row=0,column=2)
##### Cuadro 2

cuadro2=Label(pizza)
cuadro2.config(width=5,height=5,bg="old lace")
cuadro2.grid(row=1,column=1)
elementos2={"Margarita","Cuatro quesos","Pepperoni","Napolitana","Hawaiana"}


lista2= Listbox(cuadro2,exportselection=0)
lista2.config(width=20,height=7,selectmode=EXTENDED,bg="azure2",
selectbackground="white smoke",selectforeground="black",selectborderwidth=3)
lista2.insert(0,*elementos2)
lista2.grid(row=1,column=0)
titulo2=Label(cuadro2)
titulo2.config(text="Tipo",width=25,height=1,bg="old lace")
titulo2.grid(row=0,column=0)
#boton2=Button(cuadro2,text="seleccionar",command=seleccionar2)
#boton2.grid()

###### cuadro 3 #####

cuadro3=Label(pizza)
cuadro3.config(width=10,height=10,bg="red",border=2,relief="solid",fg="red")
cuadro3.grid(row=1,column=2)
elementos3={"Pepperoni","Queso","Oregano","Pimienta","Maiz"}
lista3= Listbox(cuadro3,exportselection=0)
lista3.config(width=20,height=7,selectmode=EXTENDED,bg="azure2",
selectbackground="indian red",selectforeground="white",selectborderwidth=3)
lista3.insert(0,*elementos3)
lista3.grid(row=1,column=0)

titulo3=Label(cuadro3)
titulo3.config(text="Adicional",width=25,height=1,bg="red")
titulo3.grid(row=0,column=0)

 ################################   Bebida ################################
###Cuadro Bebida
bebida=Label(etiquetaROOT,image=img2)
bebida.config(width=10,height=10)
bebida.grid(row=1,column=0)
#### titulo bebida

tituloBebida=Label(bebida)
tituloBebida.config(text="BEBIDA",height=1,width=6,fg="yellow",bg="grey10",
font=("arial",14,"italic"))#####
tituloBebida.grid(row=0,column=1)


### cuadro uno 
cuadro1Bebida=Label(bebida)
cuadro1Bebida.config(width=10,height=8,bg="green")
cuadro1Bebida.grid(row=1,column=0)
#elementos={"Pequeña","Media","Grande"}
elementosB=["Pequeña","Mediana","Grande"]
listaB= Listbox(cuadro1Bebida,exportselection=0)
listaB.config(width=20,height=7,selectmode=EXTENDED,selectbackground="green",selectforeground="white",
selectborderwidth=3)
listaB.insert(0,*elementosB)
listaB.grid(row=1,column=0)
#### boton 

tituloTaB=Label(cuadro1Bebida)

tituloTaB.config(text="Tamaño",width=25,height=1,bg="green")
tituloTaB.grid(row=0,column=0)
### cuadro tipo de ebebida 


### cuadro 2##### bebida
cuadroTB=Label(bebida)
cuadroTB.config(width=10,height=5,bg="old lace")
cuadroTB.grid(row=1,column=1)


tituloTaB2=Label(cuadroTB)

tituloTaB2.config(text="Tamaño",width=25,height=1,bg="white")
tituloTaB2.grid(row=0,column=0)

#boton 2
#botonB2=Button(cuadroTB,text="seleccionar",command=seleccionar3)
#botonB2.grid()
elementosB2={"Te","Coca-cola","Colita","Pepsi"}

listaB2= Listbox(cuadroTB,exportselection=0)
listaB2.config(width=20,height=7,selectmode=EXTENDED,selectborderwidth=3,
bg="azure2",selectforeground="black",selectbackground="white") 

listaB2.insert(0,*elementosB2)
listaB2.grid(row=1,column=0)


#cuadro 3 en bebida 
cuadro3Llevar = Label(bebida)
cuadro3Llevar.config(bg="red")
cuadro3Llevar.grid(row=1,column=2)
elementosElegir=["Para llevar","Comer aqui"]
ListaElegir=Listbox(cuadro3Llevar,exportselection=0)
ListaElegir.insert(0,*elementosElegir)
ListaElegir.config(bg="azure",selectbackground="indian red",selectforeground="white",
selectborderwidth=3,height=7)
ListaElegir.grid(row=1,column=0)

tituloElegir=Label(cuadro3Llevar)
tituloElegir.config(text="Elegir",width=25,height=1,bg="red")
tituloElegir.grid(row=0)


###

root.config(bg="grey10")

root.geometry("900x600")
root.mainloop()