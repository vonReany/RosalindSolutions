dataset = open('rosalind_gc.txt').read().split('\n')
dnaStrings = {}
lastID = ''
for line in dataset:
 if line=='': break
 if line[0]=='>':
  lastID=line.split('>')[1]
  dnaStrings[lastID]=''
 elif lastID!='':
  dnaStrings[lastID]+=line
def GCPercent(dnaString):
 return float(dnaString.count('G')+dnaString.count('C'))*100/len(dnaString)
maxGC=[lastID, GCPercent(dnaStrings[lastID])]
for ID in dnaStrings:
 if GCPercent(dnaStrings[ID]) > maxGC[1]:
  maxGC[0]=ID
  maxGC[1]=GCPercent(dnaString[ID])
print(*maxGC, sep="\n")
