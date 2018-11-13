# Dict learning & test

alien_0 = {'color': 'green', 'points': 5}
print('The aline\'s color is', alien_0['color'])

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'Michael': 'ruby',
    }
friends = ['phil', 'sarah', 'Mike']

# Exercise 6-6
for friend in friends:
    if friend in favorite_languages.keys():
        print('Appreciations for joining the poll.')
    else:
        print(friend + ', please join the poll.')

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'speed': 'low', 'point': 5, }
    aliens.append(new_alien)

for i in range(3):
    print(aliens[i])
print('...')
print('The total number of the aliens is: ' + str(len(aliens)))


# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("\tHi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
#
# names = []
# names = sorted(favorite_languages.keys())
# print(names)
#
# values = []
# values = favorite_languages.values()
# print(values)




