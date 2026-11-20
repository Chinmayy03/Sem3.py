num = int(input("Enter a positive integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    ans = 1

    for i in range(num, 0, -1):
        ans = ans * i

    print("The factorial of", num, "is", ans)