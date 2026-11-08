n=int(input("Enter a number: "))

def fib(n):
    if n<0:
        return "Fibonacci is not defined for negative numbers."
    elif n==0 or n==1:
        return 1
    else:
        fibNM1=fib(n-1)
        fibNM2=fib(n-2)
        fibN=fibNM1+fibNM2
        return fibN

    
tomorrow=fib(n)
print(f"the fibonacci of {n} is {tomorrow}")
              
              