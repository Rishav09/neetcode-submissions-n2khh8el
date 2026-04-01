class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return []
            
            left = inorder(node.left)
            current = [node.val]
            right = inorder(node.right)
            
            return left + current + right

        sorted_nodes = inorder(root)
        return sorted_nodes[k - 1]
