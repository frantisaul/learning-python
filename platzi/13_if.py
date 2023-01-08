# if
if True:
    print('should perform')
    
if False:
    print('won\'t be executed')

pet = input('Cual es tu mascoa favorita? ')
if pet == 'perro':
    print('genial!. Tienes buen gusto')
elif pet == 'gato':
    print('espero tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print('calm down')

stock = input('Digita el stock => ')
stock = int(stock)
if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')