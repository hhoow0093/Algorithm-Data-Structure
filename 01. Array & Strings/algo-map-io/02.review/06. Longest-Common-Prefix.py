def solve(strs):
    # find the shortest list of strings
    shortest_string = strs[0]
    for i in range(1, len(strs)):
        if len(shortest_string) > len(strs[i]):
            shortest_string = strs[i]
    # find common prefix
    for i in range(0, len(shortest_string)):
        for str in strs:
            if str[i] != shortest_string[i]:
                if i == 0:
                    return ""
                else:
                    return shortest_string[:i]
    return shortest_string


    

def main():
    strs = ["dog", "racecar", "car"]
    prefix = solve(strs)
    print(prefix)
main()