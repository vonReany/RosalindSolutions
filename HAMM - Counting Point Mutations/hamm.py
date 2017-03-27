dataset = open('rosalind_hamm.txt').read().split('\n')
dnaString1 = dataset[0]
dnaString2 = dataset[1]
length = len(dnaString1)
i = 0
hamming = 0
while i<length:
 if dnaString1[i] != dnaString2[i]: hamming+=1
 i+=1
print(hamming)
