dataset = open('rosalind_iprb.txt').read().split('\n')
k=int(dataset[0].split()[0])
m=int(dataset[0].split()[1])
n=int(dataset[0].split()[2])
o=k+m+n
MM=m*(m-1)/2
NN=n*(n-1)*2
MN=n*m*2
TOT=o*(o-1)*2
print((TOT-(MM+NN+MN))/TOT)
