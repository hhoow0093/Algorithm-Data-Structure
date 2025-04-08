def solve(array):
    result = []
    index = 0
    start = 0
    length = len(array)
    while index < length:
        if index + 1 < length and array[index] + 1 == array[index + 1]:
            index +=1
        elif index == start:
            result.append(f"{array[index]}")
            index += 1
            start += 1
        else:
            result.append(f"{array[start]}->{array[index]}")
            start = index + 1
            index += 1
    return result

def main():
    array = [0, 2, 3, 4, 6, 8, 9]
    result = solve(array)
    print(result)

main()