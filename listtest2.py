# Exercise 3-8
tourspots = ['hakeijima', 'hakone', 'tokyotower','fujigoko','agowan','gozaishodake','musashino', 'akihabara']
print("sorted list is:", sorted(tourspots))
print(tourspots)
print('reversed sorted list is:', sorted(tourspots, reverse=True))
print(tourspots)
tourspots.reverse()
print('reversed list is:', tourspots)
tourspots.reverse()
print('returned to original order', tourspots)
tourspots.sort()
print(tourspots)
tourspots.sort(reverse=True)
print(tourspots)

# Exercise 4-3
numbers = list(range(1,21))
print(numbers)

# Exercise 4-4
# numbers = list(range(1,100001))
# for number in numbers:
#     print(number)

# Exercise 4-5
numbers = list(range(1,1000001))
print(max(numbers))
print(sum(numbers))

# Exercise 4-6
numbers = list(range(1,21,2))
for number in numbers:
    print(number)

# Exercise 4-7
numbers = list(range(3,31,3))
for number in numbers:
    print(number)

# Exercise 4-8 & 4-9
numbers = [value **3 for value in range(1,11)]
print(numbers)

# Exercise 4-10
print(numbers[:3])

index1 = int(len(numbers)/2)
print(numbers[index1 - 1], numbers[index1], numbers[index1 + 1])

print(numbers[-3:])

# Exercise 4-13
birds = ('b1', 'b2')
birds = ('b3', 'b4', 'b6')

print(birds)



