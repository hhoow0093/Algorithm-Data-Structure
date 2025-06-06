def solve(s, t):
    answer = True
    dict = {}

    for i in range(0, len(s)):
        if s[i] not in dict:
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1

    for i in range(0, len(t)):
        if t[i] not in dict:
            answer = False
        else:
            dict[t[i]] -= 1

    values = list(dict.values())

    for i in range(0, len(values)):
        if values[i] != 0:
            answer = False
    return answer

def main():
    s = "rat"
    t = "car"
    print(solve(s, t))

main()