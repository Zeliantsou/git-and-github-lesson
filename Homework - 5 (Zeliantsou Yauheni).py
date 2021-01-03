import os
login = input("Зарегистрируйте Ваш логин: ")
password = input("Зарегистрируйте Ваш пароль: ")
os.system('cls')
def login_password(function):
    def wrapper():
        global login, password
        log = input ("Введите Ваш логин: ")
        pas = input ("Введите Ваш пароль: ")
        result = function()
        if log == login and pas == password:
            return result
        else:
            return "Вы ввели неверный логин или пароль"
    return wrapper
def function1():
    return "ФИО: Пупкин Валерий Петрович, г. рождения: Набережные Чулны, дата рождения: 20.12.1995г."
def function2():
    return "USD - текущий остаток: 2265.68, BYN - текущий остаток: 568.33"
def function3():
    return "ИП \"Очумелые ручки\" - 100.00 BYN \n ИП \"Сад-огород\" - 38.00 BYN"
def function4():
    return "отделение банка №1 - пр-т Независимости 43 \n отделение банка №2 - Машерова 5"
def function5():
    return "USD: 1% годовых, BYN: 5% годовых"
my_dictinary = {"1": function1, "2": function2, "3": function3, "4": function4, "5": function5,}
prosmotr = "y"
menu = """            Личные данные - 1 (требуется авторизация) \n
            Открытые счета - 2 (требуется авторизация) \n
            Выписка расходов - 3 (требуется авторизация) \n
            Информация о расположении банков - 4 (не требуется авторизация) \n
            Информация о возможных вкладах - 5 (не требуется авторизация)"""
while prosmotr == "y":
    while True:
        os.system('cls')
        print (menu)
        n = input("Введите номер интересуемой информации: ")
        if n == "1" or n == "2" or n == "3" or n == "4" or n == "5":
            break
        else:
            os.system('cls')
            print ("Вы ввели неверный пункт. Введите цифру от 1 до 5 \n \n", menu)
    if n == "1" or n == "2" or n == "3":
        p = login_password(my_dictinary[n])
        res = p()
        print(res)
        prosmotr = input("Введите \"y\", если хотите просмотреть еще информацию: ")
    else:
        res = my_dictinary[n]()
        print(res)
        prosmotr = input("Введите \"y\", если хотите просмотреть еще информацию: ")