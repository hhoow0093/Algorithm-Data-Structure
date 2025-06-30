# step 1 : create a ist for stack representation
# step 2 : if it is a number keep adding the number into the stack
# step 3 : if it is an operator pop 2 numbers from the stack and push the new value number based from the given operator
# step 4 : keep evaluating until the stack is empty

def is_valid_number(token):
    try:
        int(token)
        return True
    except ValueError:
        return False

def solve(tokens) -> int:
    stack = []
    for token in tokens:
        if is_valid_number(token):
            stack.append(int(token))
        elif token == "+":
            firstNum = stack[-1]
            secondNum = stack[-2]
            stack.pop()
            stack.pop()
            addNum = secondNum+ firstNum
            stack.append(addNum)
        elif token == "-":
            firstNum = stack[-1]
            secondNum = stack[-2]
            stack.pop()
            stack.pop()
            addNum = secondNum - firstNum
            stack.append(addNum)
        elif token == "*":
            firstNum = stack[-1]
            secondNum = stack[-2]
            stack.pop()
            stack.pop()
            addNum = secondNum * firstNum
            stack.append(addNum)
        elif token == "/":
            firstNum = stack[-1]
            secondNum = stack[-2]
            stack.pop()
            stack.pop()
            addNum = int(secondNum / firstNum)
            stack.append(addNum)
    return stack[0]



def main():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    score = solve(tokens)
    print(score)

main()