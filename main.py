import Part1

k = [2, 5, 1, 3]
text = "Hello World!"
print(text)

ciphertext = Part1.BlockEncrypt(k, text)
print(ciphertext)

ass = Part1.PermutationEncrypt('QWERTYUIOPASDFGHJKLZXCVBNM', 'ADASQDBWUQDJQWEOS!!!D')
print(ass)
ass = Part1.PermutationDecrypt('QWERTYUIOPASDFGHJKLZXCVBNM', ass)
print(ass)