import string

alfabet = string.ascii_lowercase # hele alfabetet i ascii (engelsk) abcdefghijklmnopqrstuvwxyz

def loadWords(word_list): # loads words into a list
    print("Vennligst vent litt")
    wordlist = list() 

    with open(word_list) as f:
        for line in f:
            wordlist.append(line.strip('\n'))
    return wordlist


wordlist = loadWords("./words_ciphered.txt")

def decrypt(string):
    cipherKey = len(string)
    result = ""

    for letter in string:
        if letter in alfabet:
            letter_index = (alfabet.find(letter) - cipherKey) % len(alfabet)

            result = result + alfabet[letter_index]
        else:
            result = result + letter
    return result

def decryptWords(word_list):
    
    decrypted_wordlist = []
    for word in word_list:
        decrypted_word = decrypt(word)
        decrypted_wordlist.append(decrypted_word)
        
    return decrypted_wordlist
    

