# https://cs50.harvard.edu/python/2022/psets/8/jar/
import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        
    def __str__(self):
        return "🍪 " * self.size

    def deposit(self, n):
       self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if not(isinstance(n, int) and n > 0):
            raise ValueError('incorrect capacity')
            sys.exit()
        if n < 0:
            raise ValueError("Capacity isn't non-negative")
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError("Adding more cookies than max capacity")
        elif n < 0:
            raise ValueError("Not enough cookies to remove")

        self._size = n

def main():
    
    jar = Jar(5)
#    jar = Jar.get()
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(1)
    print(jar)
#    jar.deposit(20)
#    print(jar)


if __name__ == '__main__':
    main()

