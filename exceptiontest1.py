# Exercise 10-6


def convert_to_int(num):
    try:
        num_int = int(num)
    except ValueError:
        print('Input invalid, terminated.')
        num_int = None
    return num_int


num1 = input('Please input 1st int: ')
num1 = convert_to_int(num1)
if num1 is not None:
    num2 = input('Please input 2nd int: ')
    num2 = convert_to_int(num2)
    if num2 is not None:
        sum1 = num1 + num2
        print(sum1)
