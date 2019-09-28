    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int"""
        stack = []
        
        def postOrderTraversal(root):
            if root:
                if L <= root.val <= R:
                    stack.append(root.val)
                postOrderTraversal(root.left)
                postOrderTraversal(root.right)
            
        postOrderTraversal(root)
        return sum(stack)  
