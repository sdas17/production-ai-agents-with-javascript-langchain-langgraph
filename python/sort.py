people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
# def Sortfunction(name_value):
#     return name_value['name']

people.sort(key=lambda people :people['name'])
print(people)
