def factorial(num):
    fact = 1
    for i in range(num,0,-1):
        fact = fact*i
    print(fact)

factorial(5)
factorial(6)