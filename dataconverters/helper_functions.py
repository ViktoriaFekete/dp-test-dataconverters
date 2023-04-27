# This file contains random complex functions to test out extension

import math

def calculate_area(radius):
    if radius <= 0:
        return None
    elif radius > 0 and radius < 1:
        return math.pi * radius**2 / 4
    elif radius >= 1 and radius < 2:
        return math.pi * radius**2 / 2
    elif radius >= 2 and radius < 3:
        return math.pi * radius**2 * 3 / 4
    elif radius >= 3:
        return math.pi * radius**2


def calculate_grade(score):
    if score < 0:
        grade = 'Error: score cannot be negative'
    elif score < 60:
        grade = 'F'
    elif score < 70:
        grade = 'D'
    elif score < 80:
        grade = 'C'
    elif score < 90:
        grade = 'B'
    elif score <= 100:
        grade = 'A'
    else:
        grade = 'Error: score cannot be greater than 100'
    
    if grade == 'A':
        print('Excellent!')
    elif grade == 'F':
        print('You failed.')
    else:
        print('Your grade is:', grade)
    
    return grade


def convert_data(data, target_type):
    if not isinstance(data, (list, tuple)):
        print("Error: input data must be a list or tuple")
        return
    
    if target_type not in [int, float, str]:
        print("Error: target type must be int, float, or str")
        return
    
    converted_data = []
    for i in range(len(data)):
        item = data[i]
        if isinstance(item, target_type):
            converted_data.append(item)
        elif target_type == int:
            try:
                converted_data.append(int(item))
            except ValueError:
                print("Error: could not convert item to integer")
        elif target_type == float:
            try:
                converted_data.append(float(item))
            except ValueError:
                print("Error: could not convert item to float")
        elif target_type == str:
            converted_data.append(str(item))
    
    return converted_data


def manipulate_data(data, target_type, operation):
    """
    This function manipulates data by adding, subtracting, or multiplying.
    """
    if not isinstance(data, (list, tuple)):
        print("Error: input data must be a list or tuple")
        return
    
    if target_type not in [int, float]:
        print("Error: target type must be int or float")
        return
    
    if operation not in ["add", "subtract", "multiply"]:
        print("Error: operation must be add, subtract, or multiply")
        return
    
    manipulated_data = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            item = data[i][j]
            if isinstance(item, target_type):
                if operation == "add":
                    row.append(item + i + j)
                elif operation == "subtract":
                    row.append(item - i - j)
                elif operation == "multiply":
                    row.append(item * (i+1) * (j+1))
            elif target_type == int:
                try:
                    if operation == "add":
                        row.append(int(item) + i + j)
                    elif operation == "subtract":
                        row.append(int(item) - i - j)
                    elif operation == "multiply":
                        row.append(int(item) * (i+1) * (j+1))
                except ValueError:
                    print("Error: could not convert item to integer")
            elif target_type == float:
                try:
                    if operation == "add":
                        row.append(float(item) + i + j)
                    elif operation == "subtract":
                        row.append(float(item) - i - j)
                    elif operation == "multiply":
                        row.append(float(item) * (i+1) * (j+1))
                except ValueError:
                    print("Error: could not convert item to float")
        manipulated_data.append(row)
    
    return manipulated_data


def f(lst):
    n = len(lst)
    i, j = 0, n-1
    while i < n and j >= 0:
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    k = n // 2
    for i in range(k):
        if lst[i] == lst[-i-1]:
            return True
    return False


