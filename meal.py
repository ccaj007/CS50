from operator import ge


def main():
    time = input('What time is it? ')
    t = convert(time)
    if t >= 7.00 and t <= 8.00:
        print('Breakfast')
    if t >= 12.00 and t <= 13.00:
        print('Lunch')
    if t >= 18.00 and t <= 19.00:
        print('Dinner')

def convert(time):
    hours, min = time.split(":")
    minutes = int(min) / 60
    time = int(hours) + minutes
    return time


if __name__ == "__main__":
    main()
