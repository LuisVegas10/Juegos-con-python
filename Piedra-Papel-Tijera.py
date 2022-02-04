import random

'''
Este ejercicio simula el juego de 'Piedra', 'Papel', y 'Tijera'.
'''


# DONE: Esta funcion devuelve el movimiento seleccionado por el usuario
def selectMovimiento() -> str:
    while True:  # Un ciclo que se repetira hasta que se ingrese un numero valido
        try:
            index = int(input("Seleccione su movimiento: "))
            if index >= 1 and index <= 3:
                return index
            elif index < 1:
                print("¡¡EL MOVIMIENTO SELECCIONADO DEBE SER MAYOR A 0!!")
            else:
                print("¡¡EL MOVIMIENTO SELECCIONADO DEBE SER ENTRE 1 Y 3!!")
        except Exception as exception:
            print("¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!")


# Diccionario con la lista de movimiento y contra que movimiento es efectivo.
TablaMovimientos = {"Piedra": "Tijera", "Papel": "Piedra", "Tijera": "Papel"}

# Muestra la lista de movimiento
print("Movimientos disponibles:")
for index, item in enumerate(TablaMovimientos):
    print(f"— {index + 1}. {item}")

# Pide al usuario seleccionar un movimiento
movimiento_Jugador = list(TablaMovimientos)[selectMovimiento() - 1]
# El oponente selecciona un movimiento randon
movimiento_CPU = list(TablaMovimientos)[random.randrange(0, 3)]

# Muestra el resultado
print(f"\nTu elegiste: —{movimiento_Jugador}—.\n" +
      f"El oponente eligió: —{movimiento_CPU}—.\n\n" +
      "Resultado:")

if movimiento_Jugador == movimiento_CPU:
    print("——Empate——.")
elif TablaMovimientos[movimiento_Jugador] == movimiento_CPU:
    print(f"——Ganaste——")
else:
    print(f"——Perdiste——")
