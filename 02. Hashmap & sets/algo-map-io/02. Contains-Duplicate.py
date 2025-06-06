nums = [1, 2, 3, 4]

# def solve(nums):
#     answer = False
#     dict = {}
#     for i in range(0, len(nums)):
#         if nums[i] not in dict:
#             dict[nums[i]] = 1
#         else:
#             dict[nums[i]] += 1
    
#     keys = dict.keys()
#     keys_list = list(keys)
#     for i in range(0 , len(keys_list)):
#         if(dict[keys_list[i]] > 1):
#             answer = True
#     return answer

def solve(nums):
    dict = {}
    for i in range(0, len(nums)):
        if nums[i] in dict:
            return True
        else:
            dict[nums[i]] = 1
    return False



def main():
    print(solve(nums))

main()