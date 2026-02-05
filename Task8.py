from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        # Список для зберігання (col, row, value)
        node_list = []
        
        # Використовуємо BFS для обходу (можна і DFS)
        # Черга зберігає пари (вузол, рядок, стовпець)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            if node:
                node_list.append((col, row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Сортуємо: 
        # 1. За стовпцем (col)
        # 2. За рядком (row)
        # 3. За значенням (val)
        node_list.sort()
        
        # Групуємо результат за стовпцями
        res = defaultdict(list)
        for col, row, val in node_list:
            res[col].append(val)
            
        # Повертаємо значення, відсортовані за ключами стовпців
        return [res[c] for c in sorted(res.keys())]

# --- ТЕСТУВАННЯ ---

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

sol = Solution()

# Приклад 1
root1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Приклад 1: {sol.verticalTraversal(root1)}") 
# Вихід: [[9], [3, 15], [20], [7]]

# Приклад 2
root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(f"Приклад 2: {sol.verticalTraversal(root2)}")
# Вихід: [[4], [2], [1, 5, 6], [3], [7]]