def solve(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    
    sort_result = sorted(result)

    return sort_result



def main():
    result = solve([-4,-1,0,3,10])
    print(result)


main()