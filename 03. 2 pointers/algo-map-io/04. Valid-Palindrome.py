# step 1 : convert string to lowercase
# step 2 : if a character is not alpha numeric, change the pointer left or right by 1 with continue statement
# step 3 : if a character from left and right is different, return false
# step 4 : is left < right is false, return true

def solve(string):
    s = string.lower()

    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        elif s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
        
    return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(solve(s))

main()
