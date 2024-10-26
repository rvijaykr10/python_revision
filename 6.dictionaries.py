my_dict = {'name': 'John Doe', 'age': 25, 'magic_power': False}


result = my_dict['name']
result = len(my_dict)
result = list(my_dict.keys())
result = list(my_dict.values())
result = list(my_dict.items())


age = my_dict.get('age')
age = my_dict.get('age', 0)
my_dict['favourite_snack'] = 'Grapes'
my_dict.update({'cool': True})


del my_dict['name']
result = my_dict.pop('name', None)
new_dict = my_dict.pop('magic_power')


new_dict = dict([['name', 'John'], ['age', 32], ['magic_power', False]])

result = {**my_dict, **{'cool': True}}

new_dict = dict([['name', 'John'], ['age', 32], ['magic_power', False]])

new_dict = dict(zip(['name', 'age', 'magic_power'], ['John', 32, False]))


result = {key: value for key, value in my_dict.items() if key ==
          'age' or key == 'name'}
