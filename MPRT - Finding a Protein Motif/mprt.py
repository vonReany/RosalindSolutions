import urllib.request

dataset = open('rosalind_mprt.txt').read().split('\n')
for prot in dataset:
 if prot=='': break
 requestBody = urllib.request.urlopen('http://www.uniprot.org/uniprot/'+prot+'.fasta').read()
 requestSplit = str(requestBody).split('\\n')
 protStr = ''.join(requestSplit[1:len(requestSplit)-1])
 motifCount = 0
 motifIndices = []
 for i in range(0, len(protStr)-3):
  if (protStr[i]=='N') &  (protStr[i+1]!='P') & ((protStr[i+2]=='S') | (protStr[i+2]=='T')) & (protStr[i+3]!='P'):
   motifIndices.append(i+1)
   motifCount+=1
 if motifCount==0: continue
 print(prot)
 print(*motifIndices, sep=" ")
