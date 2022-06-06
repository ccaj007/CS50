# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
    #        "2[0-4][0-9]|25[0-5])\\.){3}"\
    #        "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
    #        "2[0-4][0-9]|25[0-5])"  
    regex = "^(?:(?:0?0?\d|0?[1-9]\d|1\d\d|2[0-5][0-5]|2[0-4]\d)\.){3}(?:0?0?\d|0?[1-9]\d|1\d\d|2[0-5][0-5]|2[0-4]\d)$"

    p = re.compile(regex)
    if (re.search(p,ip)): return "Valid IPv4"
    else: return "Invalid IPv4"




if __name__ == "__main__":
    main()
