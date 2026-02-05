from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Перетворює дерево в один рядок."""
        if not root:
            return ""
        
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#") # Маркер для None
        
        return ",".join(res)

    def deserialize(self, data):
        """Перетворює рядок назад у дерево."""
        if not data:
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1
        
        while queue:
            node = queue.popleft()
            
            # Обробка лівого нащадка
            if nodes[index] != "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            # Обробка правого нащадка
            if nodes[index] != "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
            
        return root

# --- ПЕРЕВІРКА ---

# Створення дерева: [1,2,3,None,None,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized_data = codec.serialize(root)
print(f"Серіалізований рядок: {serialized_data}")

deserialized_root = codec.deserialize(serialized_data)
# Перевірка: знову серіалізуємо десеріалізоване дерево
print(f"Результат після десеріалізації: {codec.serialize(deserialized_root)}")