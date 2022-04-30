#lst = ['apple', 'zoo', 'apple', 'banana', 'kiwi', 'zoo', 'apple']
lst = []
while True:
    try:
        item = input()
    
    except EOFError:
        break
    
    else:
        lst.append(item)

#print(lst)

new_lst = set(lst)
grocery_dict = {}
for ele in new_lst:
    grocery_dict[ele] = 0

for ele in lst:
    grocery_dict[ele] += 1

#new_dict = {}
new_dict = sorted(grocery_dict)
for i in new_dict:
    print(grocery_dict[i], i.upper())

#for i in grocery_dict:
#
#    print(grocery_dict[i])
#    print(i.upper())
#
