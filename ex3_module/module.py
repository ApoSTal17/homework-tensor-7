def add(args):
    """Функция суммирования любого количества численных аргументов
    
    args:
        args - численные аргументы в любом количестве в виде списка или кортежа
    returns:
        Численную сумму аргументов args
    """
    return sum(args)


def fibonacci(n):
    '''
    Функция вычисления чисел Фибоначчи
    '''
    """Функция вычисления чисел Фибоначчи
    args:
        n - номер числа Фибоначчи
    returns:
        Число Фибоначчи по номеру n
    """
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def print_dict(dict):
    """Функция печатает словарь в особом оформлении"""
    for key in dict:
        print(key, '->', dict[key], 'kg')
    print()