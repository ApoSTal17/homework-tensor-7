import numpy
from random import randint

arr = numpy.array([[randint(1, 100) for line1 in range(3)],
                [randint(1, 100) for line2 in range(3)],
                [randint(1, 100) for line3 in range(3)]])
print('Результат создания массива 3x3 со случайными значениями: ')
print(arr)
arr_trans = arr.transpose()
print('Результат транспонирования этого массива: ')
print(arr_trans)