class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        preorder_left = preorder[1:1+root_index]
        preorder_right = preorder[1+root_index:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
