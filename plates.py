import re

def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    ot = bool(re.match(r'[A-Z]+$', s[0:2]))
    n = bool(re.match(r'[0-9]', s[-1]))

    print(n)
    return True
main()

