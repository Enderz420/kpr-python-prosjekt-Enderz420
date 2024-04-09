import string

alfabet = string.ascii_lowercase # hele alfabetet i ascii (engelsk) abcdefghijklmnopqrstuvwxyz

def load_words(word_list): # loads words into a list
    print("Vennligst vent litt")
    wordlist = list() 
    try:    
        with open(word_list, encoding="utf-8") as f: # specify encoding aswell
            for line in f:
                wordlist.append(line.strip('\n'))
        return wordlist
    except IOError:
        print("Error 1: Filen eksister ikke, vennligst prøv en annen fil")


def decrypt(string): # Funksjon for å dekryptere den gitte stringen 
    key = len(string) # Finner ut hvilken key den bruker
    result = "" # lagrer resultatet

    for letter in string: # løke for å kjøre gjennom alle bokstavene i stringen
        if letter in alfabet: # hvis bokstaven er i alfabetet
            letter_index = (alfabet.find(letter) - key) % len(alfabet) # finner posisjonen til bokstaven i alfabetet og evt subtrakterer til modulo (resten)

            result = result + alfabet[letter_index] # legger til bokstaven til result variabelen
        else:
            result = result + letter 
    return result # returnerer result til starten

def decrypt_words(word_list): # for ordlisten
    
    decrypted_wordlist = [] # liste for å lagre alle ordene som blir dekryptert
    for word in word_list: # kjører gjennom hver eneste ord i ordlisten
        decrypted_word = decrypt(word) # lagrer dekryptert ord i en variabel
        decrypted_wordlist.append(decrypted_word) # appender det til en liste
        
    return decrypted_wordlist # sender tilbake listen som ble sendt inn
    

