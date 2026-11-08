n = int(input("Enter a number: ")) 

def sumN(n): 
    if n < 0: 
        return "Sum is not defined for negative numbers." 
    elif n == 0: 
        return 0 
    else: 
        return sumN(n - 1) + n 

tom = sumN(n) 
print(f"the sum of {n} is {tom}")
    