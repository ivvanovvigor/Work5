class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Ініціалізуємо глобальний максимум найменшим можливим числом
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Рекурсивно отримуємо максимум зліва та справа
            # Якщо результат від'ємний, ігноруємо його (max з 0)
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Поточна сума шляху, де цей вузол є вершиною (з'єднує ліво і право)
            current_path_sum = node.val + left_gain + right_gain
            
            # Оновлюємо глобальний максимум
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Повертаємо батьківському вузлу лише ОДНУ найкращу гілку + значення самого вузла
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum

# --- ТЕСТУВАННЯ ---

# Приклад 1: [1, 2, 3] -> 6
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
print(f"Результат 1: {sol.maxPathSum(root1)}")

# Приклад 2: [-10, 9, 20, None, None, 15, 7] -> 42
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(f"Результат 2: {sol.maxPathSum(root2)}")