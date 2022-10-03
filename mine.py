
secret_dogs = ['Asya','Varya','Lily','Lapka','Bristol','Lelik','Chernika']
secret_dogs = sorted(secret_dogs)
# print('sorted(secret_dogs)',sorted(secret_dogs) )
guess_dogs = []
count_guess_dog = 0

# a = {
#     "try_max": 0,
#     "try_max1": 0,
#     "try_max2": 0,
# }

# def find_dog(guess):
    # return guess in guess_dogs

# Count try
try_count = 0
try_max = 1



while True:
    guess = input('Пожалуйста угадайте имя собаки: ')
    # print("guess in secret_dog", guess in secret_dogs)
    if guess in secret_dogs:  # in операция есть ли значение в массиве
        #    print("guess in guess_dogs", guess in guess_dogs) / for debug in terminal
        if guess in guess_dogs:
            print(f'Не пойдет, {guess} уже есть!')
        else:
            # if guess not in guess_dogs:
            guess_dogs.append(guess)  # Добавить элемент в массив
            guess_dogs = sorted(guess_dogs)
            if secret_dogs == guess_dogs:
                print(
                    f"Вы угадали всех собак! Вот они слева направо: {', '.join(guess_dogs)} ")
                break
            count_guess_dog += 1
            print(f'Вы угадали! {count_guess_dog} из 7' )
        # print("guess_dogs", guess_dogs)
    else:
        if try_count < try_max:
            print('Попытайся еще, у тебя еще одна попытка!')
            try_count += 1
            continue
        else:
            print('Фууу... \nХотите попробовать еще ? \nY (Начать заново) / N (Закончить игру) ' )
            decision = input()
            if decision == 'Y':
                guess_dogs = []
                count_guess_dog = 0
                try_count = 0
                try_max = 1
            elif decision == 'N':
                break



            
    
    """
    Если человек ввел не: то звершить программу
    Если человек ввел да то обнулить все значения и запустить новую итерацию цикла
    """

#+ Дать возможность ошибиться 1 раз, после чего игра все равно продолжится
# Дать возможность вводить разные вариации имени собаки которые будут считаться верными (н-р: Варечка Асечка)
#+ После проигрыша не заканчивать программу, а дать возможность начать заново и сбросить прогресс.
#+ Когда человек угадывает собаку, показывать счетчик, например - угадано 3 из 7 собак
