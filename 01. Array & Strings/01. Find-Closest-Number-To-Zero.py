# My Solution
def findClosestNumber(nums: list[int]):
    # meyimpan nomor pada index ke 0
    closest = nums[0]
    # sebagai pembanding pada seluruh isi array nums
    test_i = 0
    for i in range(1, len(nums)):
        # biar nilai selalu positif
        different_closest = abs(closest) - 0
        different_in_i = abs(nums[i]) - 0
        test_i = nums[i]
        # siapa yang paling mendekati 0, maka dia dijadikan paling dekat 
        if(different_closest > different_in_i ):
            closest = nums[i]
        elif(different_closest == different_in_i):
            if(closest < test_i):
                closest = test_i
        else:
            continue

    return closest


def main():
    nums_array = []
    nums = input("give me lists of number: ")
    strings_in_number = nums.split(",")

    for number in strings_in_number:
        nums_array.append(int(number))

    result = findClosestNumber(nums_array)
    print(result)


main()

# Deepseek Solution
# def findClosestNumber(nums: list[int]) -> int:
#     closest = nums[0]
#     for num in nums[1:]:
#         current_abs = abs(num)
#         closest_abs = abs(closest)
#         if current_abs < closest_abs:
#             closest = num
#         elif current_abs == closest_abs and num > closest:
#             closest = num
#     return closest

# def main():
#     nums = [int(num) for num in input("Enter a list of numbers (comma-separated): ").split(",")]
#     result = findClosestNumber(nums)
#     print(result)

# main()