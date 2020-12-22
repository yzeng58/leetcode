# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        current = self
        output = "[" + str(current.val)
        current = current.next
        
        while current != None:
            output += "," + str(current.val)
            current = current.next
            
        output += "]"
        return output
    
    def __str__(self):
        return self.__repr__()
    
def linkedList(lists):
    """
    Generate a linked list.
    """
    prehead = ListNode(-1)

    prev = prehead
    for item in lists:
        prev.next = ListNode(item)
        prev = prev.next

    return prehead.next
