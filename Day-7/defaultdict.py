# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

"""
Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5

"""
from collections import defaultdict

n, m = map(int, input().split())
# m = int(input())

A = defaultdict(list)
B = []

for i in range(0,n):
    user_input = input()
    A[user_input].append(i+1)

for j in range(0,m):
    user_input = input()
    B.append(user_input)


for word in B:
    if word in A:
        print(' '.join(map(str, A[word])))
    else:
        print(-1)





