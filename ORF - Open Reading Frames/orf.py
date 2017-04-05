codonTable={'CAC': 'H', 'TCT': 'S', 'TGA': 'Stop', 'GGA': 'G', 'GAT': 'D', 'TGC': 'C', 'AGC': 'S', 'TGG': 'W', 'GTT': 'V', 'CCG': 'P', 'ATG': 'M', 'AGA': 'R', 'GAA': 'E', 'CTG': 'L', 'CCT': 'P', 'TAG': 'Stop', 'CCA': 'P', 'GCT': 'A', 'GCA': 'A', 'ACA': 'T', 'AGG': 'R', 'AAA': 'K', 'AAG': 'K', 'AAC': 'N', 'CGT': 'R', 'TAC': 'Y', 'GTC': 'V', 'CGC': 'R', 'GTG': 'V', 'TCA': 'S', 'GCC': 'A', 'CAA': 'Q', 'TCC': 'S', 'CTT': 'L', 'CAT': 'H', 'CGA': 'R', 'GCG': 'A', 'AGT': 'S', 'TTA': 'L', 'ACG': 'T', 'GGG': 'G', 'TTC': 'F', 'TAA': 'Stop', 'ATA': 'I', 'GTA': 'V', 'ACC': 'T', 'CTC': 'L', 'CTA': 'L', 'CGG': 'R', 'CCC': 'P', 'ACT': 'T', 'ATC': 'I', 'TCG': 'S', 'GAC': 'D', 'GGT': 'G', 'GGC': 'G', 'AAT': 'N', 'TAT': 'Y', 'CAG': 'Q', 'GAG': 'E', 'TTG': 'L', 'ATT': 'I', 'TGT': 'C', 'TTT': 'F'}
complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

dataset = open('rosalind_orf.txt').read().split('\n')
data = ''.join(dataset[1:len(dataset)-1])
dataR = ''.join([complements[c] for c in data[::-1]])
dnaStrings = []
indices = []

def find_orf(protString):
 global dnaStrings, indices
 l = len(protString)
 for i in range(l-2):
  if codonTable[protString[i:i+3]]=='M':
   for j in range(i+3, l-2, 3):
    if codonTable[protString[j:j+3]]=='Stop':
     dnaString=''.join([codonTable[protString[x:x+3]] for x in range(i,j,3)])
     if dnaString in dnaStrings:
      break
     indices.append(i)
     dnaStrings.append(dnaString)
     break

find_orf(dataR)
find_orf(data)
print('\n'.join(dnaStrings))
