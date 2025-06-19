# step 1 : initialize left and right pointer
# step 2 : keep track of its max height from pointer right and pointer left
# step 3 : if current left pointer height is lesser than max height from left pointer, then water can be added. the same applies with right pointer
# step 4 : if step 3 doesnt work, update its max height from left pointer or max height from right pointer
# step 5 : update its left and right pointer based from the shortest length. if the same, choose 1 between left or right 


def solve(height):
    water = 0
    left = 0 
    right = len(height) - 1
    leftMAX = height[left]
    rightMAX = height[right]

    while left < right:
        if leftMAX > height[left]:
            water += leftMAX - height[left]
        elif rightMAX > height[right]:
            water += rightMAX - height[right]

        if height[left] > leftMAX:
            leftMAX = height[left]
        elif height[right] > rightMAX:
            rightMAX = height[right]
        
        if height[left] < height[right]:
            left +=1
        elif height[left] > height[right]:
            right -= 1
        else:
            left +=1

    return water



def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    water = solve(height)
    print(water)

main()