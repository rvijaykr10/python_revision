my_tuple = ('apple', 'grapes', 'mango', 'grapes')

apple, grapes, mango, grapes = my_tuple

result = len(my_tuple)

result = my_tuple[2]
result = my_tuple[-1]

my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('canday')  # AttributeError

result = my_tuple.index('grapes')
result = my_tuple.count('grapes')

result = list(zip([1, 2, 3], [4, 5, 6]))

z = [(1, 2), (3, 4), (5, 6), (7, 8)]


def unzip(z): return list(zip(*z))


unzip(z)
