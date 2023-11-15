# Función para los números de perfumería
def perfumes():
    for i in range(1, 100):
        numeros = f'{i:02}'
        yield numeros

# Función para los números de farmacia
def farmacia():
    for i in range(1, 100):
        numeros = f'{i:02}'
        yield numeros

# Función para los números de cosméticos
def costmeticos():
    for i in range(1, 100):
        numeros = f'{i:02}'
        yield numeros

numero_perfume = perfumes()
numero_farmacia = farmacia()
numero_cosmeticos = costmeticos()

# Decorador, un simulador de papel de turno
def decorador(area):
    print("\n" + "*" * 14)
    print("Su número es:")
    if area == 1:
        print(next(numero_perfume))
    elif area == 2:
        print(next(numero_farmacia))
    else:
        print(next(numero_cosmeticos))
    print("Espere su turno")
    print("*" * 14 + "\n")