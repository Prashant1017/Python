#Dictionary

#Check if the key is present or not

# dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# x = int(input("Enter a number: "))

# if x in dic:
#     print("Key is present.")

# else:
#     print("Key is not present.")


#print in the form x, x*x

n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 

