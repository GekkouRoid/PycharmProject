# Exercise of 9-7

from classtest2 import User


class Admin(User):
    def __init__(self, firstname, lastname, sexuality='male', career='engineer'):
        super().__init__(firstname, lastname, sexuality='male', career='engineer')
        self.privileges = ['Can Add Post', 'Can Delete Post']

    def describe_privileges(self):
        print(self.privileges)


if __name__ == '__main__':
    admin1 = Admin('Mike', 'water')
    admin1.describe_privileges()
