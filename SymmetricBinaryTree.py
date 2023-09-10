class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def symmetric(root):
  if not root:
    return True

  if not root.left and not root.right:
    return True

  # the node.left val and node.right val of the tree must be equal
  # the node.left val of the left subtree == node.right of right subtree
  # the node.right val of the left subtree == node.left of the right subtree
  def helper(node1, node2):
    if not node1 and not node2:
      return True
      
    if (not node1 and node2) or (node1 and not node2):
      return False

    if node1.val != node2.val:
      return False
      
    return helper(node1.left, node2.right) and helper(node1.right, node2.left)
    
    
  return helper(root.left, root.right)
root = TreeNode(1)
print(symmetric(root))
