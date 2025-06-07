import math

def solve(string):
    dict = {
        "b" : 0,
        "a" : 0,
        "l" : 0,
        "o" : 0,
        "n" : 0
    }
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            continue
    dict['o'] = math.floor(dict['o'] / 2)
    dict['l'] = math.floor(dict['l'] / 2)
    values = list(dict.values())

    min = float('inf')
    for i in range(0, len(values), 1):
        if(min > values[i]):
            min = values[i]
    return min



def main():
    string = "loonbalxballpoon"
    result = solve(string)
    print(result)

main()