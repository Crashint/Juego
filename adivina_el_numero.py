import random

#cspell: disable */
def run():
    jugar = True
    numero_aleatorio = random.randint(1, 100)
    while jugar:
        juego(numero_aleatorio)
        jugar = keep()

def juego(numero_aleatorio):
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    intento = 0
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            numero_elegido = int(input('Elige un número más grande: '))
        else:
            numero_elegido = int(input('Elige un número más pequeño: '))
    intento += 1  
    intento = str(intento)
    print('¡Ganaste! en ' + intento + ' intentos')
    

def keep():
    while True:
        option = str(input('Deseas seguir jugando? (S/N): '))
        if(option == "S"):
            return True
        elif(option == "N"):
            return False
        else:
            option = print('Ingresa una opcion valida')

if __name__ == '__main__':
    run()