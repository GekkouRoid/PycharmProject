# Exercise 8-9


def show_magicians(m_names):
    for name in m_names:
        print('Magician name is:' + name.title() + '.')


# def make_great(m_names):
#     mnames = []
#     for name in m_names:
#         name = 'The great ' + name
#         mnames.append(name)
#     return mnames

#
def make_great(m_names):
    for i in range(len(m_names)):
        name = m_names[i]
        name = 'The great ' + name
        m_names[i] = name
    return m_names


names = ['ma1', 'ma2', 'ma3']
show_magicians(names)

othernames = make_great(names)
show_magicians(names)
show_magicians(othernames)
