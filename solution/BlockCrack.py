from random import *
import Part1

def Crack(ciphertext, k=None):
    ceiling = 1000
    
    if(k == None):
        return
    else:
        count = 0
        kp = randint(0, pow(10, k)-1)
        prev = Part1.BlockDecrypt(kp, ciphertext)
        kn = randint(0, pow(10, k)-1)
        next = Part1.BlockDecrypt(kn, ciphertext)
        while count<ceiling:
            if(Score(prev)<Score(next)):
                kp = kn
                prev = next
                count = 0
            kn = randint(0, pow(10, k)-1)
            next = Part1.BlockDecrypt(kn, ciphertext)
            count += 1
        
        return [kp, prev]