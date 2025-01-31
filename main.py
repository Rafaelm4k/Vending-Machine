import os 

Productos = ["Agua 💧", "Refresco 🥤", "Zumo 🧃"]
Precios = [0.50, 0.75, 0.95]
ReservaMonedas = [20, 20, 20,20,20,20]
ValoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
 
def menu(nombres, precios):
    cont = 0
    textomenu = ""
    for nombre in nombres:
        textomenu += f"{cont+1} - {nombre} = {precios[cont]} 💵\n"
        cont += 1
    textomenu += f"{cont+1} - Salir 🚪"
    return textomenu

def ProductoElegido(opcion, Productos, Precios):
    if opcion == 1 or opcion == 2 or opcion == 3:
        return f"\nHas escogido {Productos[opcion - 1]} \nTotal a pagar: {Precios[opcion - 1]}"
    elif opcion == 4:
        return "¡PROGRAMA FINALIZADO!"

def MonedasIngresadas(SumaPago, Precios, ReservaMonedas, ValoresMonedas, opcion):
    precio = Precios[opcion - 1]
    if SumaPago < precio:
        return f"Monto insuficiente, Te falta {round(precio - SumaPago, 2)} 💵"
    cambio = round(SumaPago - precio, 2)
    mensaje = f"Pago recibido: {SumaPago} 💵\nCambio a devolver: {cambio} 💰\n"
    for i in range(len(ReservaMonedas)):
        valor = ValoresMonedas[i]
        while cambio >= valor and ReservaMonedas[i] > 0: 
            cambio = round(cambio - valor, 2)
            ReservaMonedas[i] -= 1 
    if cambio < 0:
        return "No hay suficiente cambio disponible. Compra cancelada."
    return mensaje + "Pago Completado!. ¡Gracias por tu compra! 🛒"


def ActualizarReservaMonedas(Pago, ReservaMonedas, ValoresMonedas):
    for i in range(len(ValoresMonedas)):
        if round(Pago, 2) == round(ValoresMonedas[i], 2):
            ReservaMonedas[i] += 1

opcion = 0
while opcion != 4:
    continuar = True
    print(menu(Productos, Precios))
    opcion = int(input("Escoge una opción: "))
    os.system("cls")
    if opcion == 4:
        print(ProductoElegido(opcion, Productos, Precios))
        continuar = False
    else:
        print(ProductoElegido(opcion, Productos, Precios))
        SumaPago = 0
        while continuar:
            print(MonedasIngresadas(SumaPago, Precios, ReservaMonedas, ValoresMonedas, opcion))
            Pago = float(input(f"Ingresa monedas para completar el pago. 💵 : "))
            ActualizarReservaMonedas(Pago, ReservaMonedas, ValoresMonedas)
            SumaPago += Pago
            if SumaPago >= Precios[opcion - 1]:
                continuar = False
        os.system("cls")
        print(MonedasIngresadas(SumaPago, Precios, ReservaMonedas, ValoresMonedas, opcion))
        print(ReservaMonedas)