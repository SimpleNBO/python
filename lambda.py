people = [
    {'name': 'Harry', 'house': 'Gryffindor'},
    {'name': 'Cho', 'house': 'Ravenclaw'},
    {'name': 'Draco', 'house': 'Slytherin'}
]

people.sort(key=lambda _: _['name'])

print(people)