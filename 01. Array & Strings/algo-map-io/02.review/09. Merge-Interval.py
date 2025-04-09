def solve(intervals):
    result = []
    sorted_intervals = sorted(intervals, key= lambda x : x[0])
    prev = sorted_intervals[0]
    for i in range(1, len(sorted_intervals)):
        # overlapping 
        if prev[1] > sorted_intervals[i][0]:
            prev[1] = max(prev[1], sorted_intervals[i][1])
        # non overlapping
        else:
            result.append(prev)
            prev = sorted_intervals[i]
    
    result.append(prev)
    return result





def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merged = solve(intervals)
    print(merged)

main()