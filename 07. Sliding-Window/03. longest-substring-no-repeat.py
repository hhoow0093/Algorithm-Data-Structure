# step 1 : initialize left as 0 and windw_width as 0
# step 2 : use set() and store it in char_set to keep track of duplicates
# step 3 : iterate right pointer until len(s) - 1
# step 4 : while right pointer s is present in set, remove the set from left pointer, increment left pointer
# step 5 : add the s from right pointer to the set, calculate the width and compute the max
# step 6 : return the max

def solve(s):
    left = 0
    window_width = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        char_set.add(s[right])
        width = right - left + 1
        window_width = max(window_width, width)
    return window_width




def main():
    result = solve("abcabcbb")
    print(result)

main()
