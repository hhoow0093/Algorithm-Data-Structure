# step 1 : Iterate all the temperature list.
# step 2 : for each temperature, create a new list representing a queue from the day after the current day.
# step 3 : create a counter variable thet counts the number of dequeue until the selected day is warmer than the current day.
# step 4 : if queue is empty, then immediately append 0 to indicate no temperature is warmer than the current day


# queue implementation
# def solve(temperatures):
#     answer = []
#     for i, temperature in enumerate(temperatures):
#         queue_next_day_temperature = temperatures[i + 1:]
#         counter = 0
#         while len(queue_next_day_temperature) != 0:
#             if temperature < queue_next_day_temperature[0]:
#                 answer.append(counter + 1)
#                 break
#             elif temperature > queue_next_day_temperature[0]:
#                 counter +=1
#                 queue_next_day_temperature.pop(0)
        
#         if len(queue_next_day_temperature) == 0:
#             answer.append(0)
#     return answer

# step 1 : create a stack for storing tuples. and add the first index to the stack 
# step 2 : initialize answer list to store the possible day thay may be warmer than the selected day
# step 3 : check if the current temperatire us bigger then the previous temperature from the latest stack
# step 4 : if it is bigger, pop all possible tuples from stack until current temperature is lesser than the temparature on stack or empty
# step 5 : after popping, add the current temoerature to the stack


# monotonous stack implementation
def solve(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for index, temperature in enumerate(temperatures):
        if index == 0:
            stack.append((temperature, index))
            continue
        try:
            while temperature > stack[-1][0]:
                prev_index = stack[-1][1]
                update_days = index - prev_index
                answer[prev_index] = update_days
                stack.pop()
            stack.append((temperature, index))
        except IndexError:
            stack.append((temperature, index))
            continue

    return answer


def main():
    temperatures = [73,74,75,71,69,72,76,73]
    result = solve(temperatures)
    print(result)

main()
