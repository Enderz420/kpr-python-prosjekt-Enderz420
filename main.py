# Skriv koden din i denne filen. Du kan kjøre koden med å trykke på "play"-knappen i menyen over.
# Først importerer time for buffer
import time

def bufferTid(sleep): # Buffer mulighet med dynamisk endring
    time.sleep(sleep)

def main(): # definerer main funskjon sånn at jon ikke blir sint på meg
    print("Velkommen til hangman!")
    bufferTid(2)

    secret_word = input("Hva er det hemmelige ordet? ")  # brukeren gir et ord

    if secret_word.isalpha():
        print("Det ser greit ut denne!")

    bufferTid(2)

    attempts = input("Hvor mange forsøk skal du ha? ") # brukeren gir forsøk som blir til en int
    try:
        int(attempts)
        print(attempts)
    except:
        print("Dette er ikke et tall")
        print("Jeg slutter programmet for det da")
        bufferTid(1)
        exit

    while True:
        guessed_letters = [] # empty list til guesses
        
        player_guess = None # holder bokstavene til spilleren
        chosen_word = secret_word.lower()    # konverterer alle bokstavene til lower case og legger de til en variabel
        word_guessed = []
        for letters in chosen_word:
            word_guessed.append('-') # lager sånn at ordet er ----

        joined_word = None # trust the process, den skal kombinere alle ordene word_guessed listen
        
        bufferTid(1)
        while attempts != 0 and '-' in word_guessed: # while løkke som er aktiv til attempts er under 0
            bufferTid(2)
            print(("Du har {} førsøk igjen").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try: # Spiller input
                player_guess = input(("Vennligst gjett en bokstav. ").lower(player_guess)) 
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
                if player_guess == letter:
                    word_guessed[idx] = player_guess
                    print(player_guess, "er en bokstav i ordet!")
                    bufferTid(1)
                    print(("Du har {} forsøk igjen.").format(attempts))
            if player_guess not in chosen_word: # hvis player guess ikke er i ordet så løper denne
                attempts -= 1
                bufferTid(1)
                print("Det ser ut som at", player_guess, "ikke var i ordet.")
                print(("Du har {} forsøk igjen").format(attempts))
        
        if '-' not in word_guessed: # her er vinn kondisjonen, løper hvis - ikke er i word_guessed                
            print("Gratulerer, du vant!")
            print(("{} var ordet!").format(chosen_word))
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


        
main()