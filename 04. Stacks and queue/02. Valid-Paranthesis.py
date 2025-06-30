# step 1 : create a list for stack representation
# step 2 : add every open paranthesis into stack
# step 3 :  if there is any close parenthesis pop the stack ONLY IF :
#           1. the open paranthesis match with the closing paranthesis
#           2. else continue the iteration until the end
# step 4 : if stack is empty, then it is valid, return True
# step 5 : if stack is not empty, return false


def solve(s) -> bool:
    stack = []

    for paranthesis in s:
        try:
            if paranthesis == '[' or paranthesis == "{" or paranthesis == "(":
                stack.append(paranthesis)
            elif ((paranthesis == ']' and stack[-1] == '[') or (paranthesis == '}' and stack[-1] == '{') or (paranthesis == ')' and stack[-1] == '(')):
                stack.pop()
            elif ((paranthesis == ')' and stack[-1] != '(') or (paranthesis == '}' and stack[-1] != '{') or (paranthesis == ']' and stack[-1] != '[')):
                return False
        except IndexError:
            return False
    

    if len(stack) == 0:
        return True
    else:
        return False



def main():
    s = "(])"
    isValid = solve(s)
    print(isValid)

main()