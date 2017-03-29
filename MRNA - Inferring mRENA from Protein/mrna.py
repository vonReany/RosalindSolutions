codonTable='''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G'''
codonTableSplit=codonTable.split()
codonTableDict={}
for i in range(0, len(codonTableSplit), 2):
 if codonTableSplit[i+1] != 'Stop':
  if codonTableSplit[i+1] in codonTableDict:
   codonTableDict[codonTableSplit[i+1]]+=1
  else:
   codonTableDict[codonTableSplit[i+1]]=1

dataset = open('rosalind_mrna.txt').read().split('\n')
dnaString = dataset[0]
res = 3
for codon in dnaString:
 res*=codonTableDict[codon]
 res=res%1000000
print(res)
