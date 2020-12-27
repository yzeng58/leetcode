from typing import List
from time import time
from collections import *

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

from graphviz import Graph, Digraph
class binaryTreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val
        
    def to_graphviz(self, g = None):
        if g == None:
            g = Digraph()
            
        # draw self
        g.node(repr(self.val))
    
        for label, child in [("0", self.left), ("1", self.right)]:
            if child != None:
                # draw child, recursively
                child.to_graphviz(g)
                
                # draw edge from self to child
                g.edge(repr(self.val), repr(child.val))
        return g
    
    def _repr_svg_(self):
        return self.to_graphviz()._repr_svg_()
    
    def listToTree(nums):
        root = None
        
        for num in nums:
            if root == None:
                root = binaryTreeNode(num)
                continue
            
            current = root
            while current != None:
                if current.val > num:
                    if current.left == None:
                        current.left = binaryTreeNode(num)
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = binaryTreeNode(num)
                        break
                    else:
                        current = current.right
                        
        return root
    
    def sort(self): 
        nums = []
        current = self
        
        if current.left != None:
            nums += current.left.sort()
        
        nums.append(current.val)
            
        if current.right != None:
            nums += current.right.sort()
            
        return nums
    
def linkedList(lists):
    """
    Generate a linked list through a lists.
    """
    prehead = ListNode(-1)

    prev = prehead
    for item in lists:
        prev.next = ListNode(item)
        prev = prev.next

    return prehead.next

def test(inputs, func):
    """
    Tests whether the given function works correctly via printing
    the output of the function given the arguments.
    
    Parameters:
    -----------
    inputs: a list of inputs/arguments. e.g. [[*args1], [*args2]]
    func: function
    """
    start = time()
    for args in inputs:
        output = ""
        for arg in args:
            output += str(arg) + " "
        print(output + ": " + str(func(*args)))
        
    print("Time elapsed: %.5f seconds" % (time()-start))
