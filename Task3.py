from collections import deque

# Клас вузла бінарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Функція для перетворення масиву в дерево (для тестів)
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

# Функція для перетворення дерева в масив (для виводу результату)
def tree_to_list(root):
    if not root: return []
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # Видаляємо зайві None в кінці
    while res and res[-1] is None: res.pop()
    return res

# --- ОСНОВНА РЕАЛІЗАЦІЯ ---

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Використовуємо чергу (BFS)
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            
            # Обмін місцями лівого і правого нащадків
            current.left, current.right = current.right, current.left
            
            # Додаємо дітей у чергу
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
            
        return root

# --- ТЕСТУВАННЯ ---

sol = Solution()

# Приклад 1
input1 = [4, 2, 7, 1, 3, 6, 9]
tree1 = build_tree(input1)
inverted1 = sol.invertTree(tree1)
print(f"Приклад 1 | Вхід: {input1} | Вихід: {tree_to_list(inverted1)}")

# Приклад 2
input2 = [2, 1, 3]
tree2 = build_tree(input2)
inverted2 = sol.invertTree(tree2)
print(f"Приклад 2 | Вхід: {input2} | Вихід: {tree_to_list(inverted2)}")

# Приклад 3
input3 = []
tree3 = build_tree(input3)
inverted3 = sol.invertTree(tree3)
print(f"Приклад 3 | Вхід: {input3} | Вихід: {tree_to_list(inverted3)}")