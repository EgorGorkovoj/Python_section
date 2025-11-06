class Fibo:

    def __init__(self, n: int):
        self.n = n
        self.previous = 0
        self.next = 0

    def __iter__(self):
        self.value = self.previous + self.next
        return self

    def __next__(self):
        if self.value == 0:
            self.value = self.value + self.next
            self.next = 1
            self.n -= 1
            return self.value
        if self.n == 0:
            raise StopIteration
        self.value = self.previous + self.next
        self.previous = self.next
        self.next = self.value
        self.n -= 1
        return self.value


fibo = Fibo(n=10)
result = [num for num in fibo]
print(result)
