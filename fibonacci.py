#Fibonacci

a = 1
b = 1
print(a)
print(b)
for i in range(1,11):
    c = a+b
    a = b
    b = c
    print(c)

#Factorial

n = int(input("Enter a number"))
f = 1

while(n>0):
    fact = n*f
    n = n-1
    f = fact
print(fact)
