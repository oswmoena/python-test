import random

def check_result(user, op):
    check = ""
    if (user == "Piedra"):
        if (op == "Papel"):
            check = "Perdiste :("
        if (op == "Tijeras"):
            check = "Ganaste!"

    elif (user == "Papel"):
        if(op == "Piedra"):
            check = "Ganaste!"
        if (op == "Tijeras"):
            check = "Perdiste :(!"

    elif (user == "Tijeras"):
        if(op == "Piedra"):
            check = "Perdiste :("
        if (op == "Papel"):
            check = "Ganaste!"
    print(check)

def play():
    exitLoop = False
    choices = {"R": "Piedra", "P": "Papel", "S": "Tijeras"}
    while(exitLoop == False):
        print("presiona R para Piedra")
        print("presiona P para Papel")
        print("presiona S para Tijeras")
        choice = choices[input("Escribe tu respuesta: ").upper()]
        oponentChoice = random.choice(list(choices.values()))
        print(f"has elegido: {choice} y tu oponente: {oponentChoice}")

        if choice == oponentChoice:
            print("Empate!")
        else:
            check_result(user=choice, op=oponentChoice)


        exitLoopInput = input("¿Quieres salir? Y ").upper()
        if (exitLoopInput == "Y"):
            exitLoop = True

if __name__ == '__main__':
    play()
