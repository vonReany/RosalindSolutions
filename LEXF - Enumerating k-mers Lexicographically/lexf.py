dataset = open('rosalind_lexf.txt').read().split('\n')
alph = dataset[0].split()
alph.sort()
length = int(dataset[1])
def enumerate(prefix):
 if len(prefix)==length: 
  print(prefix)
 else:
  for a in alph:
   enumerate(prefix+a)
enumerate('')
