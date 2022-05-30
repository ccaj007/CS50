import re

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August":8 ,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        inp = input('Date: ')
        a = re.split('[,/\s]+', inp)
        if a[0].title() in months:
            if int(a[1]) in range(1,32):
                print(f"{a[2]}-{months[a[0].title()]:02}-{int(a[1]):02}")
                break
        if int(a[0]) in range(1,13):
            if int(a[1]) in range (1,31):
                print(f"{a[2]}-{int(a[0]):02}-{int(a[1]):02}")
                break
    except EOFError:
        break
    
    else:
        pass