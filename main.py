"""
Maquina Expendedora

1 def funciones 
2 podemos crear arrays bidimensionales o dos arrays, productos y precios


"""
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

print(menu(Productos,Precios))