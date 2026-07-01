#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Valar Morghulis")


# Valar Dohaeris

# In[10]:


age_input = input("Enter your age: ")

age = int(age_input)
if age < 0:
    print("Invalid age. Please enter a non-negative number.")
elif age <= 5:
    price = 0
elif age <= 18:
    price = 5
elif age <= 64:
    price = 10
else:
    price = 15

if age >= 0:
    if price == 0:
        print(f"Age {age}: Ticket is free.")
    else:
        print(f"Age {age}: Ticket price is {price}.")


# In[9]:


n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))


# In[12]:


for i in range(3,6):
    print(i,end=" ")


# In[13]:


for i in range(3,20,2):
    print(i,end=" ")


# In[1]:


for i in range(-10,0):
    print(i,end=" ")


# In[6]:


while True:
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("0. Exit")

    ch = int(input("Enter your choice: "))  

    if ch == 1:
        num = int(input("Enter a decimal number: "))
        print("Binary:", bin(num)[2:])  
    elif ch == 2:
        num = int(input("Enter a decimal number: "))
        print("Octal:", oct(num)[2:])  
    elif ch == 3:
        num = int(input("Enter a decimal number: "))
        print("Hexadecimal:", hex(num)[2:]) 
    elif ch == 0:
        print("Exiting program...")
        break 
    else:
        print("Invalid choice, try again.")        


# In[4]:


print("Demo of break:")
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break  
    print("Number:", i)

print("\nDemo of continue:")
for i in range(1, 10):
    if i % 2 == 0:
        continue   
    print("Odd number:", i)

print("\nDemo of pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print("Number:", i)


# In[10]:


n = 5

for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row += chr(65 + j)
    print(row)


# In[17]:


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)


# In[18]:


cube = lambda a:a*a*a
print(cube(5))


# In[19]:


square = lambda a:a*a
print(square(5))


# In[23]:


odd_even = lambda n:"Even" if n%2==0 else "Odd"
print(odd_even(22))


# In[25]:


cel_feren = lambda n:(n*9/5)+32
print(cel_feren(40))


# In[26]:


max_num = lambda n, m: n if n > m else m
print(max_num(12, 48))

