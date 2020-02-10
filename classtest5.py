#Exercise of 9-11


from classtest2 import User
import Privileges


class Admin(User):
    def __init__(self, firstname, lastname, sexuality='male', career='engineer'):
        super().__init__(firstname, lastname, sexuality='male', career='engineer')
        self.privilege = Privileges.Privileges()


admin1 = Admin('Mike', 'Carson')
admin1.privilege.describe_privileges()
admin1.increment_login_attempts()
admin1.show_login_attempts()


class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print("私有：%s 的年龄是 %d" % (self.name, self.__age))

    def public(self):
        print("公有：%s 的年龄是 %d" % (self.name, self.__age))
        self.__secret()


class Girl(Women):
    def test(self):
        print("你的姓名是 %s" % self.name)
        # print("你的年龄是 % d" % self.__age)  # 不能在子类中直接调用父类的私有属性
        # self.__secret()  # 不能在子类中直接调用父类的私有方法

        # 可以通过调用父类的公有方法来简介调用父类的私有属性和方法
        self.public()  # 运行结果：(公有： xiaohong 的年龄是18  私有：xiaohong 的年龄是 18)
        print("...")


xiaohong = Girl("xiaohong", 18)
# 子类的对象不能在外部直接调用父类/祖父类的私有属性和方法
# print(xiaohong.__age)
# print(xiaohong.__secret)
xiaohong.test()
