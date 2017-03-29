dataset = open('rosalind_cons.txt').read().split('\n')
dnaStrings = []

for i in range(0, len(dataset)):
 if len(dataset[i]) < 1: break
 if dataset[i][0] == '>':
  dnaStrings.append('')
 else:
  dnaStrings[len(dnaStrings)-1]+=dataset[i]

counts = [[],[],[],[]]
for i in range(0,4): counts[i]=[0]*len(dnaStrings[0])
letters={'A':0,'C':1,'G':2,'T':3}
for dnaString in dnaStrings:
 for i in range(0, len(dnaString)):
  counts[letters[dnaString[i]]][i]+=1

consensus=''
letters={y:x for x,y in letters.items()}
for i in range(0, len(dnaStrings[1])):
 row=[row[i] for row in counts]
 consensus+=letters[row.index(max(row))]

print(consensus)
letters={'A':0,'C':1,'G':2,'T':3}
for c in ['A', 'C', 'G', 'T']:
 print(c+': ', end="")
 print(*counts[letters[c]])
