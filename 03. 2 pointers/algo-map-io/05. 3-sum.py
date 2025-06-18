nums = [-1,0,1,2,-1,-4]
solution = []

for i in range(0, len(nums)):
    current = nums[i]
    left = i + 1
    right = len(nums) - 1
    while left < right:
        if current + nums[left] + nums[right] == 0:
            solution.append([current, nums[left], nums[right]])
        right -= 1
    
    

print(solution)

