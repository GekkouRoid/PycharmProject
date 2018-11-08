""" This is a text file for testing Git in Pycharm!
This is a new line for 1st time edition.
End of line
"""

"""This is the 2nd time edition. 
New line appended for 2nd time."""

name = "morris"
print('%s, Welcome to PyCharm' % name)

"""Exercise 2-3: 
Upper case the first char of the name string
"""

# Function Casecon() complete the uppercase convert for the first char of the string
def Casecon(name):
        name = name.upper()[0] + name[1:]
        return name

name = Casecon(name)


print(name)

print('This is Upper case of your name:%s' % name.upper())
print('This is another case of your name in Uppercase:%s' % name)


"""Some new comments"""
# exercise 2-6

name_with_space = '  morris  \t'

name = name_with_space.strip()

print(name, len(name))

num = 8
print('This is my favourite number: %d' % num )


# Add some more comment
# Add some more comment