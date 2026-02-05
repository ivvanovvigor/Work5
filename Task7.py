class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        
        def dfs(node):
            if not node:
                # Порожній вузол вважаємо "охопленим" (стан 2), 
                # щоб не ставити камер на листя.
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 1. Якщо хоча б одна дитина не охоплена, ми ПОВИННІ поставити камеру тут.
            if left == 0 or right == 0:
                self.cameras += 1
                return 1 # Позначаємо цей вузол як такий, де є камера
            
            # 2. Якщо хоча б одна дитина має камеру, цей вузол тепер охоплений.
            if left == 1 or right == 1:
                return 2
            
            # 3. В інших випадках (діти охоплені іншими камерами), 
            # цей вузол залишається "не охопленим" і чекає допомоги від свого батька.
            return 0
        
        # Якщо корінь сам залишився без нагляду, ставимо на нього камеру.
        if dfs(root) == 0:
            self.cameras += 1
            
        return self.cameras

# --- ТЕСТУВАННЯ ---

# Приклад 1: [0, 0, None, 0, 0]
root1 = TreeNode(0)
root1.left = TreeNode(0)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(0)

sol = Solution()
print(f"Приклад 1 | Мінімально камер: {sol.minCameraCover(root1)}") # Вихід: 1

# Приклад 2: [0, 0, None, 0, None, 0, None, None, 0]
root2 = TreeNode(0)
root2.left = TreeNode(0)
root2.left.left = TreeNode(0)
root2.left.left.left = TreeNode(0)
root2.left.left.left.right = TreeNode(0)

print(f"Приклад 2 | Мінімально камер: {sol.minCameraCover(root2)}") # Вихід: 2