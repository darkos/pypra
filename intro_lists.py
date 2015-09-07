squares = [1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[1:3])
print(squares[3:1])
print(squares[2:])
print(squares[:2])
print(squares[-2:-4])
print(squares[-4:-2])
squares = squares + [36,49,64,81,100]
print(squares)
cubes = [1,8,27,65,125]
print(cubes)
print("replacing wrong 4 ** 3")
cubes[3] = 64
print(cubes)
print('3 ** 5: ' + str((3 ** 5)))
cubes.append(216)
cubes.append(343)
print(cubes)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C','D','E']
print(letters)
