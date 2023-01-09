text = 'Ella sabe python'
print(text[0])
print(text[1])

print('\n')
size = len(text)
print('size => ', size)
print(text[size-1])
print(text[-1])

# slicing
print('\n')
print(text[0:5])
print(text[10:16])
print(text[:10]) # 0:10
print(text[5:-1])

print(text[:]) # from starting point to the finish position

# saltos
print('\n')
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])