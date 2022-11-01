from random import *
def ugaday_ka():

    print('Добро пожаловать в числовую угадайку', 'Будем угадывать от 1 и до скольки?', sep = '\n')
    
    while True:
        kol = input()
        if kol.isdigit() and int(kol) > 0:
            kol = int(kol)
            break
        else:
            print('Надо ввести число больше нуля')
            
    num, coun = randint(1, kol), 0
    

    def is_valid(number):
        return number.isdigit() and int(number) in range(1, kol + 1)

    print('введите целое число от 1 до', kol)

    while True:
        n = input()
        if is_valid(n):
            n = int(n)
            if n > num:
                coun += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n < num:
                coun += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n == num:
                coun += 1
                print('Вы угадали c', coun, 'попытки', 'поздравляем!', '\n', 'Спасибо, что играли в числовую угадайку.')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до', kol)

ugaday_ka()

while True:
    print('Хотите сиграть ещё: да или нет')
    answer = input()
    if answer.lower() == 'да':
        ugaday_ka()
    else:
        print('Жаль. До новых встреч!!!')
        break
