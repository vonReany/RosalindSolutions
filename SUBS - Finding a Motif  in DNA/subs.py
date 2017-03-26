dataset = open('rosalind_subs.txt').read().split('\n')
dnaString = dataset[0]
motif = dataset[1]
last = 0
while True:
 last = dnaString.find(motif, last)
 if last == -1: break
 last += 1
 print(last, end=' ')