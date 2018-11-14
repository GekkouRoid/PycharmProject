# Exercise 6-9
place1 = 'Akihabara'
place2 = 'Yokohama'
place3 = 'Hakone'
place4 = 'Agowann'
place5 = 'Asakusa'
places = [place1, place2, place3, place4, place5]
new_place = 'MusashiKosugi'

print(places)
people = {
    'Michael': [place1, place3, place4],
    'Neil': [place4, place1, place2],
    'John': [place3, place2, place5],
}

for p in people:
    print(p + ':')
    if p == 'Michael':
        people[p].append(new_place)
    for place in people[p]:
        print('\t' + place)
