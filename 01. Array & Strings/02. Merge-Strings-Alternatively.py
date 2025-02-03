"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string. 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""

def mergeAlternately(word1: str, word2: str) -> str:
    string_primary_length = len(word1)
    string_secondary_length = len(word2)

    longer = ""
    self = ""

    if(string_primary_length != string_secondary_length):
        if(string_primary_length > string_secondary_length):
            longer = word1
        else:
            longer = word2

    else:
        # jika nilai panjang string sama, harusnya gak ngaruh
        longer = word1

    for i in range(0, len(longer)):
        if(i > len(word1) - 1):
            self += ""
        else:
            self += word1[i]

        if(i > len(word2) - 1):
            self += ""
        else:
            self += word2[i]
    
    return self



def main():
    primary_string = input("enter your first string: ")
    secondary_string = input("enter your secondary string: ")
    result = mergeAlternately(primary_string, secondary_string)
    print(result)

main()

"""
solusi lain:
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0 
        #strings are immutable in Python 
        mergedString = []


        while idx<len(word1) and idx<len(word2):
            mergedString+=word1[idx]
            mergedString+=word2[idx]
            idx+=1

        if idx<len(word1):
            mergedString+=word1[idx:]
        elif idx<len(word2):
            mergedString+=word2[idx:]

        return "".join(mergedString)
"""