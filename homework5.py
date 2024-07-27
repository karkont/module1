a = 'hello'
b = 123
c = 1.5
d = True
e = ['1', '2']
immutable_var = a, b, c, d, e
print('Immutable tuple: ', immutable_var)
# immutable_var[0] = int      TypeError: 'tuple' object does not support item assignment
mutable_list = [a, b, c, d, e]
mutable_list[0] = a.upper()[:-1]
print('Mutable list: ', mutable_list)