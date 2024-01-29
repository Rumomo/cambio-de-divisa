'''
Created on 29 ene 2024

@author: Ruymán
'''



def opcion1():
    dolar = precio * 0.92
    print("EL cambio dolar a euro es ", dolar, "€")

def opcion2():
    libra = precio * 1.17
    print("EL cambio libra a euro es", libra, "€")

def opcion3():
    rublos = precio * 0.010
    print("EL cambio rublos a euro es", rublos, "€")
    
def opcion4():
    yenes = precio * 0.0062
    print("EL cambio rublos a euro es", yenes, "€")

menu = {
    "1":opcion1,
    "2":opcion2,
    "3":opcion3,
    "4":opcion4
    }

def mostrar_menu():
    print("Menú:")
    print("1. Dolar")
    print("2. Libra")
    print("3. Rublo")
    print("4. Yenes")
    print("5. salir")
    
    opcion = input("Seleccione una opción: ")
    return opcion

while True:
    
    seleccion = mostrar_menu()
    
    if seleccion == "5":
        print("Saliendo del programa")
        break
    
    try:
        precio = float(input("Introduzca el importe en euros: "))
    except ValueError:
        print("Error: Por favor, introduzca un número válido.")
        continue
        
    accion = menu.get(seleccion)
    if accion:
        accion()
    else:
        print("Opción no valida. Por favor, selecione una opción válida")