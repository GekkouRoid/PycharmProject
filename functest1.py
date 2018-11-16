# Exercise 7-1
# def favourite_book(bookname):
#     """output a name user inout"""
#     print('Your favorite book is: ' + bookname.title())
#
#
# bk = input('Please tell me your favourite book name:')
# favourite_book(bk)

# Exercise 8-3


def make_shirt(shirt_words='I love Python', shirt_size='m'):
    print('\nYour shirt size is: ' + shirt_size.title() + '.')
    print('Your shirt is printed with words: ' + shirt_words.title() + '.')


make_shirt('Big mouth')
make_shirt('Big mouth', 's')
make_shirt('Big mouth', 'l')
make_shirt()
make_shirt(shirt_size='l')

# Exercise 8-7


def make_album(singer, album_name, song_number=''):
    album = {}
    if song_number:
        album = {'singer':singer, 'album_name':album_name, 'song_number':song_number}
    else:
        album = {'singer':singer, 'album_name':album_name,}
    return album


album1 = make_album('Singer1', 'bb1', 6)
print(album1)
