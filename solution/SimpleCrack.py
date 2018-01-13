import part_2B

def SimpleCrack(counts, ciphertext):
    
    messages = []
    ks = list(range(0, 26))
    
    #setup an array of decypted messages
    for k in range(0, 26):
        messages.append(SimpleDecrypt(k, ciphertext))
    
    #now we need to sort these messages
    for i in range(0, 25):
        res = part_2B.part_2B(counts, messages[i], messages[i+1])
        if res == 2: #the second message is better
            continue
        elif res == 1: #the first message is better
            messages[i + 1] = messages[i]
            ks[i + 1] = ks[i]
            #replace 2nd with 1st message
    
    return [ks[25], messages[25]]
    
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