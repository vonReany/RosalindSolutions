dataset = open('rosalind_dna.txt').read().split('\n')
dnaString = dataset[0]
for s in ['A', 'C', 'G', 'T']:
 print(dnaString.count(s), end=" ")