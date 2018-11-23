# Exercise of 10.36


def count_file_words(filename, one_string=''):
    """To count how many words there are in the file; or,
    if necessary, count how many times the one_string appears in the file.
    returned result is a list"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('File ' + filename + ' not found!')
    else:
        if one_string:
            return [contents.lower().count(one_string.lower()), len(contents.split())]
        else:
            return [len(contents.split()),]


f_name = input('Please input your file name: ')
input_string = input('Please the string you like to find:')
n = count_file_words(f_name, input_string)
print(n)

