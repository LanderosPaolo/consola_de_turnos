# importamos lo que se encuentra en el archivo numeros.py
import numeros

# Funcion encargada de guardar el area donde se dirige
def pregunta():
    print("Bienvenido")

    while True:
        print("""
Donde se dirige?
[1]: Perfumeria
[2]: Farmacia
[3]: Cosmeticos""")
        # en caso de escoger un numero valido, guarda la opcion para ser ocupada con las opciones de numeros.py
        try:
            area = int(input("Elija el area: "))
            [1, 2, 3].index(area)
        except ValueError:
            print("No es una opcion valida")
        else:
            break

    numeros.decorador(area)

# Funcion principal, se encarga de mostrar el turno y en caso de no querer mas turnos finalizar el programa
def inicio():
    while True:
        pregunta()

        # En caso de querer otro turno vuelve a preguntar a que area se quiere ir
        try:
            otro_turno = input("Quieres sacar otro turno? S/N: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("No es una opcion valida")
        else:
            # En caso de que no quiera mas turnos, finaliza el programa
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()