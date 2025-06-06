ransomNote = "aa"
magazine = "ab"

def solve(ransomNote, magazine):
    dict = {}
    for i in range(0, len(magazine)):
        if magazine[i] not in dict:
            dict[magazine[i]] = 1
        else:
            dict[magazine[i]] += 1
    for i in range(0, len(ransomNote)):
        if ransomNote[i] not in dict or dict[ransomNote[i]] == 0:
            return False
        dict[ransomNote[i]] -= 1
        
    return True

def main():
    print(solve(ransomNote, magazine))

main()
