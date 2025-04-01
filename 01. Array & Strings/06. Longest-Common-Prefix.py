def solve():
    arr = ["hh", "hhaaha", "hahahaha"]
    shortest = arr[0]
    for i in range(len(arr) - 1):
        if(len(shortest) > len(arr[i + 1])):
            shortest = arr[i + 1]

    for j in range(0, len(shortest), 1):
        for string in arr:
            if string[j] != shortest[j]:
                return shortest[:j]
    return shortest
            
def main():
    common_prefix = solve()
    print(common_prefix)

main()
