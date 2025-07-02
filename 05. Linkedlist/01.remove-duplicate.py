# step 1 : initalize placeholder variable for storing all the linked list order value.
# step 2 : iterate the head until head.next is None
# step 4 : if a duplicate is found between head and head.next.value, update head.next to head.next.next
# step 5 : else, keep mobing head 
# step 6 : once iteration is done, retun the placeholder variable

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to a list for easy testing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,1,2] -> [1,2]
    test1 = create_linked_list([1, 1, 2])
    result1 = solution.deleteDuplicates(test1)
    print(f"Test 1: {linked_list_to_list(result1)}")  # Expected: [1, 2]
    
    # Test case 2: [1,1,2,3,3] -> [1,2,3]
    test2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = solution.deleteDuplicates(test2)
    print(f"Test 2: {linked_list_to_list(result2)}")  # Expected: [1, 2, 3]
    
    # Test case 3: Empty list
    test3 = create_linked_list([])
    result3 = solution.deleteDuplicates(test3)
    print(f"Test 3: {linked_list_to_list(result3)}")  # Expected: []
    
    # Test case 4: Single element
    test4 = create_linked_list([1])
    result4 = solution.deleteDuplicates(test4)
    print(f"Test 4: {linked_list_to_list(result4)}")  # Expected: [1]
    
    # Test case 5: All duplicates [1,1,1,1] -> [1]
    test5 = create_linked_list([1, 1, 1, 1])
    result5 = solution.deleteDuplicates(test5)
    print(f"Test 5: {linked_list_to_list(result5)}")  # Expected: [1]

