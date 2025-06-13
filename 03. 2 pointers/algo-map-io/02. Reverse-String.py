# step 1: uses left and right index to modify list
# keep swapping ledt. increment left, decrement right until left > right
def solve(s):
    left = 0
    right = len(s) - 1
    while(left < right):
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s



def main():
    result = solve(["h","e","l","l","o"])
    print(result)

main()