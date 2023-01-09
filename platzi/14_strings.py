
print('*' * 10)
print('Search texts into strings')
text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
    print('elegiste bien!.')
else:
    print('También elegiste bien')

print('\n')
size = len(text)
print('size: ',size)

print('\n')
print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python','Go'))

print('\n')
text_2 = 'este es un título'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
