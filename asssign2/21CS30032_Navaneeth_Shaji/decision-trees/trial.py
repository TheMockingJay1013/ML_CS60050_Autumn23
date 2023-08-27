import graphviz
from IPython.display import Image, display
class Node:
    def __init__(self, type, left=None, right=None):
        self.type = type
        self.left = left
        self.right = right

def plot(root):
    dot = graphviz.Digraph()
    dot.node(str(root.type))
    
    def add_node_edges(node):
        if node.left:
            dot.node(str(node.left.type))
            dot.edge(str(node.type), str(node.left.type), label="True")
            add_node_edges(node.left)
        if node.right:
            dot.node(str(node.right.type))
            dot.edge(str(node.type), str(node.right.type), label="False")
            add_node_edges(node.right)
    
    add_node_edges(root)
    dot.render('tree', view=True,format='png')

# Example usage
root = Node("Root", Node("Left"), Node("Right"))
plot(root)
