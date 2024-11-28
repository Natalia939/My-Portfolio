# Prompt the user for an arithmetic expression
expression = input("Expression: ").strip()

# Split the input into parts
x, y, z = expression.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Perform the operation based on the operator
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    raise ValueError("Invalid operator")

# Print the result formatted to one decimal place
print(f"{result: .1f}")
