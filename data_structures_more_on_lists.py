from collections import deque
from math import pi

def print_title_line(title):
    print('--- ' + title + ' ---')

def print_header(title):
    ticksNum = len(title) + 8
    print('-' * ticksNum)
    print_title_line(title)
    print('-' * ticksNum)


print_header('list.append(x)')
print('This is a list of numbers 1 - 9')
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
print('Appending 10 to this list: numbers.append(10)')
numbers.append(10)
print(numbers)
print("list.appned(x) is the same as a[len(a):] = [x]")
print('Appending 11 the "classic" way: numbers[len(numbers):] = [11]')
numbers[len(numbers):] = [11]
print(numbers)
print_header('list.extend(L)')
additional = [12,13,14,15,16,17,18,19,20]
print('list.extend(L) - will extend list numbers withj list additional numbers')
print('numbers:' + str(numbers))
print('additional:' + str(additional))
print('numbers.extend(additional)')
numbers.extend(additional)
print('numbers:' + str(numbers))
print_header('list.insert(i,x)')
print('list.insert(i,x) i=index of element BEFORE which to insert value x')
print('list.insert(0,-1) inserts -1 at the beginning of the list, since 0 is the first element of the lsit')
print('numbers.insert(0,-1)')
numbers.insert(0,-1)
print(numbers)
print('numbers.insert(len(numbers),21) inserts 21 at the end of the numbers list')
print('numbers.insert(len(numbers),21)')
numbers.insert(len(numbers),21)
print(numbers)
print_header('list.remove(x)')
print('list.remove(x) removes a first occurence of element whose value is x in this list')
print('Will insert 21 in the middle of the list')
print('numbers.insert(len(numbers)//2,21)')
numbers.insert(len(numbers)//2,21)
print(numbers)
print('numbers.remove(21)')
numbers.remove(21)
print(numbers)
print_header('list.pop(i)')
print('list.pop(i) removes and returns item at the index i. list.pop() returns the last item from the list')
print(numbers)
print('numbers.pop(10)')
print(numbers.pop(10))
print(numbers)
print('numbers.pop()')
print(numbers.pop())
print(numbers)
print_header('list.index(x)')
print('list.index(x) return the index of the first occurence of the eleemnt whose value is x')
print('Will insert 20 in the middle of the list')
print('numbers.insert(len(numbers)//2,20)')
numbers.insert(len(numbers)//2,20)
print(numbers)
print('numbers.index(20)')
print(numbers.index(20))
print_header('list.count(x)')
print('list.count(x) return number of how many times value x appears in the list')
print(numbers)
print('numbers.count(20)')
print(numbers.count(20))
print_header('list.reverse()')
print('list.reverse() reverses the order of elements in the list in place')
print(numbers)
print('numbers.reverse()')
numbers.reverse()
print(numbers)
print_header('list.sort()')
print('list.sort() sorts the elements of the list')
print('numbers.sort()')
numbers.sort()
print(numbers)
print_header('list.copy()')
print('list.copy() returns shallow copy of the list')
print('copy_of_numbers = numbers.copy()')
copy_of_numbers = numbers.copy()
print('numbers' + str(numbers))
print('copy_of_numbers' + str(copy_of_numbers))
print_header('list.clear()')
print('list.clear() removes all elements from this list')
print('copy_of_numbers.clear()')
copy_of_numbers.clear()
print('copy_of_numbers:', str(copy_of_numbers))
print_header('deque')
print('deque is helpful when using list as queues')
print("names=['john','paul','george','ringo','brian','stewart']")
names=['john','paul','george','ringo','brian','stewart']
print('queue = deque(names)')
queue = deque(names)
print(queue)
print("queue.append('mick')")
queue.append('mick')
print("queue.popleft() - first in first out")
queue.popleft()
print(queue)
print('queue.pop() - last in first out')
print(queue.pop())
print(queue)
print_header('list comprehensions')
print('squares = [x**2 for x in range(10)]')
squares = [x**2 for x in range(10)]
print(squares)
print("combs = [(x,y) for x in [1,2,3] for y in [4,5] if x != y]")
combs = [(x,y) for x in [1,2,3] for y in [4,5] if x != y]
print(combs)
print('--- filtering list ---')
print('vec = [-4, -2, 0, 2, 4]')
vec = [-4, -2, 0, 2, 4]
print(vec)
print("vec1 = [x*2 for x in vec] - new list with values doubled")
vec1 = [x*2 for x in vec]
print(vec1)
print("vec2 = [x for x in vec1 if x >= 0]")
vec2 = [x for x in vec1 if x >= 0]
print(vec2)
print("vec3 = [abs(x) for x in vec2] - applying function to all elements")
vec3 = [abs(x) for x in vec2]
print(vec3)
print('--- call method on each element ---')
print("freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']")
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
print("fr1 = [fr.strip() for fr in freshfruit]")
fr1 = [fr.strip() for fr in freshfruit]
print(fr1)
print('--- x, x **2, x **3 for each element ---')
print("nl = [(x, x**2, x**3) for x in range(6)]")
nl = [(x, x**2, x**3) for x in range(6)]
print(nl)
print('--- flatten list ---')
print("nfl = [[1,2,3],[4,5,6],[7,8,9]]")
nfl = [[1,2,3],[4,5,6],[7,8,9]]
print("fl = [num for elem in nfl for num in elem]")
fl = [num for elem in nfl for num in elem]
print(fl)
print('--- complex expressions and nested functions ---')
print("rp = [str(round(pi, i)) for i in range(6)]")
rp = [str(round(pi, i)) for i in range(6)]
print(rp)
print('--- nested list comprehensions ---')
print("matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]")
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
print('[[row[i] for row in matrix] for i in range(4)] will convert rows into columns')
print("converted = [[row[i] for row in matrix] for i in range(4)]")
converted = [[row[i] for row in matrix] for i in range(4)]
print(converted)
print_header('using del')
print('numbers:' + str(numbers))
print("del(numbers[0])")
del(numbers[0])
print('numbers:' + str(numbers))
print("del(numbers[7:14])")
del(numbers[7:14])
print('numbers:' + str(numbers))
print("del numbers[:]")
del(numbers[:])
print('numbers:' + str(numbers))
print("del a will throw an error")
# del a
print('numbers')
print(numbers)
print_header('tuples')
print('empty = ()')
empty = ()
print("empty " + str(empty))
print("single = 'harvey',")
single = 'harvey',
print('single ' + str(single))
print("len(empty)")
print(len(empty))
print("len(single)")
print(len(single))
print("t = 'peter', 'john', 999, 3.14159,")
t = 'peter', 'john', 999, 3.14159,
print('t ' + str(t))
print("basket = {'apple','orange','apple','orange','banana','cherry','watermellon','banana','pear'}")
basket = {'apple','orange','apple','orange','banana','cherry','watermellon','banana','pear'}
print(basket)
print('notice, no duplicates')
print("'orange' in basket")
print('orange' in basket)
print("'plum' in basket")
print('plum' in basket)
print("a = set('abracadabra')")
a = set('abracadabra')
print('a ' + str(a))
print("b = set('alacazam')")
b = set('alacazam')
print('b ' + str(b))
print('a - b ' + str(a-b))
print('b - a ' + str(b-a))
print('a | b ' + str(a | b))
print('a & b ' + str(a & b))
print('a ^ b ' + str(a ^ b))
print_header('set comprehensions')
print("a = {letter for letter in 'abracadabra' if letter not in 'abc'}")
a = {letter for letter in 'abracadabra' if letter not in 'abc'}
print(a)
