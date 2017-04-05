dataset = open('rosalind_lcsm.txt').read().split('\n')
indices = []
for i in range(0, len(dataset)-1):
 if dataset[i][0] == '>':
  indices.append(i)
indices.append(len(dataset))
dnaStrings=[]
for i in range(1, len(indices)):
 dnaStrings.append(''.join(dataset[indices[i-1]+1:indices[i]]))
lcs=''
for length in range(1,len(dnaStrings[0])+1):
 anyFound=len(lcs)
 for i in range(0,len(dnaStrings[0])-length+1):
  foundAll=True
  for dnaString in dnaStrings:
   if dnaString.find(dnaStrings[0][i:i+length]) == -1:
    foundAll=False
    break
  if foundAll:
   lcs=dnaStrings[0][i:i+length]
 if len(lcs)==anyFound:
  break
print(lcs)
