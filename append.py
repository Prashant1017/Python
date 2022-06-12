#WAP to ask a user to enter the marks in 5 different subjects and find his total, average, percentage, minimum marks and max marks among subject

mark = []
total = 0
print("Enter marks:")
A = int(input("Marks in A: "))
B = int(input("Marks in B: "))
C = int(input("Marks in C: "))
D = int(input("Marks in D: "))
E = int(input("Marks in E: "))

mark.append(A)
mark.append(B)
mark.append(C)
mark.append(D)
mark.append(E)
sum_ = sum(mark)
for i in range(len(mark)):
    total = total + mark[i]

ave = total/5

min_value = min(mark)
max_value = max(mark)

print(total)
print(ave)
print(min_value)
print(max_value)