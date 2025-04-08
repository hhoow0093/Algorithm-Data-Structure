def solve(subsequence, string):
    string_complement = list(string) 
    # remove subsequence from string
    for i in range(0, len(subsequence)):
        if subsequence[i] in string_complement:
            string_complement.remove(subsequence[i])
    
    # remove item in string complement to match with subsequence
    string_check = list(string)
    for item in string_complement:
        string_check.remove(item)

    # check if string_check is the same as list(subsequence)
    if string_check == list(subsequence):
        return True
    else:
        return False

        
def main():
    subsequence = "axc"
    string = "ahbgdc"
    result = solve(subsequence, string)
    print(result)
main()