"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10


print(simple_separator())


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return "*" * count


print(long_separator(3))
print(long_separator(4))


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return str(simbol) * count


print(separator('=', 25))
print(separator('&', 55))


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """
    print('=' * 30 + '\n\n' + 'Привет мир!' + '\n\n' + '+' * 30)

'''
**********
Hello World!
##########
'''
hello_world()


def hello_who(who='мир!'):
    """
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print('$' * 15 + '\n\n' + f'Привет {who}!' + '\n\n' + '@' * 9)


'''
**********
Hello World!
##########
'''
hello_who()
'''
**********
Hello Max!
##########
'''
hello_who('Максим!')
'''
**********
Hello Kate!
##########
'''
hello_who('Катюша!')


def pow_many(exponent, *numbers):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    return sum(numbers) ** exponent

print()
print()
print(pow_many(6, 3, 6) ) #  (3 + 6)**6 == 531441
print(pow_many(8, 3, 3) )  # (3 + 3)**8 == 1679616
print(pow_many(9, 4, 6) )  #  (4 + 6)**9 == 1000000000
print(pow_many(3, 2, 1, 4, 5, 6) )  #  (2+ 1+4+5+6)**3 == 5832
print(pow_many(12, 5, 9, 26, ) )  # (5+ 9+ 26)**12 == 10**2 == 16777216000000000000
print()

def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, val in kwargs.items():
        print(f'{key} -----> {val}')


"""
name --> Max
age --> 21
"""
print_key_val(Имя ='Чингачгук', кто_такой = 'Большой змей')
"""
animal --> Cat
is_animal --> True
"""
print_key_val(Животное ='Ягуар', это_зверь = "Да")
print()

def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    # С функцией filter
    # return list(filter(function, iterable))
    #  Циклом
    result = []
    for i in iterable:
        if function (i):
            result.append(i)
    return result


print(my_filter([256, 23, 853, 24, 15], lambda x: x >= 23) ) # == [256, 23, 853, 24]
print(my_filter([600, 2, 33467, 2, 548, 2], lambda x: x == 2) )  # == [2, 2, 2]
print(my_filter([1037, 102, 38, 465, 15], lambda x: x != 38) )  # == [1037, 102, 465, 15]
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abracadabra') )  # == ['a', 'b', 'c', 'd']