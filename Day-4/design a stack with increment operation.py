class CustomStack:
    v = []
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.v = []

    def push(self, x: int) -> None:
        if len(self.v) < self.maxSize:
            self.v.append(x)

    def pop(self) -> int:
        if(len(self.v) == 0):
            return -1
        x = self.v[-1]
        self.v.pop()
        return x

    def increment(self, k: int, val: int) -> None:
        if(len(self.v)<k):
            for i in range(0,len(self.v)):
                self.v[i] += val
        else:
            for i in range(0,k):
                self.v[i] += val
                


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)