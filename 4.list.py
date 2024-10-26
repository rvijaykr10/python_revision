my_list = [1, 2, '3', True]
result = len(my_list)
result = my_list.index('3')
result = my_list.count(2)

result = my_list[3]
result = my_list[1:]
result = my_list[:1]
result = my_list[-1]
result = my_list[::1]
result = my_list[::-1]
result = my_list[0:3:2]

result = my_list * 2
result = my_list + [100]

result = my_list.append(100)  # mutates
result = my_list.extend([100, 200])  # mutates
result = my_list.insert(2, '!!!')  # mutates

result = ' '.join(['Hello', 'There'])

basket = ['apples', 'pears', 'oranges']
result = basket.copy()  # copy
result = basket[:]  # copy

numbers = [1, 2, 3]
result = numbers.pop()
result = numbers.pop(1)
result = numbers.remove(2)
result = numbers.clear()


numbers = [1, 2, 5, 3]
result = numbers.sort()
result = numbers.sort(reverse=True)
result = numbers.reverse()
result = sorted(numbers)
result = list(reversed(numbers))


result = 1 in numbers
result = min(numbers)
result = max(numbers)
result = sum(numbers)
first, *x, last = numbers


a = [i for i in 'hello']
b = [i * 2 for i in [1, 2, 3]]
c = [i for i in range(0, 10) if i % 2 == 0]


list_of_chars = list('Hello')
element_sum = [sum(pair) for pair in zip([1, 2, 3], [4, 5, 6])]
sorted_by_key = sorted(['hi', 'you', 'man'], key=lambda el: el[1])
sorted_by_key = sorted([
    {'name': 'Bina', 'age': 30},
    {'name': 'Andy', 'age': 18},
    {'name': 'Zoey', 'age': 55}],
    key=lambda el: (el['name']))
