# step 1 : create a new list for storing all the scores by using stack implementation
# step 2 : iterate each operation from the given array and update its scroe accordingly based from the operation rules
# step 3 : count the total from the new list

def is_valid_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def solve(ops):
    score = []
    for i in range(0, len(ops)):
        if is_valid_integer(ops[i]):
            score.append(int(ops[i]))
            print(score)
        elif ops[i] == "D":
            score.append(score[len(score) - 1] * 2)
            print(score)
        elif ops[i] == "C":
            score.pop()
            print(score)
        elif ops[i] == "+":
            score.append(score[len(score) - 1] + score[len(score) - 2])
            print(score)
    
    print(score)
    return sum(score)


def main():
    ops = ["5","-2","4","C","D","9","+","+"]
    score = solve(ops)
    print(score)

main()