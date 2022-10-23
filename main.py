from math import pow, sqrt, sin, cos, tan


def dan():
    return float(input('Введiть перше число: ')), float(input('Введiть друге число: '))


def one_c():
    return float(input('Введiть число: '))


def my_sum():
    x, y = dan()
    return 'Результат =', x + y


def minus():
    x, y = dan()
    return 'Результат =', x - y


def dil():
    x, y = dan()
    try:
        return 'Результат =', x / y
    except:
        return 'Не можна ділити на 0'


def stu():
    x, y = dan()
    return 'Результат =', pow(x, y)


def qva():
    x = one_c()
    return 'Результат =', sqrt(x)


def cube():
    x = one_c()
    return 'Результат =', x ** (1 / 3)


def sinn():
    x = one_c()
    return 'Результат =', sin(x)


def coss():
    x = one_c()
    return 'Результат =', cos(x)


def tang():
    x = one_c()
    return 'Результат =', tan(x)


def mn():
    x, y = dan()
    return 'Результат =', x * y


def bank(val, month, percent=10):
    """
    Функція розраховує фінальну кількість на рахунку після завершення строку депозиту.
    """
    if month == 1:
        return val * (((percent / 12) + 100) / 100)
    return bank(val * (((percent / 12) + 100) / 100), month - 1, percent)


def action():
    try:
        d = int(input('''
Оберiть дiю (число):
1. Додавання
2. Віднімання
3. Множення
4. Ділення
5. Зведення в ступінь
6. Квадратний корінь
7. Кубічний корінь
8. Знайти синус
9. Знайти косинус
10. Знайти тангенс
11. Порахувати накопичення депозиту
12. Вийти
= '''))
        if d == 1:  # 1. Додавання
            print(*my_sum())
            action()
        elif d == 2:  # 2. Віднімання
            print(*minus())
            action()
        elif d == 3:  # 3. Множення
            print(*mn())
            action()
        elif d == 4:  # 4. Ділення
            print(*dil())
            action()
        elif d == 5:  # 5. Зведення в ступінь
            print(*stu())
            action()
        elif d == 6:  # 6. Квадратний корінь
            print(*qva())
            action()
        elif d == 7:  # 7. Кубічний корінь
            print(*cube())
            action()
        elif d == 8:  # 8. Знайти синус
            print(*sinn())
            action()
        elif d == 9:  # 9. Знайти косинус
            print(*coss())
            action()
        elif d == 10:  # 10. Знайти тангенс
            print(*tang())
            action()
        elif d == 11: # 11. Запустити калькулятор депозиту
            amnt = int(input("Сума депозитного вкладу? \n"))
            term = float(input("Термін депозиту, у місяцях? \n"))
            rate = float(input("Річний відсоток депозиту, у %? \n"))

            print(f'Загальна сума, акумульована на рахунку за весь час депозиту '
                  f'становитиме {round(bank(amnt, term, rate), 2)}')
            action()
        elif d == 12:  # 11. Вийти
            print('Завершення програми')
        else:
            print('Потрiбно обрати дiю (1-12), спробуйте ще раз')
            action()
    except Exception as e:
        print(f'Помилка вводу "{e}", почнiть з початку')
        action()


action()
