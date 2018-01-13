def PermutationCrack(ciphertext)
    message = ''
    parentKey = ''
    iterations = 100000
    maxScore = -1000000
    
    #Generate random key 
    for i in range(0, 26)
        j = random.randint(0, 26)
        key = key + chr(65 + j)
    
    i = 0
    while(i < iterations):
    
        message = PermutationDecrypt(key, ciphertext)
        score = Score(message)
        
        if score > maxScore:
            maxScore = score
            parentKey = key
            key = SwapRandom(parentKey)
        else 
            key = SwapRandom(parentKey)
        
    return([parentKey, message])
        
def SwapRandom(key)
    
    i = 0 
    j = 0
    while (i == j)
        i = random.randint(0, 26)
        j = random.randint(0, 26)
    
    temp = key[i]
    key[i] = key[j]
    key[j] = temp
    
    return key
    
    
        
    