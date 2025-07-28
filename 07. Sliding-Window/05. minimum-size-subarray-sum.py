# step 1 : initialize left pointer, total, and min window length
# step 2 : iterate right pointer till the end of array
# step 3 : keep adding total numbers from right pointer
# step 4 : while total >= target, we can start minimizing the window
# step 5 : return thw window width

def main(target = 7, nums = [2, 3, 1, 2, 4, 3]):
    left = 0
    total = 0
    window_length = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            window_length = min(window_length, right - left + 1)
            total -= nums[left]
            left += 1
    if window_length == float('inf'):
        print(0)
    print(window_length)

main()

