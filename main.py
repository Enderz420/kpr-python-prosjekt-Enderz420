# Skriv koden din i denne filen. Du kan kjøre koden med å trykke på "play"-knappen i menyen over.
# Først importerer time for buffer
# Importerer random for sjanse spill
# Importerer decrypt_words og load_words
import time
import random
from cipherDecryption import decrypt_words, load_words

wordlist = load_words("./words_ciphered.txt") # laster ordene i en liste
decrypted_wordlist = list(decrypt_words(wordlist)) # putter de dekrypterte ordene i en annen liste

baby = [] # lister for alle vansklighetsgraden
easy = []
normal = []
hard = []
jesus = []

def append_words(wordlist): # lagrer ordene i gitt listen for å append de til vansklighetsgradene
    for word in wordlist: # kjører gjennom gitt ordliste
        try: 
            if len(word) > 9:
                baby.append(word)
            elif len(word) == 9 or len(word) == 8:
                easy.append(word)
            elif len(word) == 7 or len(word) == 6:
                normal.append(word)
            elif len(word) == 5 or len(word) == 4:
                hard.append(word)
            elif len(word) == 3 or len(word) == 2:
                jesus.append(word)
        except TypeError: # catcher error om den ikke går gjennom
                print("Error 2: Error in appending words")

append_words(decrypted_wordlist) # kaller funksjonen

def sleep(sleep): # Buffer mulighet med dynamisk endring
    time.sleep(sleep)

def difficulties(): # her har man alle vansklighetsgradene
    # Print setninger
    print("Vansklighets grader")
    print('-----------')
    print('En baby klarer dette (Baby) = over 9 bokstaver')
    sleep(1)
    print('Dette klarer alle (Enkel) = 9-8 bokstaver')
    sleep(1)
    print('Helt ok (Normal) = 7-6 bokstaver')
    sleep(1)
    print('Nå begynner det å bli litt vanskelig (Vanskelig) = 5-4 bokstaver')
    sleep(1)
    print('Jesus = 3 bokstaver eller mindre')

def word_picker(difficulty): # Kjører for å sjekke så gi tilbake et ord tilordnet brukerens vansklighetsgrad
    try:
        print(f"{difficulty} valgt. Henter ord.")
        sleep(1) # lat som at den henter noe (selv om den har allerede det)
        if difficulty == 'baby':
            return random.choice(baby)
        elif difficulty == 'enkel':
            return random.choice(easy)
        elif difficulty == 'normal':
            return random.choice(normal)
        elif difficulty == 'vanskelig':
            return random.choice(hard)
        elif difficulty == 'jesus':
            return random.choice(jesus)
    except:
        print("Error 3: Feil ved å velge ord, enten feil input ved vanskelighetsgrad eller så finnes ikke den du prøver å få")
        exit()
def points(string, liv): # gir en poeng sum
    # formelen for poengene er tall * antall liv som er igjen
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
        print("Error 2: Input ikke gyldig")
        print("Prøv igjen senere")
        exit()

def give_points(navn, score, filename): # Gir brukeren poeng og skriver det til highscore filen
    try:
        with open(filename, 'a') as f:
            f.writelines(navn + "\n" + str(score) + "\n") 
            f.close()
    except IOError: # Kjører hvis bruker ikke har spesifisert fil
        print(f"Error 1:{filename} eksisterer ikke, kunne ikke skrive poeng sum") 

def high_score(filename): # Tar in filen og prøver å lese den
    print("Velkommen!")
    print("Vennligst vent til at alt laster.")
    sleep(1)
    print(".")
    sleep(1)
    print("..")
    sleep(1)
    print("...")
    sleep(1)
    print("Takk for at du ventet!") # la de vente for ingen grunn : )
    try: # denne er her for å catch errors
       with open(filename, 'r') as f:
            innhold = f.read()
            print(innhold)
            f.close()
    except IOError: # hvis filen ikke eksisterer
        print(f"Error 1: {filename} eksisterer ikke, prøv igjen senere")
        

def hangman(): # definerer hangman funskjon sånn at jon ikke blir sint på meg
    print("Velkommen til hangman!")
    sleep(2)
    try:
        attempt = int(input("Hvor mange forsøk skal du ha? \n")) # brukeren gir forsøk som blir til en int
        
    except ValueError: # catcher errorer som ikke er en value
        print("Error 4: Verdien er ugyldig vennligst prøv igjen men en ny verdi")
        print("Du blir nå sendt ut av programmet")
        exit()
    difficulties() # viser vansklighetsgrad til brukeren
    difficultyChecker = input("Oppgi vansklighetsgrad \n").strip().lower() # de oppgir det de vil ha og konverterer til lower

    difficulty = ['baby', 'enkel', 'normal', 'vanskelig', 'jesus'] # for å gjøre det mye enklere til å sjekke om de skriver riktig


    if difficultyChecker in difficulty: # sjekker om difficultyChecker er i difficulty listen
        try:
            secret_word = word_picker(difficultyChecker) # velger ord basert på hva man valgte
            if secret_word not in difficulty:
                print("Ingen vansklighet valgt, bruker sendes ut av program")
                exit()
        except:
            print("Error 5: If-setning klarte ikke å løpe")
            exit()

    sleep(2) # late som at det den må generere noe

    while True:  # her begynner det
        guessed_letters = [] # tom liste til guesses
        chosen_word = secret_word.lower()    # konverterer alle bokstavene til lower case og legger de til en variabel
        player_guess = None # holder bokstavene til spilleren
        word_guessed = [] # liste for å gjømme ordet
        for letters in chosen_word: # for antall bokstaver det i ordet så blir de erstattet med -
            word_guessed.append('-') # gjør til at ordet er gjømt

        joined_word = None # trust the process, den skal kombinere alle ordene fra word_guessed listen senere i koden
        
        sleep(1)
        while attempt != 0 and '-' in word_guessed: # while løkke som er aktiv til attempts er under 0
            sleep(2)
            print(("Du har {} førsøk igjen").format(attempt))
            joined_word = "".join(word_guessed) # gjør til at de bokstavene som er rett blir satt sammen
            print(joined_word) # printer over^^

            try: # Spiller input
                player_guess = input("Vennligst gjett en bokstav. \n") # får input
                player_guess = player_guess.lower().strip() # konverterer det til lower case

            except: # Hender hvis input er invalid
                print("Det der skal ikke være gyldig...\nPrøv å skrive noe gyldig.")
                sleep(2)
                continue
            else: 
                if not player_guess.isalpha(): # koden her kjører hvis det ikke er en bokstav
                    print("Ser ut som at det ikke er en bokstav...")
                    sleep(1)
                    print("Dette er hangman...")
                    sleep(1)
                    print("Vennligst prøv igjen.")
                    continue
                elif len(player_guess) > 1: # koden kjøtrer om lengden av input er større en 1
                    print("Det der er flere bokstaver en det du får lov til å gjette.")
                    sleep(1)
                    print("Prøv igjen")
                    continue
                elif player_guess in guessed_letters: # hvis du gjetter en bokstav igjen så kjører denne
                    print("Du har allerede gjettet dette")
                    print("Gjett en annen bokstav nå da.")
                    continue
                else:
                    pass
            guessed_letters.append(player_guess) # legger til unike bokstaver til gussed letter listen

            for idx, letter in enumerate(chosen_word): # kjører gjennom hver bokstav og sjekker om den er i ordet
                if player_guess == letter: # sjekker om det spilleren gjettet er en bokstav i ordet
                    word_guessed[idx] = player_guess #  sjekker hvor den er plassert 
                    print(player_guess, "er en bokstav i ordet!") # printer bokstaven spilleren gjettet
                  
            if player_guess not in chosen_word: # hvis player guess ikke er i ordet så kjører denne
                attempt -= 1 # fjerner et liv
                print("Det ser ut som at", player_guess, "ikke var i ordet.") 
              
        
        if '-' not in word_guessed: # her er vinn kondisjonen, kjører hvis - ikke er i word_guessed                
            score = points(secret_word, attempt) # lagrer poengsum i score variablen
            print("Gratulerer, du vant!")
            print(("{} var ordet!").format(chosen_word))
            print("Du fikk", score, "poeng!") 

            navn = input("Vennligst oppgi navn \n") # oppgi navn 
            str(score) # konverter til string
            give_points(navn, score, "./highscore.txt") # kjører give_points() funksjonen
            break
        else: # hvis ikke kjører denne
            print("Womp womp, du tapte. Prøv igjen så kanskje du finner ut ordet.")
            sleep(3)
            print(("ordet var {} lol").format(chosen_word))
            sleep(5)
            print("hadet lmao")
            break

def main(): # main funksjon 

    while True: # while løkke for å være som en proto-main menu.

        print("----------")
        print("Hangman (h)")
        sleep(1)
        print("----------")
        print("High score (s)")
        sleep(1)
        print("----------")
        print("Vansklighetsgradene (v)")
        sleep(1)
        print("----------")
        sleep(1)
        print("Exit (e)") # jon sin lille exit knapp :)
        print("----------")


        navigation = input("Hva vil du gjøre? \n").strip()      # Konverterer til lower case og fjerner whitespaces

        if navigation.startswith('h'):
            hangman()
        elif navigation.startswith('s'):
            try:   
                high_score('./highscore.txt')
            except IOError:
                print("Error 1: Fil eksisterer ikke vennligst lag en fil med navnet 'highscore'")
        elif navigation.startswith('v'):
            difficulties()
        elif navigation.startswith('e'):
            break
        else:
            print("Input er ikke gyldig prøv igjen.")


if __name__ == '__main__':
    main()