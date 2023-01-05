name = 'Franti'
last_name = 'Huaman Mera'
print(name)
print(last_name)

# concatenate
full_name = name + ' ' + last_name
print(full_name)

quote = 'I\'m Franti' # or "I'm Franti"
print((quote))

quote2 = 'She said "Hello"' # or "She said \"Hello\""
print(quote2)

# format
template = "Hola, mi nombre es " + name +  " y mi apellido es " + last_name
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2 ',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3 ', template)

# challenge
years = 20
template = f"Hola, mi nombre es {name} {last_name} y mi edad es {years}"
print('v4 ', template)