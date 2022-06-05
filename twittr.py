import re

vowel = ['A','E','I','O','U','a','e','i','o','u']

def main():
    inp = input('Input: ')
    print(shorten(inp))

def shorten(word):
    new = ''
    for char in word:
        if char not in vowel:
            new += char
    return new

if __name__ == '__main__':
    main()