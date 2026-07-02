# Electricity Bill Calculator

units = int(input("Enter units consumed: "))

if units <= 50:
    bill = units * 3.20

elif units <= 200:
    bill = (50 * 3.20) + (units - 50) * 3.95

else:
    bill = (50 * 3.20) + (150 * 3.95) + (units - 200) * 5.00

print("Electricity Bill = ₹", bill)


#number system 

n = int(input("Enter number: "))

binary = format(n, "b")
octal = format(n, "o")
hexa = format(n, "X")

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexa)