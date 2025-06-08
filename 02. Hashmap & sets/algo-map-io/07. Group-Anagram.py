# step 1 : create a dictionary and sort each string to create grouping
# step 2 : add each string to each dedicated groupping based from step 1
# step 3 : if a string exists in a dictionary, append the string into the existing group
# step 4 : if do not exist, create new key from the dictionary

def solve(array):
    dict = {}
    for i in range(0, len(array)):
        if ''.join(sorted(array[i])) not in dict:
            dict[''.join(sorted(array[i]))] = list()
            dict[''.join(sorted(array[i]))].append(array[i])
        else:
            dict[''.join(sorted(array[i]))].append(array[i])
    result = []
    values = list(dict.values())
    for i in range(0, len(values)):
        result.append(values[i])
    return values 


def main():
    result = solve(["eat","tea","tan","ate","nat","bat"])
    print(result)

main()
