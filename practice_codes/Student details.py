n= int(input("Enter the number: ") )

def factorial(n):
    if n == 0:
        return 1
    else:
        factNm1=factorial(n-1)
        factN=factNm1*n
        return factN

print("The factorial of", n , "is", factorial(n))