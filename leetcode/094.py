class Solution(object):
    def inorderTraversal(self, root):
        result = []
        n = root
        s = []
        while len(s) or n:
            if n is not None:
                s.append(n)
                n = n.left
            else:
                n = s.pop()
                result.append(n.val)
                n = n.right
        return result

