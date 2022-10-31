from words import words
import random

def func():
    word = random.choice(words)
    submit_word = ''
    underscore_leter = []
    failure_tries = 5
    failure = False
    
    if len(word) > 5:
        failure_tries = len(word)
    
    for leter in word:
        underscore_leter.append('-')
    
    while submit_word != word:
        print("")
        print("")
        
        show_word = ''
        submit_word = ''
        hit = False
        
        for x in underscore_leter:
            show_word += f' {x} '
        
        print(f"let's go! {show_word.upper()}")
        print(f"you got only {failure_tries} times to failure!!")
        leterInput = input("type a leter: ")
        for index, leter in enumerate(word):
            if leter == leterInput:
                underscore_leter[index] = leterInput
                hit = True
            submit_word += underscore_leter[index]
        if hit == False:
            print("the leter isn't be in the word :(")
            failure_tries -= 1
        
        print("")
        print("")
        
        if failure_tries == 0:
            failure = True
            break
        
            
    if failure:
        print(f"Perdiste :\'(  la palabra era {word.upper()}")
    else:
        print("Lo lograste! Felicidades :D")
    
func()