# step 1 : initalize placeholder variable for storing all the linked list order value.
# step 2 : iterate the head until head.next is None
# step 4 : if a duplicate is found between head and head.next.value, update head.next to head.next.next
# step 5 : else, keep mobing head 
# step 6 : once iteration is done, retun the placeholder variable
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res
        
