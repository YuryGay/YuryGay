from random import *

def code_discode():
    while True:
        s = input('выбери: 1 для шифрования и 2 для дешифрования ')
        if s == '1' or s == '2':
            return s
            break
        else:
            print('Это не верный ответ')

def language():
    while True:
        lan = input('Какой язык использовать?(ру/en) ')
        if lan == 'ру' or lan == 'en':
            return lan
            break
        else:
            print('Такой язык использовать не получиться!')
        

def shift():
    lan = language()
    while True:
        n = input('Выберите шаг сдвига: ')
        if n.isdigit() and lan == 'ру':
            n = int(n) % 32
            return n, 'ру'
            break
        elif n.isdigit() and lan == 'en':
            n = int(n) % 26
            return int(n), 'en'
            break
        else:
            print('Надо выбрать шаг сдвига!')

def caesar_code():
    ang = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    ang2 = ang.upper()
    rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus2 = rus.upper()
    a = code_discode()
    b, c = shift()
    
    if a == '1':
        if c == 'en':
            text = ''
            for i in input('Введите текст для шифровки: '):
                if i.isalpha() and i.islower():
                    i = ang[ang.find(i) + b]
                    text += i
                elif i.isalpha() and i.isupper():
                    i = ang2[ang2.find(i) + b]
                    text += i
                else:
                    text += i
            return text
        if c == 'ру':
            text = ''
            for i in input('Введите текст для шифровки: '):
                if i.isalpha() and i.islower():
                    i = rus[rus.find(i) + b]
                    text += i
                elif i.isalpha() and i.isupper():
                    i = rus2[rus2.find(i) + b]
                    text += i
                else:
                    text += i
            return text

    elif a == '2':
        if c == 'en':
            text = ''
            for i in input('Введите текст для шифровки: '):
                if i.isalpha() and i.islower():
                    i = ang[ang.find(i) + 26 - b]
                    text += i
                elif i.isalpha() and i.isupper():
                    i = ang2[ang2.find(i) + 26 - b]
                    text += i
                else:
                    text += i
            return text
        if c == 'ру':
            text = ''
            for i in input('Введите текст для шифровки: '):
                if i.isalpha() and i.islower():
                    i = rus[rus.find(i) + 32 - b]
                    text += i
                elif i.isalpha() and i.isupper():
                    i = rus2[rus2.find(i) + 32 - b]
                    text += i
                else:
                    text += i
            return text

print(caesar_code())






