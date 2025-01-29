"""
Maquina Expendedora

"""
import os 

Productos = ["Agua 💧" , "Refresco 🥤" , "Zumo 🧃" ]
Precios = [0.50,0.75,0.95]
ReservaMonedas = [20,20,20,20,20]
ValoresMonedas = [2,1,0.50,0.20,0.10,0.05]

def menu(nombres,precios):
    cont = 0
    textomenu = ""
    for nombre in nombres:
        textomenu += f"{cont+1} - {nombre}  = {precios[cont]} 💵\n"
        cont += 1
    textomenu += f"{cont+1} - Salir 🚪"
    return textomenu

def ProductoElegido(opcion, Productos , Precios):
    if opcion == 1 or opcion == 2 or opcion == 3 :
        return f"\nHaz Escogido {Productos[opcion - 1]} \nTotal a Pagar : {Precios[opcion - 1]}"
    elif opcion == 4:
        return "¡PROGRAMA FINALIZADO!"

continuar = True
while continuar : 
    print(menu(Productos,Precios))
    opcion = int(input("Escoge una Opcion "))
    os.system("cls")
    if opcion == 4:
        print(ProductoElegido(opcion,Productos,Precios))
        continuar = False
    else:
        print(ProductoElegido(opcion,Productos,Precios))
        pago = float(input("Ingresa Las monedas necesarias para pagar el producto "))
    