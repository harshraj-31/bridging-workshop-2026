# ============================================
# h1) Spam Detector (Linear Search)
# ============================================

# Definition:
# Linear Search checks each element one by one
# until the target is found or the list ends.
# It works on both sorted and unsorted lists.

def linear_search(blacklist, sender):
    for i in range(len(blacklist)):
        if blacklist[i] == sender:
            return i
    return -1

print("===== h1) Spam Detector =====")

blacklist = ["spam123", "offer456", "fake789", "ads999"]

sender = input("Enter Sender ID: ")

result = linear_search(blacklist, sender)

if result != -1:
    print("Spam Sender Found at index", result)
else:
    print("Safe Email")


# ============================================
# h2) E-Commerce Price Filter (Lower Bound)
# ============================================

# Definition:
# Binary Search works only on sorted lists.
# Lower Bound finds the first element
# greater than or equal to the target.

def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

print("\n===== h2) E-Commerce Price Filter =====")

prices = [25000, 32000, 42000, 50000, 55000, 62000, 70000]

target = int(input("Enter Minimum Price: "))

index = lower_bound(prices, target)

if index != -1:
    print("First Laptop Price:", prices[index])
else:
    print("No Laptop Found")


# ============================================
# h3) IRCTC Waitlist Merger (Merge Step)
# ============================================

# Definition:
# Merge Sort divides the list into smaller parts,
# sorts them, and merges the sorted lists.
# Here we perform only the merge step.

def merge(list1, list2):
    result = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

print("\n===== h3) IRCTC Waitlist Merger =====")

waitlist1 = [2, 5, 8, 12]
waitlist2 = [1, 4, 7, 10]

merged = merge(waitlist1, waitlist2)

print("Merged Waitlist:", merged)