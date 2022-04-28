

while True:
    s = input('Fraction: ')
    n, d = s.split('/')
    print(n)
    print(d)
    try:
        value = round(int(n) / int(d))
        print(value)
    except (ZeroDivisionError, ValueError):
        print("error")
    
    else:
        break


if value > .99:
    print('F')
elif value < .01:
    print('E')
else:
    print(f"{value * 100}%")

