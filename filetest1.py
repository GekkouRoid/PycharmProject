import datetime


with open('D:\Documents\PythonDocs\ehmatthes-pcc-f555082\chapter_10\programming.txt') as f_obj:
    lines = f_obj.readlines()

m_lines = []

for line in lines:
    m_line = line.replace('python', 'C#')
    m_lines.append(m_line)

with open('D:\Documents\PythonDocs\ehmatthes-pcc-f555082\chapter_10\programming1.txt', 'w') as f_obj:
    for line in m_lines:
        f_obj.write(line)

with open('D:\Documents\PythonDocs\ehmatthes-pcc-f555082\chapter_10\guestbook.txt', 'w') as f_obj:
    while True:
        username = input('Please input your name. ')
        if username == 'q':
            break
        else:
            t = str(datetime.datetime.now())
            f_obj.write(username + ' has visited at ' + t + '\n')
