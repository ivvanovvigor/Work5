from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        
        while stack or current:
            # 1. Йдемо до найлівішого вузла
            while current:
                stack.append(current)
                current = current.left
            
            # 2. Обробляємо вузол (це і є порядок зростання)
            current = stack.pop()
            k -= 1
            
            if k == 0:
                return current.val
            
            # 3. Переходимо до правої гілки
            current = current.right

# --- ДОПОМІЖНІ ФУНКЦІЇ ДЛЯ ТЕСТУВАННЯ ---

def build_tree(nodes):
    if not nodes: return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# --- ТЕСТУВАННЯ ---

sol = Solution()

# Приклад 1
# Дерево: [3,1,4,null,2], k = 1
root1 = build_tree([3, 1, 4, None, 2])
print(f"Приклад 1 | Результат: {sol.kthSmallest(root1, 1)}") # Вихід: 1

# Приклад 2
# Дерево: [5,3,6,2,4,null,null,1], k = 3
root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
print(f"Приклад 2 | Результат: {sol.kthSmallest(root2, 3)}") # Вихід: 3