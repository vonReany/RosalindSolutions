dataset = open('rosalind_perm.txt').read().split('\n')
num = int(dataset[0])
permCount = 1
numbers = []
for x in range(1, num+1):
 permCount*=x
 numbers.append(str(x))
print(permCount)
def perm(arr, i):
 if num-1 > i:
  for j in range(i, num):
   swap=arr[i]
   arr[i]=arr[j]
   arr[j]=swap
   perm(arr, i+1)
   swap=arr[j]
   arr[j]=arr[i]
   arr[i]=swap
 else:
  print(' '.join(arr))
perm(numbers, 0)
