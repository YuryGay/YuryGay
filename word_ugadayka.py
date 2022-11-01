from random import *

word_list = ['телефон', 'слон', 'колокол', 'газета', 'крот']

def get_word():
    return choice(word_list)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def is_valid_alpha():  # проверка валидности введенной буквы
    print('Введите букву или слово:')
    n = input()
    while True:
        if n.isalpha() == True and n not in guessed_letters and len(n) == 1:
            guessed_letters.append(n)
            print('Названы:', *guessed_words, *guessed_letters, sep=' ')
            return n
        elif n.isalpha() == True and n not in guessed_words and len(n) > 1:
            guessed_words.append(n)
            print('Названы:', *guessed_words, *guessed_letters, sep=' ')
            return n
        elif n in guessed_letters or guessed_words:
            print(f'Вы уже вводили:', n)
            n = input()
        else:
            print(f'Введите букву или слово!')
            n = input()
            continue


def play(word):
    global tries
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    print(word_completion)
    #print(word)  #закомментить овтет

    while word_completion != word or tries > 0:
        guess = is_valid_alpha()
        if len(guess) > 1 and guess == word:
            print(f'Поздравляем, вы угадали слово! Вы победили!', word)
            break
        elif len(guess) > 1 and guess != word:
            tries -= 1
            print(f'Это не слово "{guess}"!')
            print(f'Нет такой буквы, осталось {tries} попыток:')
            print(display_hangman(tries))
            print(word_completion)
        elif len(guess) == 1 and guess in word:
            print('Есть такая буква, попыток осталось:', tries)
            for i in range(len(word)):
                if guess == word[i]:
                    word_completion = word_completion[:i] + guess + word_completion[i+1:]
            print(word_completion,tries)
        elif guess not in word and tries != 0:
            tries -= 1
            print(f'Нет такой буквы, осталось {tries} попыток:')
            print(display_hangman(tries))
        elif tries == 0:
            print(f'Вы проиграли. Загаданное слово: {word}')
            print(word)
            print(display_hangman(tries))


q = 'y'
guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов
tries = 6  # количество попыток

while q == 'y':
    play(get_word())
    print('Желаете сыграть еще? Y = да')
    q = input().lower()
else:
    print('Игра закончена')
