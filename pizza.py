import sys
import os
from tabulate import tabulate

with open('sicilian.csv') as file:

    print(tabulate(file, tablefmt="prettytable"))


