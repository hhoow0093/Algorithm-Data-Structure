def sort(given_array):
    sorted_array = sorted(given_array, key = lambda x: x[0])
    return sorted_array

def solve(sorted_array):
    merged_array = []
    prev = sorted_array[0]
    for current in sorted_array[1:]:
        # overlapping
        if prev[1] >= current[0]:
            prev[1] = max(prev[1], current[1])
        # non-overlapping
        else:
            merged_array.append(prev)
            prev = current
            
    merged_array.append(prev)
    return merged_array

def main():
    given_array = [[1, 4], [2, 3]]
    sorted_array = sort(given_array)
    result = solve(sorted_array)
    print(result)

main()

