class Employee:

    attr = None

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Jon', 'Smith', 60000)
emp_2 = Employee('Jim', 'Michael', 63000)

emp_1.attr = '1'
print(emp_1.attr)
print(emp_2.attr)
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

emp_1.hhhh = 0
print(emp_1.hhhh)
