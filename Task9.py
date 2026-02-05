class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # 1. Рахуємо глибину (кількість тире)
            level = 0
            while i < n and traversal[i] == '-':
                level += 1
                i += 1
            
            # 2. Рахуємо значення вузла (може бути багатоцифровим)
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            new_node = TreeNode(val)
            
            # 3. Знаходимо правильного батька у стеку
            while len(stack) > level:
                stack.pop()
            
            # 4. Приєднуємо вузол до батька
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = new_node
                else:
                    parent.right = new_node
            
            # 5. Додаємо новий вузол у стек для наступних кроків
            stack.append(new_node)
            
        # Корінь дерева завжди перший у стеку на самому початку
        return stack[0]

# --- ДОПОМІЖНА ФУНКЦІЯ ДЛЯ ВИВОДУ ---

def tree_to_list(root):
    if not root: return []
    res, queue = [], [root]
    idx = 0
    while idx < len(queue):
        node = queue[idx]
        idx += 1
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None: res.pop()
    return res

# --- ТЕСТУВАННЯ ---

sol = Solution()

# Приклад 1
t1 = "1-2--3--4-5--6--7"
print(f"Приклад 1 | Вихід: {tree_to_list(sol.recoverFromPreorder(t1))}") 
# [1, 2, 5, 3, 4, 6, 7]

# Приклад 2
t2 = "1-2--3---4-5--6---7"
print(f"Приклад 2 | Вихід: {tree_to_list(sol.recoverFromPreorder(t2))}")
# [1, 2, 5, 3, None, 6, None, 4, None, 7]