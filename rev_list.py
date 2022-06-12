#Reversing a list

alist = [100, 200, 300, 400, 500]
blist = alist[::-1]
print(blist)

#Concatenate two lists 

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

print(list3)

#Turn every item no list into square

aList = [1,2,3,4,5,6,7]
bList = []
for i in aList:
    bList.append(i**2)

print(bList)

    
#Concatenate two lists

list_1 = ["Hello", "take"]
list_2 = ["Dear", "Sir"]
list_3 = []

for i in range(len(list_1)):
    for j in range(len(list_2)):
        list_3.append(list_1[i]+list_2[j])

print(list_3)

#list1 should gibe item in original order and list2 in reverse order

a = [10, 20, 30, 40]
b = [100, 200, 300, 400]

for i in range(len(a)):
    print(a[i],b[(i +1)*(-1)])


#Remove empty string

x = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in range(len(x)):
    if "" in x:
        x.remove("")
    else:
        break
print(x)


#Add 7000 after 6000 in the list

y = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

y[2][2].append(7000)
print(y)

#If there is 20 replace by 200 only update first occurence

z = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(z)):
    if z[i]== 20:
        z[i] = 200
        break

print(z)


w = [5, 10, 15, 20, 25, 50, 20]

for j in range(len(w)):
    
    if 20 in w:
        w.remove(20)
    else:
        break

print(w)
