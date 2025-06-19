# step 1 : iterate all numbers
# step 2 : check if the current index is the same number as the previous index. if the sa,e, skip the iteration
# step 3 : assign j and k. j as i + 1 and k len(arr) - 1
# step 4 : use 2 pointer approach. if total is lesser than 0, add j pointer by 1. otherwise subtract k pointer by 1
# step 5 : if total is 0, add the combination to result variable and update j pointer by 1. 
# step 6 : if updated j pointer number is the same number as the previous j pointer number at a certain index. keep updateing j pointer

def solve(nums):
    result = []
    nums.sort()
    for i in range(0, len(nums)):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j  += 1
                while nums[j] == nums[j - 1] and j < k:
                    j +=1
        
    return result


def main():
    nums  = [-1,0,1,2,-1,-4]
    result = solve(nums)
    print(result)

main()
