def SimpleCrack(ciphertext):
    
    messages = []
    ks = range(0, 26)
    
    #setup an array of decypted messages
    for k in range(0, 26):
        messages.Append(SimpleDecrypt(k, ciphertext))
    
    #now we need to sort these messages
    for i in range(0, 25)
        res = Part_2B(messages[i], messages[i+1])
        if res = 2: #the second message is better
            continue
        else if res = 1: #the first message is better
            messages[i + 1] = messages[i]
            ks[i + 1] = ks[i]
            #replace 2nd with 1st message
    
    return [ks[25], messages[25]]
            