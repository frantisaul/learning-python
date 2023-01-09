numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

print('\n')
tasks = ['make a dishes', 'play videogames']
print(tasks)

print('\n')
types = [1, True, 'hola']
print(types)

print('\n')
print(numbers[0])
print(tasks[0])

text = 'Hola'
# text[0] = 'M' # error. Strings ares inmutable.

print('\n')
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(tasks[:3])
print(True in types)
print('hola' in types)