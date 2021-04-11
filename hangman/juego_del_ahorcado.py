import random
import os

def get_word():
    with open("./data.txt", "r", encoding="utf-8") as word_file:
        words = [word[:-1] for word in word_file]        
    return random.choice(words)      

def verifyletter(letter_input,spaces,word):
    string, string_complete = "", ""
    lives = True
    complete = False
    for index,value in enumerate(word):
        if value == letter_input:
            lives = False            
            spaces[index] = value

    for letter in spaces:
        string  += letter + " "
        string_complete += letter

    if word == string_complete:
        complete = True

    return string,lives,complete

def main():
    word = get_word()
    count_lives = 5    
    letter_input = ""
    spaces = [_.replace(_,"_") for _ in word]

    os.system("cls")
    print("Welcome to Hangman 🏆 \n")    
    print("¡Guess the word!")    
    string,lives,complete = verifyletter(letter_input,spaces,word)
    print(string)
    while count_lives > 0:
        letter_input =input(('Please enter a letter ✔️ : '))        
        string,lives,complete = verifyletter(letter_input,spaces,word)
        print(string, "\n")
        if lives:
            count_lives = count_lives -1
            if count_lives == 0 :
                print("\n Game Over! ☠️ your word was",word)

        print(f'You have {count_lives} ❤️  oportunities')
        if complete:
            print("\n YOU WIN! 🥇")   
            break                 
    

if __name__ == '__main__':
    main()