# step 1 : initialize left and right pointer at the very start of the array
# step 2 : initialize window_width as 0, and nums of flip as 0
# step 3 : iterate right pointer from start to end of array
# step 4 : if current right pointer is pointing at 0, increase nums of flip by 1. and keep calculating width by right - left + 1
# step 5 : while nums of flip is bigger than k, keep moving left pointer if it was 1. if it was 0, move left by 1 and decrease nums of flip ny 1
# step 6 : return window_width

def solve(nums: list[int], k: int) -> int:
    window_width = 0
    flip = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            flip += 1
        while flip > k:
            if nums[left] == 0:
                flip -= 1
            left += 1
        width = right - left + 1
        window_width = max(window_width, width)
    return window_width


def main():
    result = solve([1,1,1,0,0,0,1,1,1,1,0], k = 2)
    print(result)

main()
