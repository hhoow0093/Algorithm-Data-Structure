def convert(character):
    if character == 'I':
        return 1
    elif character == 'V':
        return 5
    elif character == 'X':
        return 10
    elif character == 'L':
        return 50
    elif character == 'C':
        return 100
    elif character == 'D':
        return 500
    elif character == 'M':
        return 1000
    else:
        return 0

def solve(roman_string):
    index = 0
    length = len(roman_string)
    result = 0
    while index < length:
        if  index + 1 < length and convert(roman_string[index]) < convert(roman_string[index + 1]):
            result += convert(roman_string[index + 1]) - convert(roman_string[index])
            index += 2
        else:
            result += convert(roman_string[index])
            index += 1
    return result


def main():
    Roman = "LVIII"
    result = solve(Roman)
    print(result)

main()
