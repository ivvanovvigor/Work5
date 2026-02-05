class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Якщо обидва вузли None — вони однакові
        if not p and not q:
            return True
        # Якщо один з них None або значення різні — вони різні
        if not p or not q or p.val != q.val:
            return False
        
        # Рекурсивно перевіряємо ліві та праві гілки
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# --- ПРИКЛАДИ ТЕСТУВАННЯ ---

# Приклад 1: Однакові дерева
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Приклад 2: Різна структура (одне дерево зміщене вправо)
p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))

sol = Solution()
print(f"Результат 1: {sol.isSameTree(p1, q1)}") # True
print(f"Результат 2: {sol.isSameTree(p2, q2)}") # False