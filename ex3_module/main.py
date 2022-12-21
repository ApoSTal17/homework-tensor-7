from module import add, fibonacci, print_dict

print(f'Результат сложения чисел 1..13: {add(range(13))}')
print(f'17-е число Фибоначчи: {fibonacci(17)}')

abc_dict = {
    'A': 2.8,
    'B': 3.5,
    'C': 1.2,
}
print(f'Красивый вывод словарика:')
print_dict(abc_dict)