"""
    "Болтовня ничего не стоит. Покажите мне код" (с) Linus Torvalds

Декораторы. Интерактивный конспект Python.

на осннове лекций :
Олега Молчанова   - https://www.youtube.com/watch?v=Ss1M32pp5Ew
Ивана Викторовича - https://www.youtube.com/watch?v=3WbglY2b65g&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=20
Сергея Балакирева - https://www.youtube.com/watch?v=v0qZPplzwUQ

Приведен код из видео, а так же решены задачи темы 7.11 "Декораторы функций" курса "Добрый, добрый Python"
Сергея Балакирева.
https://stepik.org/lesson/567062/step/1?unit=561336

N.B. Нижеприведенные функции решений задач написаны в процессе и для обучения,
лично автором конспекта. Они проходят испытания на 22.10.2022, при
этом могут быть не оптимальными(идеальными) с точки зрения логики алгоритмов.
"""

from datetime import datetime


def timeit(*args):                         # принимает агрумент декоратора
    """
    Функция - декоратор, измеряющая время работы декорируемой функции.
    В приведенном примере сравнивает скорость формирования списка (type 'list')
    циклом for и генератором, формирование происходит в функциях  one, two.

    Код из видео Олега Молчанова
    https://www.youtube.com/watch?v=Ss1M32pp5Ew

    Дополнительные тезисы:
    - функция должна содержать только целевой код;
    - dry, don't repeat yourself;
    - функции - объекты первого класса;
    """
    print(args)

    def outer(func):                        # принимает функцию
        def wrapper(*args, **kwargs):
            start = datetime.now()          # timestamp начала работы
            result = func(*args, **kwargs)  # выполняет переданную в декоратор функцию
            print(datetime.now() - start)   # завершение работы - timestamp начала
            return result                   # возврат результата работы переданной в декоратор ф-ции
        return wrapper                      # возврат wrapper
    return outer                            # возврат outer

# @timeit('name')                      # вызов осуществляется без
def one(n):
    # start = datetime.now()           # timestamp начала работы
    l = []                             # объявляем список
    for i in range(n):                 # формирование списка циклом
        if i % 2 == 0:                 # проверка на положительное число
            l.append(i)                # добавление в список
    # print(datetime.now() - start)    # завершение работы - timestamp начала
    return l


#@timeit('name')                # "синтаксический сахар" с аргументом, выводит ('name',) в консоль, !снять комментарий!
def two(n):
    # start = datetime.now()                 # timestamp начала работы
    l = [x for x in range(n) if x % 2 == 0]  # формирование списка генератором
    # print(datetime.now() - start )         # завершение работы - timestamp начала
    return l


help(timeit)
# l1 = timeit('name')(one)(10**4)   # => wrapper(10) => one(10) # вызов декоратора без @timeit
# l2 = two(10**4)                   # вызов декоратора с @timeit
# print(l1)
# print(l2)

# l2_2 = two                        # обращение к функции two как к объекту
# print(type(l2_2), l2_2.__name__)  # вывод <class 'function'> wrapper, содержание, тип, имя


def my_decor(func):
    """
    Пример вывода текста в последовательности. В видео был и пример с измерением времени функции,
    идентичный с предыдущим.

    Код из видео Ивана Викторовича
    https://www.youtube.com/watch?v=3WbglY2b65g&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=20

    Дополнительные тезисы:
    - декоратор это функция, позволяющая обернуть другую функцию для расширения ее функциональности без
    непосредственного изменения кода оборачиваемой функции;
    - функция в Python это объект, мы можем проводить с функцией любые манипуляции как с объектом;
    - часто применяется дл разграничения прав пользователей в backend - Flask, Django
    - позволяет упростить код для повторяющихся действий
    - скрыть выполнение определенных функций
    """
    def wrapper(n):         # получаем арумент для основной функции
        print('start')      # перед выполнением
        func(n)             # выполнение основной ф-ции
        print('stop')       # после выполнения
    return wrapper          # возврат значения wrapper

@my_decor
def my_func(number):              # основная функция для передачи в декоратор
    print(number**2)              # возведение в квадрат


help(my_decor)
# my = my_decor(my_func); my(10)  # вариант вывода без указания декоратора над функцией
# my_func(10)                     # вариант вывода с указанием декоратора над функцией


def func_decorator(func):
    """
    Пример, иллюстрирующий порядок выполнения декоратора и декорируемой функции,
    с передачей в функцию строки, тега, выводом строки внутри тегов.

    Код из видео Сергея Балакирева
    https://www.youtube.com/watch?v=v0qZPplzwUQ

    https://stepik.org/lesson/567062/step/1
    """

    def wraper(*args, **kwargs):          # выполняет блок команд до и после оборачиваемой функции
        print("---  some actions ---")    # вывод до выполнения оборачиваемой функции
        result = func(*args, **kwargs)    # выполнение оборачиваемой функции
        print("---  some actions ---")    # вывод после выполнения оборачиваемой функции
        return result                     # возврат переменной result
    return wraper                         # возврат результата функции wrapper


def some_func(title, tag):                    # оборачиваемая функция
    print(f"title = {title}, tag = {tag}")    # вывод аргументов оборачиваемой функции
    return f"<{tag}>{title}</{tag}>"          # возврат оборачиваемой функции


help(func_decorator)
# f = func_decorator(some_func)  # присвоение объекта функции переменной f и передача функции в декоратор
# tagged = f("python", "h1")     # вызов оборачиваемой фунции с аргументами и декоратором, присвоение результата tagged
# print(tagged)                  # вывод содержания tagged

import time


def test_time(func):
    """
    Имплементация подсчета времени выполнения функции от Сергея Балакирева, сравнение
    нахождения общего делителя по быстрому и медленному алгоритмам Евклида.

    Код из видео Сергея Балакирева
    https://www.youtube.com/watch?v=v0qZPplzwUQ

    https://stepik.org/lesson/567062/step/1
    """
    def wraper(*args, **kwargs):       # выполняет блок команд до и после оборачиваемой функции
        st = time.time()               # timestamp начала работы
        result = func(*args, **kwargs) # выполнение оборачиваемой функции
        et = time.time()               # timestamp завершения работы
        dt = et - st                   # timestamp начала - timestamp завершения
        print(f"time: {dt} sek")       # вывод разницы во времени
        return result                  # возврат результата функции wrapper

    return wraper


@test_time
def get_nod_fast(a, b):              # быстрый алгорим Евклида по нахождению НОД
    while b > 0: a, b = b, a % b     # пока b больше ноля - a равно b, b равно отстатку от деления a на b
    return a                         # вернуть a


@test_time
def get_nod_slow(a, b):             # медленный алгорим Евклида по нахождению НОД
    while a != b:                   # пока b не равно a
        if a > b:                   # если a больше b
            a -= b                  # a равно a минус b
        else:                       # иначе
            b -= a                  # b равно b минус a
    return a                        # вернуть a


help(test_time)
# get_nod_slow = test_time(get_nod_slow)(2, 1000000) # вариант запуска без указания декоратора над функцией
# get_nod_fast = test_time(get_nod_fast)(2, 1000000) # вариант запуска без указания декоратора над функцией
# res1 = get_nod_slow(2, 1000000) # вариант запуска с указанием декоратора над функцией
# res2 = get_nod_fast(2, 1000000) # вариант запуска с указанием декоратора над функцией
# print(res1, res2)               # вывод НОД для запуска с указанием декоратора над функцией


def func_show(func):                    # объявляем функцию декоратор
    """
    Декоратор вывода значений функции подсчета площади прямоугольника.

    https://stepik.org/lesson/567062/step/2

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/stepik.org/decorators.py

    """
    def wrapper(*args, **kwargs):                    # функция, которая выполняет блок команд
        result = func(*args, **kwargs)               # запускаем оборачиваемую функцию
        print(f'Площадь прямоугольника: {result}')   # выводим результат согласно задания
    return wrapper                                   # возвращаем результат блока команд, по сути  - запускаем


@func_show                             # N.B. применять декоратор функции так же не нужно, т.е. каммент.
def get_sq(width, height):             # объявляем функцию вычисления площади
    return(width*height)               # возвращаем вычисление площади



help(func_show)
get_sq(5, 7)                           # запуск функции с тестовыми аргументами