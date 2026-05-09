# Q7. Write a Python program to implement a binary search algorithm.

def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2

        # element found
        if arr[mid] == target:
            return mid
        # search in right helf
        elif arr[mid] < target:
            left = mid + 1
        # search in left half
        else:
            right = mid - 1
    return -1


numbers = sorted(list(map(int, input("Please enter the numbers: ").split())))

target = int(input("Please enter a number: "))

result = binary_search(numbers , target)

if result != -1:
    print("Element found at index: ", result)
else :
    print("Element not found")

