# Importamos lo que se encuentra en el archivo numeros.py
import numeros

# Función encargada de guardar el área donde se dirige
def pregunta():
    print("Bienvenido")

    while True:
        print("""
Dónde se dirige?
[1]: Perfumería
[2]: Farmacia
[3]: Cosméticos""")
        # En caso de escoger un número válido, guarda la opción para ser ocupada con numeros.py
        try:
            area = int(input("Elija el área: "))
            [1, 2, 3].index(area)
        except ValueError:
            print("No es una opción válida")
        else:
            break

    numeros.decorador(area)

# Función principal, se encarga de mostrar el turno y en caso de no querer más turnos finalizar el programa
def inicio():
    while True:
        pregunta()

        # En caso de querer otro turno vuelve a preguntar a qué área quiere ir
        try:
            otro_turno = input("Quieres sacar otro turno? S/N: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("No es una opción válida")
        else:
            # Finaliza el programa
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()