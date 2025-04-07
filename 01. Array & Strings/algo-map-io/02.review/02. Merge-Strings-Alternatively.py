def solve(word1, word2):
    if len(word1) > len(word2):
        longer_string = word1
    else:
        longer_string = word2
    
    result = ""

    for i in range(0, len(longer_string)):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]
    
    return result




def main():
    word1 = "abcd"
    word2 = "pq"
    merged_string = solve(word1, word2)
    print(merged_string)    
main()
