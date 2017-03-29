dataset = open('rosalind_fibd.txt').read().split('\n')
n = int(dataset[0].split()[0])
m = int(dataset[0].split()[1])
adultRabbits=[0, 0]
youngRabbits=[0, 1]
i = 2
while i <= n:
 youngRabbits.append(adultRabbits[i-1])
 adultRabbits.append(adultRabbits[i-1]+youngRabbits[i-1])
 if i > m:
  adultRabbits[i]-=youngRabbits[i-m]
 i+=1
print(adultRabbits[n]+youngRabbits[n])
