codonTable={'CAC': 'H', 'TCT': 'S', 'TGA': 'Stop', 'GGA': 'G', 'GAT': 'D', 'TGC': 'C', 'AGC': 'S', 'TGG': 'W', 'GTT': 'V', 'CCG': 'P', 'ATG': 'M', 'AGA': 'R', 'GAA': 'E', 'CTG': 'L', 'CCT': 'P', 'TAG': 'Stop', 'CCA': 'P', 'GCT': 'A', 'GCA': 'A', 'ACA': 'T', 'AGG': 'R', 'AAA': 'K', 'AAG': 'K', 'AAC': 'N', 'CGT': 'R', 'TAC': 'Y', 'GTC': 'V', 'CGC': 'R', 'GTG': 'V', 'TCA': 'S', 'GCC': 'A', 'CAA': 'Q', 'TCC': 'S', 'CTT': 'L', 'CAT': 'H', 'CGA': 'R', 'GCG': 'A', 'AGT': 'S', 'TTA': 'L', 'ACG': 'T', 'GGG': 'G', 'TTC': 'F', 'TAA': 'Stop', 'ATA': 'I', 'GTA': 'V', 'ACC': 'T', 'CTC': 'L', 'CTA': 'L', 'CGG': 'R', 'CCC': 'P', 'ACT': 'T', 'ATC': 'I', 'TCG': 'S', 'GAC': 'D', 'GGT': 'G', 'GGC': 'G', 'AAT': 'N', 'TAT': 'Y', 'CAG': 'Q', 'GAG': 'E', 'TTG': 'L', 'ATT': 'I', 'TGT': 'C', 'TTT': 'F'}

dataset = open('rosalind_splc.txt').read().split('\n')
indices = []
for i in range(1, len(dataset)-1):
 if dataset[i][0] == '>':
  indices.append(i)
indices.append(len(dataset))

rnaString=''.join(dataset[1:indices[0]])
introns=[]
for i in range(1, len(indices)):
 introns.append(''.join(dataset[indices[i-1]+1:indices[i]]))

for intron in introns:
 rnaString=rnaString.replace(intron, '')
print(''.join([codonTable[rnaString[i:i+3]] for i in range(0,len(rnaString)-3,3)]))
