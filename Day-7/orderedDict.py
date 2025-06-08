# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
items = OrderedDict()

for i in range(0,N):
    user_input = input()
    *item_name, price = user_input.split()
    item_name = ' '.join(item_name)
    price = int(price)
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price
    
for item in items:
    print(f"{item} {items[item]}")
    


