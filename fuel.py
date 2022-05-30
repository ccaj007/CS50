while True:
    s = input('Fraction: ')
    n, d = s.split('/')

    try:
        value = int(n)/int(d)
    except (ZeroDivisionError, ValueError):
        pass
    
    else:
        break


if value > .98:
    print('F')
elif value < .02:
    print('E')
else:
    print(f"{value * 100}%")

