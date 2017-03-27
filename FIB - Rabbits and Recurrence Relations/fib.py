dataset = open('rosalind_fib.txt').read().split('\n')
n = int(dataset[0].split()[0])
k = int(dataset[0].split()[1])
fibo = [1, 1]
i = 1
while i <= n:
 fibo.append(fibo[i]+fibo[i-1]*k)
 i+=1
print(fibo[n-1])
