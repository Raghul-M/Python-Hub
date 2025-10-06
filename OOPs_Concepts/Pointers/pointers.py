num1 = 11
num2 = num1

print("Before num2 value is updated : ")
print(f"num1 = {num1}, num2 = {num2}")

print("\nnum1 points to:", id(num1)) #address of the value that num1 points to
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated : ")
print(f"num1 = {num1}, num2 = {num2}")

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))