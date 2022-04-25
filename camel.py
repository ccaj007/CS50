from operator import delitem
import re

test = 'thisIsTestAAbc'
print('Intial string: ', test)
#new_list=[]
new_list = [s for s in re.split("([A-Z][^A-Z]*)", test) if s]
res = "_".join(new_list)

print('Camel Case: ', str(res))