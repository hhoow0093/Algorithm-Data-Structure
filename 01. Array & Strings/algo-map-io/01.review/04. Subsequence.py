# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

# string ="hola"
# print(string.find('b'))
def solve(subsequence, string):
    # convert string to lists of char to find all char that does not represent subsequence
    # subsequence abc
    # string ahbgdc

    list_string_complement = list(string)
    # list_string_complement = [a, h, b, g, d, c]
    for i in range(0, len(subsequence)):
        # remove a b c from [a, h, b, g, d, c]
        if subsequence[i] in list_string_complement:
            list_string_complement.remove(subsequence[i])
    # list_string_complement = [h, g, d]

    # remove all char using list_string_complement variable    
    list_string_remove = list(string)
    # list_string_remove = [a, h, b, g, d, c]
    for i in range(0, len(list_string_complement)):
        # remove [h, g, d] from [a, h, b, g, d, c]
        list_string_remove.remove(list_string_complement[i])
    # list_string_remove = [a, b, c]

    string_result = "".join(list_string_remove)
    # string_result = "abc"

    if(string_result != subsequence):
        print(string_result)
        print(subsequence)
        return False
    else:
        # abc == abc
        print(string_result)
        print(subsequence)
        return True



def main(subsequence, string):
    answer = solve(subsequence, string)
    print(answer)

main("", "bbaaaa")