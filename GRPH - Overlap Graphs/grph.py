dataset = open('rosalind_grph.txt').read().split('\n')
indices = []
names=[]
for i in range(0, len(dataset)-1):
 if dataset[i][0] == '>':
  indices.append(i)
  names.append(dataset[i][1:])
indices.append(len(dataset))
dnaStrings=[]
for i in range(1, len(indices)):
 dnaStrings.append(''.join(dataset[indices[i-1]+1:indices[i]]))
adj=[]
for i in range(0, len(dnaStrings)):
 for j in range(0, len(dnaStrings)):
  if i==j: continue
  if dnaStrings[i][:3]==dnaStrings[j][-3:]:
   adj.append(names[j]+' '+names[i])
for a in adj: print(a)
