import random

x = random.randrange(100)
print(x)

seq = [1, 3, 5, 6, 7, 7, 9, 4]

x = random.choice(seq)
print(x)

seq2 = random.sample(seq, 4)
print(seq)
print(seq2)

x = int(random.gauss(0, 5) + 5)
print(x)
hit = False
hitnum = 7
if hitnum >= x:
    hit = True

if hit:
    print('You are hit.')
else:
    print('Lucky!')

