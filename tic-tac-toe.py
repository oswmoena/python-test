import random

positions = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def play():
    print("where you goint to put a X ?")
    game_end = False
    print_table_ex()
    while (game_end == False):
        print("")
        user_played = False
        while user_played == False:
            choice = input("number: ")
            print("")
            if user_play(int(choice) - 1):
                user_played = True
        
        if check_winner("X"):
            print_table()
            print("Congratulations !!!")
            game_end = True
            break
                
        if is_tie():
            print_table()
            print("is a tie!!")
            game_end = True
            break
          
        op_play()
        if check_winner("O"):
            print_table()
            print("sorry, you lose.")
            game_end = True
            break
        
        if is_tie():
            print_table()
            print("is a tie!!")
            game_end = True
            break
        
        print_table()
    
def print_table_ex():
    print("1 | 2 | 3")
    print("- | - | -")
    print("4 | 5 | 6")
    print("- | - | -")
    print("7 | 8 | 9")

def print_table():
    print(f"{positions[0]} | {positions[1]} | {positions[2]}")
    print("- | - | -")
    print(f"{positions[3]} | {positions[4]} | {positions[5]}")
    print("- | - | -")
    print(f"{positions[6]} | {positions[7]} | {positions[8]}")

def op_play():
    play = False
    while play == False:
        number = random.randrange(9)
        if positions[number] == ' ':
            positions[number] = 'O'
            play = True
            
def user_play(position):
    if(positions[position] == " "):
        positions[position] = 'X'
        return True
    else:
        print("Try another position")
        return False
        
def check_winner(fig):
    if positions[0] == fig and positions[1] == fig and positions[2] == fig:
        return True
    elif positions[3] == fig and positions[4] == fig and positions[5] == fig:
        return True
    elif positions[6] == fig and positions[7] == fig and positions[8] == fig:
        return True
    elif positions[0] == fig and positions[4] == fig and positions[8] == fig:
        return True
    elif positions[2] == fig and positions[4] == fig and positions[6] == fig:
        return True
    elif positions[0] == fig and positions[3] == fig and positions[6] == fig:
        return True
    elif positions[1] == fig and positions[4] == fig and positions[7] == fig:
        return True
    elif positions[2] == fig and positions[5] == fig and positions[8] == fig:
        return True
    else:
        return False

def is_tie():
    if " " in positions:
        return False
    else:
        return True

play()