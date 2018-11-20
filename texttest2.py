# calculate there are how many 9 between 0 and 100
num = 0
for i in range(101):
    i_str = str(i)
    if '9' in i_str:
        num += 1

print(num)
