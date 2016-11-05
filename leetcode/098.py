ass Solution(object):
    def isValidBST(self, root, min=float('-inf'), max=float('inf')):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
