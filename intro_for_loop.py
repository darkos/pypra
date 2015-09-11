words = ['cat','window','defenestrate']
for w in words:
    print(w, len(w))

print(words)

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

for i in range(5):
    print(i)

r =  range(5,10)
print(r)
for i in r:
    print(i)
print('range(0,10,3)')
for i in range(0,10,3):
    print(i)

print('for i in range(-10, -100, -30)')
for i in range(-10, -100, -30):
    print(i)

verse = ['Mary','had','a','little','lamb']
print(verse)
for i in range(len(verse)):
    print(i, verse[i])

r = range(10)
l = list(r)

print(r)
print(l)


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

print('----------')
for num in range(2,10):
    if num % 2 == 0:
        print('Found an even numbner', num)
        continue
    print('Fond an odd number:' , num)
