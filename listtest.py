"""This is test file for list.
"""

cars = ['ww', 'subaru','honda','toyota']
print('last car brand is % s.' % cars[-1])

# title() function is to capitalize the first char of string

print(cars[-1].title())

# Use for loop to traverse the list elements.
# Exercise 3-1
for car in cars:
    print(car)

# Exercise 3-3
for car in cars:
    print('I enjoy my car',car+'!')

# delete one element from list
del cars[-1]
print(cars)

cars.pop(2)
print(cars)

# Exercise 3-4 ~ 3-7
people = ['p1', 'p2', 'p3', 'p4']
for p in people:
    print(p + ', Please have a party with us!')

print('p2 is unavailable.')

people[1]='p2m'
for p in people:
    print(p + ', Please have a party with us!')

print('We will have bigger party!')

people.insert(0,'p1new')
people.insert(3, 'p3new')
people.append('plast')

for p in people:
    print(p + ', please enjoy party with us!')

# print('Only 2 tickets available!')
#
# while len(people) > 2:
#     pend = people.pop()
#     print(pend + ', sorry that you cannot join the party.')

print(people)

# for p in people:
#     people.remove(p)

while len(people) >0 :
    people.pop()
#
print(people)
#
# print(people.__sizeof__())

