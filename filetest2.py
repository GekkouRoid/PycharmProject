# Exercise of 10.36

filename = 'D:\Documents\PythonDocs\ehmatthes-pcc-f555082\chapter_10/\/alice.txt'


def count_file_words(filename):
    """To count how many words there are in the file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('File ' + filename + ' not found!')
    else:
        words = contents.split()
        num = len(words)
        return num


f_name = input('Please input your file name: ')
n = count_file_words(f_name)
if n:       # if file not exists, returned n will be None, so check it.
    print(n)

