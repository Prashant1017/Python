#WAP to find greatest, smallest and middle number
num1,num2,num3 = 0,0,0
while(True):
    try:
        num1 = int(input("Enter a 1st number: "))
        num2 = int(input("Enter a 2nd number: "))
        num3 = int(input("Enter a 3rd number: "))
        break
    except:
        print("No string or special character allowed")
N = 0
while(True):
    print("Enter 1 for greatest 2 for smallest and 3 for middle number.")
    try:
        N = int(input("Enter a number: "))
        if N not in [1,2,3]:
            print("Invalid Selection. Please choose again")
        else:
            break
    except:
        print("No string or special character allowed")

if(N==1):
    if(num1>num2 and num1>num3):
        print(num1, "is the greatest number.")
    elif(num2>num1 and num2>num3):
        print(num2, "is the greatest number.")
    else:
        print(num3, "is the greatest number.")

elif(N==2):
    if(num1<num2 and num1<num3):
        print(num1, "is the smallest number.")
    elif(num2<num1 and num2<num3):
        print(num2, "is the smallest number.")
    else:
        print(num3, "is the smallest number.")

else:
    if((num1>num2 and num1<num3) or (num1<num2 and num1>num3)):
        print(num1, "is the middle number.")
    elif((num2>num1 and num2<num3) or (num2<num1 and num2>num3)):
        print(num2, "is the middle number.")
    else:
        print(num3, "is the middle number.")
