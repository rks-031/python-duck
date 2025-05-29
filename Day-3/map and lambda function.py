cube = lambda x: x**3

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibonacci(n):
    fib_list = []
    
    for i in range(0,n):
        fib_list.append(fibo(i))
    
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))