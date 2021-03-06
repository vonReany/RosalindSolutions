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
 codonTableDict[codonTableSplit[i]] = codonTableSplit[i+1]

dataset = open('rosalind_prot.txt').read().split('\n')
dnaString = dataset[0]
i=0
while True:
 if i>len(dnaString):
  print('There is no stop codon.')
  break 
 elif codonTableDict[dnaString[i:i+3]] == 'Stop': break
 print(codonTableDict[dnaString[i:i+3]], end="")
 i+=3