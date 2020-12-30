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
    
    def __str__(self):
        output = [self.val]
        queue = [self]
        children = 0
        
        while len(queue) != 0:
            if children == 0:
                if queue[0].left != None:
                    output.append(queue[0].left.val)
                    queue.append(queue[0].left)
                else:
                    output.append(None)
                children += 1
                    
            elif children == 1:
                if queue[0].right != None:
                    output.append(queue[0].right.val)
                    queue.append(queue[0].right)
                else:
                    output.append(None)
                queue.pop(0)
                children = 0
                
        while output[-1] == None:
            output.pop()
            
        return list.__str__(output)
    
    def listToBST(nums):
        """
        Convert a list of numbers to a Binary Search Tree.
        """
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
    
    def listToBinaryTree(nums):
        """
        Recover the list to a Binary Tree (not necessarily to be Binary Search Tree).
        """
        if len(nums) == 0:
            return None
        
        root = binaryTreeNode(nums[0])
        queue = [root]
        children = 0
        
        for i in range(1, len(nums)):
            if children == 2:
                queue.pop(0)
                children = 0
            
            if nums[i] == None:
                children += 1
                continue
                
            queue.append(binaryTreeNode(nums[i]))
            if children == 0:
                queue[0].left = queue[-1]
            else:
                queue[0].right = queue[-1]
                
            children += 1
                
        return root    
    
    def BSTToList(self):
        bst_list = [self.val]
        
        if self.left != None:
            bst_list.extend(self.left.BSTToList())
        if self.right != None:
            bst_list.extend(self.right.BSTToList())
            
        return bst_list
    
TreeNode = binaryTreeNode