# Consola de Turnos

Este pequeño proyecto en Python simula la obtención de turnos para distintas áreas, como perfumería, farmacia y cosméticos. El programa utiliza generadores y un decorador para asignar y mostrar los números de turno correspondientes.

## Archivo `numeros.py`

Este archivo contiene las funciones y generadores necesarios para asignar números a las áreas de perfumería, farmacia y cosméticos.

### Funciones:

- `perfumes()`: Genera números para el área de perfumería.
- `farmacia()`: Genera números para el área de farmacia.
- `cosmeticos()`: Genera números para el área de cosméticos.

### Generadores:

- `numero_perfume`: Generador para números de perfumería.
- `numero_farmacia`: Generador para números de farmacia.
- `numero_cosmeticos`: Generador para números de cosméticos.

### Decorador:

- `decorador(area)`: Simula un papel de turno mostrando el número asignado según el área.

## Archivo `index.py`

Este archivo es el programa principal que importa las funciones del archivo `numeros.py` y se encarga de interactuar con el usuario para asignar turnos.

### Funciones:

- `pregunta()`: Interactúa con el usuario para seleccionar el área deseada.
- `inicio()`: Función principal que gestiona la obtención de turnos y finalización del programa.

## Uso

1. Ejecuta el archivo `index.py`.
2. Selecciona el área a la que te diriges (Perfumería, Farmacia, Cosméticos).
3. Obtén tu número de turno simulado.
4. Decide si deseas obtener otro turno o finalizar el programa.
