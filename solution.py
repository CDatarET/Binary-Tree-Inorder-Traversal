# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, arr):
        if(root == None):
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        self.inorder(root, arr)
        return(arr)
