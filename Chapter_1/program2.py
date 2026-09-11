# 1. Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Print a nice header
print("\n--- CALCULATOR RESULTS ---")

# 3. Perform and print each arithmetic operation
print("Addition:       ", num1, "+", num2, "=", num1 + num2)
print("Subtraction:    ", num1, "-", num2, "=", num1 - num2)
print("Multiplication: ", num1, "*", num2, "=", num1 * num2)
print("Division:       ", num1, "/", num2, "=", num1 / num2)
print("Floor Division: ", num1, "//", num2, "=", num1 // num2)
print("Modulus (Rem.): ", num1, "%", num2, "=", num1 % num2)
print("Exponentiation: ", num1, "**", num2, "=", num1 ** num2)

print("--------------------------")
