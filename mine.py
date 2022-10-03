
secret_dogs = ['Варя','Ася','Бристоль','Лапка','Лилу','Черника','Леля']
secret_dogs = sorted(secret_dogs)
# print('sorted(secret_dogs)',sorted(secret_dogs) )
guess_dogs = []



while True:
    guess = input('Пожалуйста угадайте имя собаки: ')
    # print("guess in secret_dog", guess in secret_dogs)
    if guess in secret_dogs:    #in операция есть ли значение в массиве
    #    print("guess in guess_dogs", guess in guess_dogs) / for debug in terminal
        if guess in guess_dogs:
            print (f'Не пойдет, {guess} уже есть!')
        else:
        # if guess not in guess_dogs:
            guess_dogs.append(guess) #Добавить элемент в массив
            guess_dogs = sorted(guess_dogs)
            if secret_dogs == guess_dogs:
                print (f"Вы угадали всех собак! Вот они слева направо: {', '.join(guess_dogs)} " )
                break
            print ('Вы угадали!')     
    #   print("guess_dogs", guess_dogs)
    else:
        print ('Фууу...')
        break



# Дать возможность ошибиться 1 раз, после чего игра все равно продолжится
# Дать возможность вводить разные вариации имени собаки которые будут считаться верными (н-р: Варечка Асечка)
# После проигрыша не заканчивать программу, а дать возможность начать заново и сбросить прогресс.
# Когда человек угадывает собаку, показывать счетчик, например - угадано 3 из 7 собак


 