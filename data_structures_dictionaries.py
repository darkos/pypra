def print_title_line(title):
    print('--- ' + title + ' ---')

def print_header(title):
    ticksNum = len(title) + 8
    print('-' * ticksNum)
    print_title_line(title)
    print('-' * ticksNum)

print_header('distionaries')
print("phonebook = {'minja':1234, 'milena':2345, 'jovana':3456}")
phonebook = {'minja':1234, 'milena':2345, 'jovana':3456}
print('phonebook \n' + str(phonebook))
