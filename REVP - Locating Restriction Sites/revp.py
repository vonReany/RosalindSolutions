dataset = open('rosalind_revp.txt').read().split('\n')
dnaString = ''.join(dataset[1:len(dataset)])
complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def checkReversePalindrome(string):
 for i in range(0, int(len(string)/2)):
  if complements[string[i]]!=string[len(string)-1-i]:
   return False
 return True

for i in range(0, len(dnaString)-3):
 for ln in range(12, 2, -2):
  if i+ln>len(dnaString): continue
  if checkReversePalindrome(dnaString[i:i+ln]):
   print(str(i+1)+' '+str(ln))

