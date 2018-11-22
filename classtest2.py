# User test exercise
class User:
    def __init__(self, firstname, lastname, sexuality='male', career='engineer'):
        self.first_name = firstname.title()
        self.last_name = lastname.title()
        self.sex = sexuality
        self.career = career
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(self.login_attempts)

    def describe_user(self):
        username = self.get_user_name()
        user_message = 'This is the user\'s information:\n' + \
            'user name is: ' + username + '\n' + \
            'user sexuality is ' + self.sex
        print(user_message)

    def greet_user(self):
        username = self.get_user_name()
        print('Hello, ' + username + '.')

    def get_user_name(self):
        username = self.first_name + ' ' + self.last_name
        return username


me = User('john', 'Smith')
me.describe_user()
me.greet_user()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)

me.reset_login_attempts()
print(me.login_attempts)
