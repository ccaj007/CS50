# https://cs50.harvard.edu/python/2022/psets/6/scourgify/

import sys
import os
from sqlalchemy import LargeBinary
from tabulate import tabulate
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguements')
if len(sys.argv) > 3:
    sys.exit('Too many command-line arguements')
if not os.path.isfile(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")


students = []
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"student": name, "house": house})

with open(sys.argv[2],"w") as file:
    writer = csv.DictWriter(file, fieldnames=["fname", "lname", "home"])

    for i in students:
        a = i["student"]
        name = a.rsplit(",")
        fname = name[-1]
        lname = name[0]
        b = i["house"]
        writer.writerow({"fname": fname, "lname": lname, "home": b})

