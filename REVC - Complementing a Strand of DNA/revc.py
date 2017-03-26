dataset = open('rosalind_revc.txt').read().split('\n')
dnaString = dataset[0]
complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for c in dnaString[::-1]:
 print(complements[c], end="")