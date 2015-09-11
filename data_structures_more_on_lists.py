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
additional = [12,13,14,15,16,17,18,19,20]
print('list.extend(L) - will extend list numbers withj list additional numbers')
print('numbers:' + str(numbers))
print('additional:' + str(additional))
print('numbers.extend(additional)')
numbers.extend(additional)
print('numbers:' + str(numbers))
