import random

#cspell: disable */
def run():
    jugar = True
    scores = []
    
    while jugar:
        intento = 0
        numero_elegido = int(input('Elige un numero del 1 al 100: '))
        numero_aleatorio = random.randint(1, 100)
        while numero_elegido != numero_aleatorio:
            if numero_elegido < numero_aleatorio:
                numero_elegido = int(input('Elige un número más grande: '))
            else:
                numero_elegido = int(input('Elige un número más pequeño: '))
            intento += 1  
        intento = str(intento)
        print('¡Ganaste! en ' + intento + ' intentos')
        jugar = keep()

    scores.append(intento)

def keep():
    option = str(input('Deseas seguir jugando? (S/N): '))
    if(option == "S"):
        return True
    elif(option == "N"):
        return False
    else:
        option = str(input('Ingresa una opcion valida (S/N): '))

if __name__ == '__main__':
    run()