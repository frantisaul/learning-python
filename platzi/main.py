user_option = input('Piedra, papel o tijera => ')
user_option = user_option.lower()
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra ganar a tijera')
        print('user ganó!')
    else:
        print('Papel gana a piedra')
        print('computer ganó!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel ganar a tijera')
        print('user ganó!')
    else:
        print('Tijera gana a papel')
        print('computer ganó!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera ganar a papel')
        print('user ganó!')
    else:
        print('piedra gana a tijera')
        print('computer ganó!')