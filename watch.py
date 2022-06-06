# https://cs50.harvard.edu/python/2022/psets/7/watch/

import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = 'https?://(www\.)?youtube\.com/embed/(\w+)'

    p = re.compile(regex)
    matches = re.search(p,s)
    if matches:
        return f"https://youtu.be/{matches.group(2)}" 
    else:
        return "None"

if __name__ == "__main__":
    main()
