# 2456  ----->  6542
# -2456  ----->  -6542

def reverse(num):
    x = num
    rev = 0
    num = abs(num)
    while(num>0):
        r = num%10
        rev = rev*10 + r
        num = int(num/10)
    if(x<0):
        rev = rev* -1
    return rev


def checkPalindrome(num):
    re = reverse(num)
    print(reverse(num))
    if(num == re):
        print("Palindrome")
    else:
        print("Not Palindrome")
num = int(input("Enter any num: "))
checkPalindrome(num)