# Exercise of 9-6
from classtest1 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, name, ctype):
        super().__init__(name, ctype)
        self.flavors = ['original', 'cherry', 'mango']

    def describe_restaurant(self):
        print('Ice cream stand name is: ' + self.restaurant_name.title() + '.')
        print("Here supplies following ice creams: ")
        print(self.flavors)


my_res5 = IceCreamStand('Bo', 'Italy')
my_res5.describe_restaurant()
