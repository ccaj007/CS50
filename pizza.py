# https://cs50.harvard.edu/python/2022/psets/6/pizza/

import sys
import os
from sqlalchemy import LargeBinary
from tabulate import tabulate
import csv

if len(sys.argv) == 1:
    sys.exit('Too few command-line arguements')
if len(sys.argv) > 2:
    sys.exit('Too many command-line arguements')
if not os.path.isfile(sys.argv[1]):
    sys.exit("File doe not exist")


pizzas = []
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for pizza, small, large in reader:
        pizzas.append({"pizza": pizza, "small": small, "large": large})
#    for line in file:
#        pizzas.append(line.rstrip().split(","))

print(tabulate(pizzas, tablefmt="grid"))



