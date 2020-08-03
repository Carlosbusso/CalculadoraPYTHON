from tkinter import*
from math import *
#Configuracion de las propiedades de la ventana
ventana=Tk()
ventana.geometry("260x420")
ventana.title("Calculadora")
ventana.configure(background='#4F4659')

#Configuracion de la imagen logo
imagen=PhotoImage(file="logo.png")
fondo=Label(ventana,image=imagen,borderwidth=0).place(x=80,y=5)

#Definimos las variables globales
variable_calculo=0    #Variable para determinar la operacion posterior al dar clic en el boton "=" o "sqrt"
cadena="0123456789."  #string para realizar busqueda en ella y determinar si es numero el boton presionado
cadena1="+-*/"        #string para realizar busqueda en ella y determinar si se dio click a una operacion
operador=""           #variable para mostrar en el display el string
memoria=""            #variable de los botones memoria

#Definimos las dimensiones de los botones
wboton=5
hboton=1

#creacion de cadena para mostrar en el display
input_text=StringVar()

#Creacion de variables de color para los diferentes botones
color_boton1=("#C99CAA")
color_boton2=("#333335")
color_boton3=("#9290A6")
color_text_boton=('white')


#Funcion Clic y logica del funcionamiento de la calculadora
def Clic(num):
    global variable_calculo
    global operador
    num=str(num)

    if variable_calculo==0:     #Verificamos si antes no se dio clic al boton "="

        if operador=="0":       #Verificamos si en el display tenemos el termino "0"
            if cadena.find(num) > -1 :   #Verificamos mediante busqeuda en la cadena si el clic se dio en un numero o en una operacion
                operador=operador.replace(operador[(len(operador) - 1)], str(num))  #se reemplaza el "0" del display por el numero que se dio clic
                variable_calculo=0   #Guardamos 0 en esta variable para definir a la siguiente vez que se da clic que el evento anterior no es la operacion "="

            else:
                operador = operador + str(num) #En caso el clic se da en una operacion este se añade a la cadena
                variable_calculo = 0

        else:
            if cadena.find(num) > -1 :   #Verificamos mediante busqueda en la cadena si el clic se dio en un numero o en una operacion
                operador = operador + str(num)  #Concatenamos el numero a la cadena
                variable_calculo = 0

            else:
                if cadena1.find(operador[(len(operador) - 1)]) > -1 :  #Verificamos si el ultimo termino de la cadena display es una operacion
                    operador=operador.replace(operador[len(operador)-1],str(num))  #Reemplazar este signo por el nuevo que fue presionado
                    variable_calculo = 0
                else:
                    operador = operador + str(num)  #Concatenamos el signo a la cadena
                    variable_calculo = 0

    else:
        if cadena.find(num) > -1 :  #Verificamos si es un numero
            operador = str(num)     #Reemplazamos el resultado por el numero ingresado
            variable_calculo = 0
        else:
            operador = operador + str(num)  #Concatenamos al resultado el signo
            variable_calculo = 0

    input_text.set(operador)        # Visualizacion del string en el display

#Funcion clear

def clear():
    global operador
    operador = ("0")            #Limpiamos el display
    input_text.set(operador)    #Visualizacion del string en el display

#Funcion del boton igual ("="), logica de la operacion del resultado

def operacion():
    global operador
    global variable_calculo
    try:
        flot=eval(operador)
        if type(flot) ==float:
            flot=round(flot,7)   #Limitamos los decimales a 7
        opera = str(flot)
        operador=opera
    except:
        clear()
        opera = ("ERROR")

    input_text.set(opera)       #Visualizacion de los resultados en el display
    variable_calculo=1          #Variable global para determinar la operacion posterior al dar clic en el boton "="

#Funcion raiz cuadrada

def raiz():
    global operador
    global variable_calculo
    try:
        opera = str(round(sqrt(eval(operador)),7)) #Limitamos los decimales a 7
        operador = opera
    except:
        clear()
        opera = ("ERROR")
    input_text.set(opera)   # Visualizacion de los resultados en el display
    variable_calculo = 1    # Variable global para determinar la operacion posterior al dar clic en el boton "sqrt"

#Funcion del boton OFF

def quit():
    global ventana
    ventana.quit()

#Funcion suma memoria

def sumaM():
    global memoria
    global operador
    try:
        if operador == "" :
            operador="0"
        memoria=str(eval(str(memoria)+"+"+str(operador)))   #Sumamos a la variable memoria el numero msotrado en el display
    except:
        opera=("ERROR")


#Funcion resta memoria

def restaM():
    global memoria
    global operador
    try:
        if operador == "" :
            operador="0"
        memoria=str(eval(str(memoria)+"-"+str(operador)))   #Restamos a la variable memoria el numero msotrado en el display
    except:
        opera=("ERROR")


#Funcion llamar memoria

def callM():
     global memoria
     global operador
     operador=memoria
     input_text.set(operador)   #Mostramos la variable memoria en el display

#Funcion limpiar memoria


def clearM():
    global memoria
    memoria="0"   #Limpiamos la memoria


#Creamos nuestros botones
clear()
botonMC=Button(ventana,text="MC",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:clearM()).place(x=17,y=160)
botonMR=Button(ventana,text="MR",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:callM()).place(x=77,y=160)
botonMsuma=Button(ventana,text="M+",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:sumaM()).place(x=137,y=160)
botonMresta=Button(ventana,text="M-",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:restaM()).place(x=197,y=160)
botonOFF=Button(ventana,text="OFF",width=wboton,height=hboton,bg=color_boton1,fg=color_text_boton,command=lambda:quit()).place(x=17,y=200)
botonC=Button(ventana,text="C",width=wboton,height=hboton,bg=color_boton1,fg=color_text_boton,command=lambda:clear()).place(x=77,y=200)
botonSqrt=Button(ventana,text="√",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:raiz()).place(x=137,y=200)
botonDivision=Button(ventana,text="÷",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:Clic("/")).place(x=197,y=200)
boton7=Button(ventana,text="7",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(7)).place(x=17,y=240)
boton8=Button(ventana,text="8",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(8)).place(x=77,y=240)
boton9=Button(ventana,text="9",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(9)).place(x=137,y=240)
botonMultiplicacion=Button(ventana,text="X",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:Clic("*")).place(x=197,y=240)
boton4=Button(ventana,text="4",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(4)).place(x=17,y=280)
boton5=Button(ventana,text="5",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(5)).place(x=77,y=280)
boton6=Button(ventana,text="6",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(6)).place(x=137,y=280)
botonResta=Button(ventana,text="-",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:Clic("-")).place(x=197,y=280)
boton1=Button(ventana,text="1",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(1)).place(x=17,y=320)
boton2=Button(ventana,text="2",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(2)).place(x=77,y=320)
boton3=Button(ventana,text="3",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(3)).place(x=137,y=320)
boton0=Button(ventana,text="0",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(0)).place(x=17,y=360)
botonPunto=Button(ventana,text=".",width=wboton,height=hboton,bg=color_boton3,fg=color_text_boton,command=lambda:Clic(".")).place(x=77,y=360)
botonIgual=Button(ventana,text="=",width=wboton,height=hboton,bg=color_boton2,fg=color_text_boton,command=lambda:operacion()).place(x=137,y=360)
botonSuma=Button(ventana,text="+",width=wboton,height=4,bg=color_boton2,fg=color_text_boton,command=lambda:Clic("+")).place(x=197,y=320)

#Creacion del display
Salida=Entry(ventana,font=('arial',20,'bold'),width=13, textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10,y=65)

#Mostramos nuestra ventana
ventana.mainloop()
