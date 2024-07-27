my_dict = {'Konstantin': 33, 'Mariya': 25, 'Vlad': 500}
print(my_dict)
print(my_dict.get('Konstantin'), my_dict.get('Svetlana'))
print(my_dict.get('Svetlana'))
my_dict.update({'A': 2, 'B': 4})
my_dict.pop('Vlad')
print(my_dict)
my_set = {1, 1, 1, 'a', 'a', (123, 321), (123, 321)}
print(set(my_set))
my_set.add('w')
my_set.add(55)
my_set.remove('a')
print(my_set)