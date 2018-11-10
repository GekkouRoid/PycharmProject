# Exercise 5-3 ~ 5-7
alien_color = 'green'

if alien_color == 'red':
    print('You killed a red alien, got 5 points.')
elif alien_color == 'green':
    print('You killed a green alien, got 10 points.')
elif alien_color == 'yellow':
    print('You killed a yellow alien, got 20 points')
elif alien_color == 'brown':
    print('You killed a brown alien, got 50 points')

fruits = ['apple', 'banana', 'melon', 'coconut', 'berry', 'cherry', 'orange']
f1 = 'cherry2'
f2 = 'orange'
# for fruit in fruits:
#     if f1 == fruit or f2 == fruit:
#         print('You really like %s!' % fruit)

if f1 in fruits:
    print('You really like %s!' % f1)

if f2 in fruits:
    print('You really like %s!' % f2)

# Exercise 5-10
current_users = ('John', 'admin', 'Hello', 'user1', 'Terry', 'Michael', 'Mike')
new_users = ['john', 'admin', 'mike', 'Teddy']

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print('user ' + new_user + ' exists!')

numbers = list(range(1, 11))
for number in numbers:
    if number == 1:
        print('It is 1st.')
    elif number == 2:
        print('It is 2nd.')
    elif number == 3:
        print('It is 3rd.')
    else:
        print('It is ' + str(number) + 'th.')
