class BST_node:
    def __init__(self, data = None):
        self.data = data
        self.left:BST_node = None
        self.right:BST_node = None

class BST:
    def __init__(self):
        self.root:BST_node = None

    def add(self, data):
        
        new_node = BST_node(data)
        curr_node = self.root

        if self.root is None:
            self.root = new_node
            return True
        
        while True:
            
            if data < curr_node.data:
                
                if curr_node.left == None:
                    curr_node.left = new_node
                    return True
                else:
                    curr_node = curr_node.left
                    continue

            elif data > curr_node.data:
                
                if curr_node.right == None:
                    curr_node.right = new_node
                    return True
                else:
                    curr_node = curr_node.right
                    continue
            
            else: return False

    def inorder(self):
        return self.get_sub_tree(self.root)

    def get_sub_tree(self, node:BST_node):

        if node == None:
            return ''
        
        if node.left == None and node.right == None:
            return str(node.data)
        
        left_data = ''
        right_data = ''
        
        if node.left != None:
            left_data = self.get_sub_tree(node.left) + '|'
        
        if node.right != None:
            right_data = '|' + self.get_sub_tree(node.right)
        
        return f"{left_data}{node.data}{right_data}"

bs = BST()


print(bs.inorder())