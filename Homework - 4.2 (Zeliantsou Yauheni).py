import os
name_1 = input("Введите имя первого игрока, который будет играть крестиками (X): ")
name_2 = input("Введите имя второго игрока, который будет играть ноликами (O): ")
want_to_play = "y"
while want_to_play == "y":
    temp = input("Кто первый ходит? (Введите 1, если ходит 1-й игрок или 2, если второй): ")
    cikl = True
    while cikl == True:
        if temp == "1" or temp == "2":
            cikl = False
        else:
            os.system('cls')
            print("Нужно ввести \"1\" или \"2\", чтобы понимать кто ходит и начать игру!")
            temp = input("Укажите, кто первый ходит - ")

                                                #ввод имен и выбор первого хода
    #------------------------------------------------------------------------------------------------------------------------------#

    if temp == "1":
        toggler = True
    if temp == "2":
        toggler = False

    game_field = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

    def print_matrix(pole):
        for i in range(len(pole)):
            for j in range(len(pole[i])):
                print(pole[i][j], end = "  ")
            print()

                                                #прорисовка поля игры, переключаетеди хода
    #------------------------------------------------------------------------------------------------------------------------------#
    os.system('cls')
    pobeda = False
    temp_1 = 0
    stroka_proverki = ""
    stroka_proverki_1 = ""
    stroka_proverki_2 = ""
    stroka_proverki_3 = ""
    nicheika = 0
    while pobeda != True:
        if toggler == True:

            print_matrix(game_field)
            print(name_1, ", Ваш ход! Введите номер любой пронумерованной ячейки")
            temp_1 = input()     

            proverka_hoda = True
            for i in range(len(game_field)):
                    for j in range(len(game_field[i])):
                        if game_field[i][j] == temp_1:
                            proverka_hoda = False

            if proverka_hoda == True:
                os.system('cls')
                print("Вы ввели не существующий номер ячейки. Попробуйте снова!")
            else:
                os.system('cls')
                for l in range(len(game_field)):
                    for k in range(len(game_field[l])):
                        if game_field[l][k] == temp_1:
                            game_field[l][k] = "X"

                                    #выбор, куда ходить. проверка возможности поставить ход в заданную ячейку
    #------------------------------------------------------------------------------------------------------------------------------#

                for a in range(len(game_field)):
                    for b in range(len(game_field[a])):
                        if game_field[a][b] == "X":
                            stroka_proverki = stroka_proverki + "X"
                        if (a == b) and (game_field[a][b] == "X"):
                                stroka_proverki_1 = stroka_proverki_1 + "X"
                        if (a == len(game_field[a]) - b - 1) and (game_field[a][b] == "X"):
                                stroka_proverki_2 = stroka_proverki_2 + "X"
                        if game_field[b][a] == "X":
                            stroka_proverki_3 = stroka_proverki_3 + "X"

                    if (stroka_proverki == "XXX") or (stroka_proverki_3 == "XXX"):
                        print(name_1, ", поздравляем, Вы победили!")
                        print_matrix(game_field)
                        pobeda = True
                        want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                        break


                    else:
                        stroka_proverki = ""
                        stroka_proverki_3 = ""

                if (stroka_proverki_1 == "XXX") or (stroka_proverki_2 == "XXX"):
                    print(name_1, ", поздравляем, Вы победили!")
                    print_matrix(game_field)
                    pobeda = True
                    want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                    break
                else:
                    stroka_proverki_1 = ""
                    stroka_proverki_2 = ""

                                                        #проверка на победу
    #------------------------------------------------------------------------------------------------------------------------------#
                if pobeda == False:
                    for a in range(len(game_field)):
                        for b in range(len(game_field[a])):
                            if game_field[a][b] == "X" or game_field[a][b] == "O":
                                nicheika += 1
                    if nicheika == 9:
                        print("Вы сыграли вничью!")
                        print_matrix(game_field)
                        want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                        break

                    else:
                        nicheika = 0
                        toggler = not toggler

                                                        #проверка на ничью
    #------------------------------------------------------------------------------------------------------------------------------#
                                                    #тоже, только для второго игрока

        if toggler == False:

            print_matrix(game_field)
            print(name_2, ", Ваш ход! Введите номер любой пронумерованной ячейки")
            temp_1 = input()

            proverka_hoda = True
            for i in range(len(game_field)):
                    for j in range(len(game_field[i])):
                        if game_field[i][j] == temp_1:
                            proverka_hoda = False

            if proverka_hoda == True:
                os.system('cls')
                print("Вы ввели не существующий номер ячейки. Попробуйте снова!")
            else:
                os.system('cls')
                for l in range(len(game_field)):
                    for k in range(len(game_field[l])):
                        if game_field[l][k] == temp_1:
                            game_field[l][k] = "O"

                                    #выбор, куда ходить. проверка возможности поставить ход в заданную ячейку
    #------------------------------------------------------------------------------------------------------------------------------#

                for a in range(len(game_field)):
                    for b in range(len(game_field[a])):
                        if game_field[a][b] == "O":
                            stroka_proverki = stroka_proverki + "O"
                        if (a == b) and (game_field[a][b] == "O"):
                                stroka_proverki_1 = stroka_proverki_1 + "O"
                        if (a == len(game_field[a]) - b - 1) and (game_field[a][b] == "O"):
                                stroka_proverki_2 = stroka_proverki_2 + "O"
                        if game_field[b][a] == "O":
                            stroka_proverki_3 = stroka_proverki_3 + "O"

                    if (stroka_proverki == "OOO") or (stroka_proverki_3 == "OOO"):
                        print(name_2, ", поздравляем, Вы победили!")
                        print_matrix(game_field)
                        pobeda = True
                        want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                        break


                    else:
                        stroka_proverki = ""
                        stroka_proverki_3 = ""

                if (stroka_proverki_1 == "OOO") or (stroka_proverki_2 == "OOO"):
                    print(name_2, ", поздравляем, Вы победили!")
                    print_matrix(game_field)
                    pobeda = True
                    want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                    break
                else:
                    stroka_proverki_1 = ""
                    stroka_proverki_2 = ""

                                                        #проверка на победу
    #------------------------------------------------------------------------------------------------------------------------------#
                if pobeda == False:
                    for a in range(len(game_field)):
                        for b in range(len(game_field[a])):
                            if game_field[a][b] == "X" or game_field[a][b] == "O":
                                nicheika += 1
                    if nicheika == 9:
                        print("Вы сыграли вничью!")
                        print_matrix(game_field)
                        want_to_play = input("введите \"y\", если хотите сыграть снова: ")
                        break

                    else:
                        nicheika = 0
                        toggler = not toggler

                                                        #проверка на ничью
    #------------------------------------------------------------------------------------------------------------------------------#