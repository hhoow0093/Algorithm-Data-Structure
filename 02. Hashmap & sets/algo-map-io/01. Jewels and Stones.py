dictionary  = {}
jewels = "z"
stones = "ZZ"

for i in range(0, len(stones)):
    if stones[i] not in dictionary:
        dictionary[stones[i]] = 1
    else:
        dictionary[stones[i]] += 1

print(dictionary)
result = 0

for i in range(0, len(jewels)):
    if jewels[i] not in dictionary:
        continue
    result += dictionary[jewels[i]]
print(result)

