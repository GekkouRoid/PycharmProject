# Exercise 7-1
# def favourite_book(bookname):
#     """output a name user inout"""
#     print('Your favorite book is: ' + bookname.title())
#
#
# bk = input('Please tell me your favourite book name:')
# favourite_book(bk)

def make_shirt(shirt_words, shirt_size='m'):
    print('\nYour shirt size is: ' + shirt_size.title() + '.')
    print('Your shirt is printed with words: ' + shirt_words.title() + '.')


make_shirt('Big mouth')
make_shirt('Big mouth', 's')
make_shirt('Big mouth', 'l')

