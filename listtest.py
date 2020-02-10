"""This is test file1 for list.
"""

cars = ['ww', 'subaru', 'honda', 'toyota']
print('last car brand is % s.' % cars[-1].title())

# title() function is to capitalize the first char of string

print(cars[-1].title())

# Use for loop to traverse the list elements.
# Exercise 3-1
for car in cars:
    print(car)

# Exercise 3-3
for car in cars:
    print('I enjoy my car', car+'!')

# delete one element from list
print('the length is: ', cars.__len__())

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

print(people)

people.__delitem__(0)

print(people)

for p in people:
    print(p + ', please enjoy party with us!')

print('Only 2 tickets available!')

while len(people) > 2:
    pend = people.pop()
    print(pend + ', sorry that you cannot join the party.')

print(people)

for pin in people:
    people.remove(pin)
print(people)
"""究其原因，在删掉第一个值，也就是索引[0]后，索引为[1]的值索引变为了[0]，然后第二次删除是从索引[1]开始删除的，所以漏掉了一个值。

如果要用remove函数删空整个List，正确的做法应该是

list = ['Google', 'Runoob', 'Taobao', 'Baidu']
for i in range(len(list)):
    list.remove(list[0])
print(list)
————————————————
"""
"""
import copy
a = rang(30)
b = copy.deepcopy(a)
for i in a:
    if i % 4 != 0:
        b.remove(i)

print(b)
"""
#
# while len(people) > 0:
#     people.pop()

print(people)

print(people.__sizeof__())
print(len(people))


