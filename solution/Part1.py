## Part 1. Simple, Block, and Permutation Encryption/Decryption ##

##Part 1A
def SimpleEncrypt(k, message):
    ciphertext = ''
    
    #Ensure message is all uppercase letters, should be redundant
    message = message.upper()
    
    for i in range(0, len(message)):
        
        #Converts letter into unicode
        char = ord(message[i])
        
        #Capital letters are from 65 to 90
        if char < 65 or char > 90:
            #Ignore if not capital letter
            ciphertext = ciphertext + chr(char)
            continue
        #setting A --> 0 for mod purposes
        #A -> 0, B -> 1, etc..
        char = char - 65
        char = (char + k)%26
        char = char + 65
        
        ciphertext = ciphertext + chr(char)
        
    return ciphertext

def SimpleDecrypt(k, ciphertext):
    #Reverse operation of the SimpleEncript
    return SimpleEncrypt(-k, ciphertext)

##Part 1B
def BlockEncrypt(k, text):
    ciphertext = ''
    count = 0
    
    #Work through each character of the text
    for n in range(len(text)):
        #Skip if there is a space (no need to encrypt space)
        if text[n] < 65 or text[n] > 90:
            ciphertext += text[n]
        #Use simple step encryption to encrypt each individual alphabetic character
        else:
            simpK = k[count%len(k)]
            ciphertext += SimpleEncrypt(simpK, text[n])
            count += 1
    
    return ciphertext
    
def BlockDecrypt(k, text):
    #Reverse the operation of BlockEncrypt
    for n in range(len(k)):
        k[n] = -k[n]
    return BlockEncrypt(k, text)

##Part 1C
def PermutationEncrypt(permutation, message):
    dict = {}
    ciphertext = ''
    
    #Create a dictionary with 
    #A->permutation[0]
    #B->permutation[1]
    #etc...
    for i in range(0, len(permutation)):
        dict.update({chr(65 + i):permutation[i]})
    
    for i in range(0, len(message)):
        char = message[i]
        char = dict.get(char, char)
        ciphertext = ciphertext + char
        
    return ciphertext

def PermutationDecrypt(permutation, ciphertext):
    dict = {}
    message = ''
    
    #Create a dictionary with 
    #permutation[0]-> A
    #permutation[1]-> B
    #etc...
    #reverse of above
    for i in range(0, len(permutation)):
        dict.update({permutation[i]:chr(65 + i)})
    
    for i in range(0, len(ciphertext)):
        char = ciphertext[i]
        char = dict.get(char, char)
        message = message + char
        
    return message