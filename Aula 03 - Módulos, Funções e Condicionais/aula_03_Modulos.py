import math
num = 17
raiz = math.sqrt(num)
print (f'A raiz do número 4 é {raiz:.2f}.')

graus = 90
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print (seno)

import random
num_random = random.random()
print(num_random)
print (num_random*10) #sortear números entre 0 e 10 mas ele não sorteia o 10
num_random_int = random.randint(1, 10) #dessa forma, o 10 está incluso
print(num_random_int)

