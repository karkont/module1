print('1st program')
print(9**0.5*5)
print('2nd program')
print(9.99 > 9.98 and 1000 != 1000.1)
print('3rd program')
print(((1234 % 1000)//10)+((5678 % 1000)//10))
print('4rd program')
a, b = 13.42, 42.13
a1, b1 = int(13.42), int(42.13)
a2, b2 = (int(a - a1) * 100), int((b - b1) * 100)
print(a1 == b2 or a2 == b1)
print('4rd program "2"')
print((int(13.42) == int(42.13 % 1 * 100)) or int(13.42 % 1 * 100) == (int(42.13)))
x = 13.42
y = 42.13
x1 = int(13.42)
x2 = int(13.42 % 1 * 100)
y1 = int(42.13)
y2 = int(42.13 % 1 * 100)
print(x1 == y2 or x2 == y1)
