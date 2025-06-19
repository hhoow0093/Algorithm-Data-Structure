# step 1 : initialize left and right pointer 
# step 2 : check its current area
# step 3 : if current area is bigger than the max area, update its area
# step 4 : if height left is shorter move left, if height right is shorter, mover right
# step 5 : otherwise move between left or right if heighr is the same

def maxArea(height):
    area_max = float('-inf')
    left = 0
    right = len(height) - 1
    
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        if current_area > area_max :
            area_max = current_area
        
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
    
    return area_max




def main():
    solution = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(solution)

main()