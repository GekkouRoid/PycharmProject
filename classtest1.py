# Exercise of 9-1
class Restaurant():
    """This is the comment of class Res"""

    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype
        self.min_num = 6
        self.number_served = self.min_num

    def describe_restaurant(self):
        print('Restaurant name is: ' + self.restaurant_name.title() + '.')
        print('Cuisine type is ' + self.cuisine_type.title() + '.')
        print('We can serve ' + str(self.number_served) + ' guests.')

    def open_restaurant(self):
        print('Restaurant ' + self.restaurant_name.title() + ' is open.')

    def update_number(self, num):
        if num < self.min_num:
            print('Input is too small. Please increase it.')
        else:
            self.number_served = num

    def increment_number(self, increnum):
        if increnum > 0:
            self.number_served += increnum
        else:
            print('increment cannot be negative.')


my_res = Restaurant('ming', 'J')
my_res.describe_restaurant()
my_res.open_restaurant()

my_res2 = Restaurant('Yang', 'French')
my_res3 = Restaurant('Bo', 'Italy')

my_res2.describe_restaurant()
my_res3.describe_restaurant()
my_res3.update_number(-7)
my_res3.increment_number(-9)
my_res3.describe_restaurant()