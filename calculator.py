#Calculator

def add(P,Q):
    return P+Q
def sub(P,Q):
    return P-Q
def mul(P,Q):
    return P*Q
def div(P,Q):
    return P/Q

print("Select the operation: ")
print("a. Addition.")
print("b. Subtraction.")
print("c. Multiplication.")
print("d. Divison.")



choice = input("Enter your choice: ")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if(choice == 'a'):
    print(num1, "+" ,num2, "=", add(num1,num2))
elif(choice == 'b'):
    print(num1, "-", num2, "=", sub(num1, num2))
elif(choice == 'c'):
    print(num1, "*", num2, "=", mul(num1,num2))
elif(choice == 'd'):
    print(num1, "/", num2, "=", div(num1,num2))
else:
    print("Choice is invalid.")
