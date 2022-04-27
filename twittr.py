import re

vowel = ['A','E','I','O','U','a','e','i','o','u']

inp = input('Input: ')
new = ''
for char in inp:
    if char not in vowel:
        new += char

print(new)