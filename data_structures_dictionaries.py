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
print("phonebook['minja']")
print(phonebook['minja'])
print("phonebook['milan'] = '9876'")
phonebook['milan'] = '9876'
print('phonebook ' + str(phonebook))
print("del phonebook['milan']")
del phonebook['milan']
print('phonebook ' + str(phonebook))
print("phonebook['nikola'] = '4567'")
phonebook['nikola'] = '4567'
print('phonebook ' + str(phonebook))
print("list(phonebook.keys())")
print(list(phonebook.keys()))
print("print(sorted(phonebook.keys()))")
print(sorted(phonebook.keys()))
print("'milena' in phonebook")
print('milena' in phonebook)
print("'milan' in phonebook")
print('milan' in phonebook)
print("dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])")
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print("d = {x: x**2 for x in (2, 4, 6)}")
d = {x: x**2 for x in (2, 4, 6)}
print(d)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
