# Exercise 10-6


def get_sum(n1, n2):
    try:
        sum = int(n1) + int(n2)
    except ValueError:
        print('Your input is not digits, terminated.')
        sum = None
    else:
        return sum


num1 = input('Please input your 1st number: ')
num2 = input('Please input your 2nd number: ')

sum1 = get_sum(num1, num2)
if sum1:
    print(sum1)
