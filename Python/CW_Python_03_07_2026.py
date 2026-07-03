"""
=========================================
Python Classwork
Author : Harshrajsinh Zala
=========================================

Topics Covered:
1. Dictionary Operations
2. File Handling - Student Result Processing
"""

# =====================================================
# Practical 1 : Dictionary Operations
# =====================================================

print("========== DICTIONARY OPERATIONS ==========\n")

sq = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# all()
print("All:", all(sq))

# any()
print("Any:", any(sq))

# len()
print("Length:", len(sq))

# sorted()
print("Sorted Keys:", sorted(sq))

# copy()
b = sq.copy()
print("Copied Dictionary:", b)

# clear()
b.clear()
print("After Clear:", b)

# items()
print("Items:", sq.items())

# keys()
print("Keys:", sq.keys())

# values()
print("Values:", sq.values())

# Sum of Dictionary Values
dict1 = {1: 50, 2: 100, 3: 150, 4: 200}
print("Sum of Values:", sum(dict1.values()))

print("\n==========================================\n")


# =====================================================
# Practical 2 : File Handling - Student Result
# =====================================================

print("========== STUDENT RESULT PROCESSING ==========\n")

# results.txt should contain data like:
#
# 101,Rahul,85,90,80
# 102,Priya,75,65,70
# 103,Amit,35,55,60
# 104,Neha,90,92,88

f = open(r"D:\results.txt", "r")

data = f.readlines()

print("RollNo\tName\tPython\tC++\tDS\tResult\tTotal\tAverage")
print("==============================================================")

final_result = []

for i in data:

    r = i.strip().split(",")

    if int(r[2]) > 40 and int(r[3]) > 40 and int(r[4]) > 40:
        result = "PASS"
    else:
        result = "FAIL"

    total = int(r[2]) + int(r[3]) + int(r[4])
    average = total / 3

    print(
        r[0], "\t",
        r[1], "\t",
        r[2], "\t",
        r[3], "\t",
        r[4], "\t",
        result, "\t",
        total, "\t",
        average
    )

    r.insert(5, result)
    r.insert(6, total)
    r.insert(7, average)

    final_result.append(r)

f.close()

# Uncomment to display updated list
# for student in final_result:
#     print(student)

print("\n========== PROGRAM COMPLETED ==========")