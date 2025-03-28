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
    list_string_complement = list(string)
    for i in range(0, len(subsequence)):
        if subsequence[i] in list_string_complement:
            list_string_complement.remove(subsequence[i])

    # remove all char using list_string_complement variable    
    list_string_remove = list(string)
    for i in range(0, len(list_string_complement)):
        list_string_remove.remove(list_string_complement[i])
    
    string_result = "".join(list_string_remove)
    if(string_result != subsequence):
        print(string_result)
        print(subsequence)
        return False
    else:
        print(string_result)
        print(subsequence)
        return True



def main(subsequence, string):
    answer = solve(subsequence, string)
    print(answer)

main("", "bbaaaa")