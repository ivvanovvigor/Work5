class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def isMirror(t1, t2):
            # Якщо обидва порожні — симетрично
            if not t1 and not t2:
                return True
            # Якщо один порожній або значення різні — не симетрично
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # Порівнюємо ЗОВНІШНІ гілки (ліва-лівого та права-правого) 
            # та ВНУТРІШНІ гілки (права-лівого та ліва-правого)
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)

# --- ПРИКЛАДИ ---
# Приклад 1: Симетричне [1,2,2,3,4,4,3]
root1 = TreeNode(1, 
                 TreeNode(2, TreeNode(3), TreeNode(4)), 
                 TreeNode(2, TreeNode(4), TreeNode(3)))

sol = Solution()
print(f"Приклад 1: {sol.isSymmetric(root1)}") # True