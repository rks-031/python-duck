# anonymous one line function

add_1 = lambda x, y: x + y

res = add_1(1,2)
print(res)

# lambda functions can be used as arguments to higher-order functions

my_numbers = [1, 2, 3, 4, 5]

suqares = list(map(lambda x: x ** 2, my_numbers))
print(suqares)

#filtering with lambda functions
evens = list(filter(lambda x: x % 2 == 0, my_numbers))
print(evens)

#sorting with lambda functions
values = [(1,'a','hello'), (2,'a','world'), (3,'c','python')]
sorted_list = sorted(values,key = lambda x: x[1] + x[2])
print(sorted_list)

#accumulating with lambda functions
from functools import reduce

my_numbers = [1,2,3,4,5]

sum_of_nos = reduce(lambda acc, x: acc + x, my_numbers)
print(sum_of_nos)

# output
# acc = 1, x = 2 --> acc = 1 + 2 = 3
# acc = 3, x = 3 --> acc = 3 + 3 = 6
# acc = 6, x = 4 --> acc = 6 + 4 = 10
# acc = 10, x = 5 --> acc = 10 + 5 = 15

my_numbers = [1,5,3,2,4]

max_val = reduce(lambda acc, x : acc if acc > x else x, my_numbers)
print(max_val)

# output
# acc = 1, x = 5 --> acc = 5
# acc = 5, x = 3 --> acc = 5
# acc = 5, x = 2 --> acc = 5
# acc = 5, x = 4 --> acc = 5