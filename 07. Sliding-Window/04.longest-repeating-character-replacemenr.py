# step 1 : initialize left pointer as 0, nums of k used, window_width, and dict to keep track or maximum frequuency from string
# step 2 : iterate right pointer from the very first item to end of array.
# step 3 : for every iteration, update max_freq and add every char to dict
# step 4 : while right - left + 1 - max_freq > k, keep moving left pointer and update dict. 
# step 5 : after iteration ends, return window_width

def solve(s, k):
    window_width = 0
    mydict = {}
    max_freq = 0
    left = 0
    for right in range(len(s)):
        mydict[s[right]] = mydict.get(s[right], 0) + 1
        max_freq = max(max_freq, mydict[s[right]])
        while right - left + 1 - max_freq > k:
            mydict[s[left]] -= 1
            left += 1
        window_width = max(window_width, right - left + 1)
    return window_width

def main():
    result = solve("AABABBA", 1)
    print(result)

main()