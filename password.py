from random import *


def is_valid(number):
    return number.isdigit() and int(number) > 0

def param_password():
    digits = '23456789'
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    maybe = 'il1Lo0O'
    chars = ''
    a = input('Включать ли цифры в параль(да/нет): ')
    if a == 'да':
      chars += digits 
    b = input('Включать ли прописные буквы в параль(да/нет): ')
    if b == 'да':
      chars += uppercase_letters
    c = input('Включать ли строчные буквы в параль(да/нет): ')
    if c == 'да':
      chars += lowercase_letters  
    e = input('Включать ли символы в параль(да/нет): ')
    if e == 'да':
      chars += punctuation
    x = input('Исключать ли неоднозначные символы из параля(да/нет): ')
    if x == 'нет':
      chars += maybe
    return chars

def quantity_password():
    while True:
        quantity_password = input('Количество паролей для генерации: ')
        if is_valid(quantity_password):
            quantity_password = int(quantity_password)
            break
        else:
            print('Нужно ввести число больше нуля!')
    return quantity_password

def long_password():           
    while True:
        long_password = input('Длину одного пароля :')
        if is_valid(long_password):
            long_password = int(long_password)
            break
        else:
            print('Нужно ввести число больше нуля!')
    return long_password

def generate_password():
    x, y, z = quantity_password(), long_password(), param_password()
    for _ in range(x):
        password = ''
        for _ in range(y):
            password += choice(z)
        print(password)
            
generate_password()            

























