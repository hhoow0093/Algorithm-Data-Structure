# step 1 : initialize 2 stacks. 1 is for storing every number, and the other one is for storing minimum number
# step 2 : when pushing, add the numbers in the first stack, and then check if the min stack is empy. if empty push the number into the 2nd stack
# step 3 : when pushing, always append the minimum numbers on the minimum stack by checking the current value and the minimum top stack in the 2nd stack
# step 4 : when popping, remove a number from the first and second stack
# step 5 : if top is called, return the latest number stack in the first stack
# step 6 : if getminimum is called, return the latest number stack in the second stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        try:
            if(self.min[-1] > val):
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
        except IndexError:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
