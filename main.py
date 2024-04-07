# Skriv koden din i denne filen. Du kan kjøre koden med å trykke på "play"-knappen i menyen over.
# Først importerer time for buffer
import time
import random


def bufferTid(sleep): # Buffer mulighet med dynamisk endring
    time.sleep(sleep)

def difficulties(): # her har man alle difficulties
    # Print setninger
    print("Vansklighets grader")
    print('-----------')
    print('over 9 bokstaver = En baby klarer dette (Veldig enkel)')
    bufferTid(1)
    print('9-8 bokstaver = Dette klarer alle (enkel)')
    bufferTid(1)
    print('7-6 bokstaver = Helt ok (Normal)')
    bufferTid(1)
    print('5-4 bokstaver = Nå begynner det å bli litt vannskelig (vanskelig)')
    bufferTid(1)
    print('3 bokstaver eller mindre = Jesus (Mega vanskelig)')

def loadWords(word_list): # loads words into a list
    # loads words
    print("Vennligst vent litt")

    wordlist = list()

    with open(word_list) as f:
        for line in f:
            wordlist.append(line.strip('\n'))
    return wordlist

def wordPicker(difficulty): # Runs a check to see what difficulty the user picked
    if difficulty == 'veldig enkel':
        return random.choice(veryEasy)
    elif difficulty == 'enkel':
        return random.choice(easy)
    elif difficulty == 'normal':
        return random.choice(normal)
    elif difficulty == 'vanskelig':
        return random.choice(hard)
    elif difficulty == 'mega vanskelig':
        return random.choice(veryHard)

wordlist = loadWords('/kpr-python-prosjekt-Enderz420/words.txt') # Follow up code to get the words into a seperate list

veryEasy = []
easy = []
normal = []
hard = []
veryHard = []

for word in wordlist:
    if len(word) > 9:
        veryEasy.append(word)
    elif len(word) == 9 or len(word) == 8:
        easy.append(word)
    elif len(word) == 7 or len(word) == 6:
        normal.append(word)
    elif len(word) == 5 or len(word) == 4:
        hard.append(word)
    elif len(word) == 3 or len(word) == 2:
        veryHard.append(word)
    else:
        print("Error in appending words")

def difficultySetter(string, liv): # setter difficulty og gir en poeng sum
    # formelen for difficulties er tall * antall liv
    if len(string) > 9:
        poengSum = (2 * liv)
        return poengSum
    elif len(string) == 9 or len(string) == 8:
        poengSum = (5 * liv)
        return poengSum
    elif len(string) == 7 or len(string) == 6:
        poengSum = (10 * liv)
        return poengSum
    elif len(string) == 5 or len(string) == 4:
        poengSum = (15 * liv)
        return poengSum
    elif len(string) == 3 or len(string) == 2:
        poengSum = (20 * liv)
        return poengSum
    else:
        print("Ikke gyldig")
        print("Prøv igjen senere")
        exit

def GivePoints(navn, points, filename): # Gives the user points and writes it into a file
    try:
        with open(filename, 'a') as f:
            f.writelines(navn, points)
            f.close
    except IOError:
        print(("{filename} eksisterer ikke, kunne ikke skrive poeng sum").format())

def highScore(filename): # for om man skal se highscore
    print("Velkommen!")
    print("Vennligst vent til at alt laster.")
    bufferTid(1)
    print("...")
    bufferTid(1)
    print("...")
    bufferTid(1)
    print("...")
    bufferTid(1)
    print("Takk for at du ventet!")
    try: # denne er her for å catch errors
       with open(filename, 'r') as f:
            innhold = f.read()
            print(innhold)
            f.close()
    except IOError:
        print(("{filename} eksisterer ikke, prøv igjen senere").format())

def hangman(): # definerer hangman funskjon sånn at jon ikke blir sint på meg
    print("Velkommen til hangman!")
    bufferTid(2)

    attempt = int(input("Hvor mange forsøk skal du ha? \n")) # brukeren gir forsøk som blir til en int

    print("Hvilken vansklighetsgrad vil du ha?\n")
    difficulties()
    difficultyChecker = input("Oppgi vansklighetsgrad \n")

    difficulty = ['veldig enkel', 'enkel', 'normal', 'vanskelig', 'mega vanskelig'] # for å gjøre det mye enklere til å sjekke om de skriver riktig

    difficultyChecker.islower()
    if difficultyChecker in difficulty:
        secret_word = wordPicker(difficultyChecker)
        level = difficultySetter(secret_word, attempt) # setter difficulty
        int(level)
    else:
        print("Det der er ugyldig")
        print("Hadet")
        exit

    bufferTid(2)

    while True:  # her begynner det
        guessed_letters = [] # empty list til guesses
        
        player_guess = None # holder bokstavene til spilleren
        chosen_word = secret_word.lower()    # konverterer alle bokstavene til lower case og legger de til en variabel
        word_guessed = []
        for letters in chosen_word: 
            word_guessed.append('-') # lager sånn at ordet er ----

        joined_word = None # trust the process, den skal kombinere alle ordene word_guessed listen
        
        bufferTid(1)
        while attempt != 0 and '-' in word_guessed: # while løkke som er aktiv til attempts er under 0
            bufferTid(2)
            print(("Du har {} førsøk igjen").format(attempt))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try: # Spiller input
                player_guess = input("Vennligst gjett en bokstav. \n") # får input
                player_guess = player_guess.lower() # konverterer det til lower case

            except: # Hender hvis input er invalid
                print("Det der skal ikke være gyldig")
                bufferTid(2)
                continue
            else: 
                if not player_guess.isalpha(): # koden her løper hvis det ikke er en bokstav
                    print("Ser ut som at det ikke er en bokstav...")
                    bufferTid(3)
                    print("Dette er hangman...")
                    bufferTid(2)
                    print("Vennligst prøv igjen.")
                    continue
                elif len(player_guess) > 1: # koden løper om lengden av input er større en 1
                    print("Det der er flere bokstaver en det du får lov til å gjette.")
                    bufferTid(1)
                    print("Prøv igjen")
                    continue
                elif player_guess in guessed_letters: # hvis du gjetter en bokstav igjen så løper denne
                    print("Du har allerede gjettet dette")
                    print("Gjett en annen bokstav nå da.")
                    continue
                else:
                    pass
            guessed_letters.append(player_guess) # legger til unike bokstaver til gussed letter listen

            for idx, letter in enumerate(chosen_word): # løper gjennom hver bokstav og sjekker om den er i ordet
                if player_guess == letter: # hvis bokstaven er en del av ordet løper denne
                    word_guessed[idx] = player_guess
                    print(player_guess, "er en bokstav i ordet!")
                    print(("Du har {} forsøk igjen.").format(attempt))
            if player_guess not in chosen_word: # hvis player guess ikke er i ordet så løper denne
                attempt -= 1
                print("Det ser ut som at", player_guess, "ikke var i ordet.")
                print(("Du har {} forsøk igjen").format(attempt))
        
        if '-' not in word_guessed: # her er vinn kondisjonen, løper hvis - ikke er i word_guessed                
            print("Gratulerer, du vant!")
            print(("{} var ordet!").format(chosen_word))
            print("Du fikk", level, "poeng!")
            SaveScore = input("Vil du lagre din score? Y/N? \n")
            SaveScore.islower()

            if SaveScore == 'Y' or 'yes':
                navn = input("Vennligst oppgi navn \n")
                GivePoints(navn, level, "kpr-python-prosjekt-Enderz420/highscore.txt")
                bufferTid(1)
            print("Hadet!")
            break
        else: # hvis ikke løper denne
            print("Womp womp, du tapte. Prøv igjen så kanskje du finner ut ordet.")
            bufferTid(3)
            print(("ordet var {} lol").format(chosen_word))
            bufferTid(5)
            print("hadet lmao")
            break

def main(): # main funksjon 

    while True:

        print("----------")
        print("Hangman")
        bufferTid(1)
        print("----------")
        print("Highscore")
        bufferTid(1)
        print("----------")
        print("Difficulty overview")
        bufferTid(1)
        print("----------")
        bufferTid(1)
        print("Exit") # jon sin lille exit knapp :)
        print("----------")


        navigation = input("Hva vil du gjøre? \n")

        NavLow = navigation.lower() # Konverterer til lower case

        if NavLow == 'hangman':
            hangman()
        elif NavLow == 'highscore':
            highScore('./kpr-python-prosjekt-Enderz420/highscore.txt')
        elif NavLow == 'difficulty' or 'difficulty overview':
            difficulties()
        elif NavLow == 'exit':
            break
        else:
            print("Input er ikke gyldig prøv igjen.")


if __name__ == '__main__':
    main()