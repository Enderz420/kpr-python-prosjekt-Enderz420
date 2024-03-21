# Skriv koden din i denne filen. Du kan kjøre koden med å trykke på "play"-knappen i menyen over.
# Først importerer time for buffer
import time

def bufferTid(sleep): # Buffer mulighet med dynamisk endring
    time.sleep(sleep)

def difficulties(): # her har man alle difficulties
    # Print setninger
    print("Difficulty")
    print('-----------')
    print('over 9 bokstaver = En baby klarer dette (Veldig enkel)')
    print('9-8 bokstaver = Dette klarer alle (enkel)')
    print('7-6 bokstaver = Helt ok (Normal)')
    print('5-4 bokstaver = Nå begynner det å bli litt vannskelig (vanskelig)')
    print('3 bokstaver eller mindre = Jesus (Mega vanskelig)')

def difficultySetter(string, liv): # setter difficulty og gir en poeng sum
    
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
        print(("{filename} eksiterer ikke, prøv igjen senere").format())

def rewardGiver(points): # denne skal gi deg kule poeng

    bufferTid(5)

def hangman(): # definerer main funskjon sånn at jon ikke blir sint på meg
    print("Velkommen til hangman!")
    bufferTid(2)

    secret_word = input("Hva er det hemmelige ordet? \n")  # brukeren gir et ord

    if secret_word.isalpha(): # må bare være sikker
        print("Denne ser greit ut!")

    bufferTid(2)

    attempt = int(input("Hvor mange forsøk skal du ha? \n")) # brukeren gir forsøk som blir til en int
    
    if attempt != int:
        print("Det ser ut som at det ikke var et tall")
        print("Prøv igjen senere")
        bufferTid(1)
        exit

    level = difficultySetter(secret_word, attempt) # setter difficulty

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
                    bufferTid(1)
                    print("Gjett en annen bokstav nå da.")
                    continue
                else:
                    pass
            guessed_letters.append(player_guess) # legger til unike bokstaver til gussed letter listen

            for idx, letter in enumerate(chosen_word): # løper gjennom hver bokstav og sjekker om den er i ordet
                if player_guess == letter: # hvis bokstaven er en del av ordet løper denne
                    word_guessed[idx] = player_guess
                    print(player_guess, "er en bokstav i ordet!")
                    bufferTid(1)
                    print(("Du har {} forsøk igjen.").format(attempt))
            if player_guess not in chosen_word: # hvis player guess ikke er i ordet så løper denne
                attempt -= 1
                bufferTid(1)
                print("Det ser ut som at", player_guess, "ikke var i ordet.")
                print(("Du har {} forsøk igjen").format(attempt))
        
        if '-' not in word_guessed: # her er vinn kondisjonen, løper hvis - ikke er i word_guessed                
            print("Gratulerer, du vant!")
            print(("{} var ordet!").format(chosen_word))
            print(("Du fikk {level} poeng!").format(level))
            print("Spille en gang senere da?")
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
        print("----------")
        print("Highscore")
        print("----------")
        print("Difficulty")
        print("----------")
        print("Exit") # jon sin lille exit knapp
        print("----------")


        navigation = input("Hva vil du gjøre? \n")

        NavLow = navigation.lower() # Konverterer til lower case

        if NavLow == 'hangman':
            hangman()
        elif NavLow == 'highscore':
            highScore('./kpr-python-prosjekt-Enderz420/highscore.txt')
        elif NavLow == 'difficulty':
            difficulties()
        elif NavLow == 'exit':
            break
        else:
            print("Input er ikke gyldig prøv igjen.")


if __name__ == '__main__':
    main()