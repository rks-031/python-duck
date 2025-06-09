# logical method
def wrap(string, max_width):
    s = str()
    k = 0
    for ch in string:
        if k != 0 and k%max_width == 0:
            s += '\n'
            s += ch
        else:
            s += ch
        k += 1
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# using textwrap library

from textwrap import fill

def wrap(string, max_width):
    return fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)