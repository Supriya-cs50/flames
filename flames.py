name1 = input('Enter the first name : ')
list1 = list(name1.lower().replace(" ",""))
name2 = input('Enter the second name : ')
list2 = list(name2.lower().replace(" ",""))


for i in list1[:]:
    if i in list2:
        list1.remove(i)
        list2.remove(i)

count = len(list1) + len(list2)

flamesdict = {'F':'Friends', 'L':'Love', 'A':'Affection', 'M': 'Marriage', 'E':'Enemies', 'S':'Siblings'}

flames = ['F','L','A','M','E','S']

index = 0
while len(flames) > 1:
    index = (index + count - 1) % len(flames)
    flames.pop(index)


print('Your relationship is :',flamesdict[flames[0]])
