# step 1 : initialize n1 and n2 as length from s1 and s2
# step 2 : if substring is longer than original string, immediately return false
# step 3 : initialize an array of n1_count and n2_count to keep track of number of occurences from a string using ASCII code
# step 4 : iterate until n1 to check the arrau content from n1_count and n2_count. if iteration is done and array content the same, return true immediatelt
# step 5 : iterate from n1 to n2 since s1 is already traversed. start traversing and only update n2_count.
# step 6 : keep adding new letters and deleting letters from the very first traversed letter from s2 by s2[i - n1]
# step 7 : if n1_count the same as n2_count from n1 to n2 iteration, return true. otherwise return false afterwards.  

def main(s1 = "ab", s2= "eidbaooo"):
    n1 = len(s1)
    n2 = len(s2)

    if n1 > n2 :
        print(False)
        return
    
    n1_count = [0] * 26
    n2_count = [0] * 26

    for i in range(n1):
        n1_count[ord(s1[i]) - 97] += 1
        n2_count[ord(s2[i]) - 97] += 1
    
    if n2_count == n1_count:
        print(True)
        return
    
    for i in range(n1, n2):
        n2_count[ord(s2[i]) - 97] += 1
        n2_count[ord(s2[i - len(s1)]) - 97] -= 1
        if n2_count == n1_count:
            print(True)
            return
    
    print(False)
    return

main()


# original bruteforce solution
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         length = len(s1)
#         dict1 = {}
        
#         for i in range(len(s1)):
#             if s1[i] not in dict1:
#                 dict1[s1[i]] = 1
#             else:
#                 dict1[s1[i]] += 1

#         for substring in range (0, len(s2) - len(s1) + 1, 1):
#             dict2 = {}
#             curr_string = s2[substring : substring + length]
#             for j in range(len(curr_string)):
#                 if curr_string[j] not in dict2:
#                     dict2[curr_string[j]] = 1
#                 else:
#                     dict2[curr_string[j]] += 1

#             if dict1 == dict2:
#                 return True
        
#         return False



