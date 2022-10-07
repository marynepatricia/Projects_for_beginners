from random import randint
tentativa = 0

computer_number = randint(0, 10)
print('=-'*25)
print(f'\033[7m Vou pensar em um número. Tente advinhar! \033[m')
print('=-'*25)

while True:
    user_number = input('Qual o seu palpite? ')
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('Por favor, digite um número.')
        continue
    tentativa += 1
    if computer_number == user_number:
        print(f'\033[32m Aê! Você acertou ! Você tentou {tentativa} vezes antes de acertar !\033[m')
        break
    else:
        if user_number > computer_number:
            print('Tente um número menor! ')
        else:
            print('Tente um número maior! ')

print(f'\033[36m Até a próxima! \033[m')
