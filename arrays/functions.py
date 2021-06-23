import random

def is_positive_integer(value: int):
    is_integer = False
    if type(value) == int:
        if value > 0:
            is_integer = True
    
    return is_integer

def fill_random(data: list, size: int):
    for i in range(size):
        data.append(random.randint(0, 1000))

def sum_array(input_array: list, size: int):
    total_sum = 0;

    for i in range(size):
        total_sum += input_array[i]
    return total_sum

def avg_array(input_array: list, size: int):
    return sum_array(input_array, size)

def add_arrays(empty_array: list, array1: list, array2: list, size: int):
    for i in range(size):
        empty_array.append(array1[i] + array2[i])

def display_array(input_array: list, size: int):
    print(input_array)