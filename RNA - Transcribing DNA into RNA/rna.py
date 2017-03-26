dataset = open('rosalind_rna.txt').read().split('\n')
dnaString = dataset[0]
print(dnaString.replace("T", "U"))