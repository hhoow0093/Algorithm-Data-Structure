def summaryRanges(nums):
    result = []
    start = 0
    i  = 0
    while i < len(nums):
        while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
            i += 1
        if start == i:
            result.append(f"{nums[start]}")
            start = i + 1
        else:
            result.append(f"{nums[start]}->{nums[i]}")
            start = i + 1
        i += 1
    return result
            

def main():
    number = input("lists of number ',' seperator: ")
    number_string = number.replace(" ", "")
    number_array = number_string.split(",")
    number_array_int = list(map(int, number_array))
    output = summaryRanges(number_array_int)
    print(output) 


main()
