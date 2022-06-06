# https://cs50.harvard.edu/python/2022/psets/7/working/

import re
import sys


def main():
    #print(convert(input("Hours: ")))
    print(convert("9:30 AM to 5 PM"))


def convert(s):
    reg_time = "(\d+)(:\d+)?\s[AP]M$"
    matches = re.findall(reg_time,s)
    
#    matches = re.findall(reg_time,s)
#    for i in matches:
#        print(int(i[0])+12)
#        if i[1] == "":
#            print(f"list {i} ")
    return matches


if __name__ == "__main__":
    main()


