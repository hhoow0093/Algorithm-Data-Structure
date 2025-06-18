# uses left and right index to keep track of the smallest and larger number.
# if sum is bigger, decrement right by 1. if sum is smaller increment left by 1
# repeat until sum is equal to target

def twoSum(ListNumber, target):
    right = len(ListNumber) - 1
    left = 0
    while left < right :
        if ListNumber[left] + ListNumber[right] > target:
            right -= 1
        elif ListNumber[left] + ListNumber[right] < target:
            left += 1
        elif ListNumber[left] +ListNumber[right] == target:
            return [ListNumber[left], ListNumber[right]]
    
    return [-1, -1]

def main():
    arr = [2, 7, 11, 15]
    result = twoSum(arr, 9)
    print(result)

main()
