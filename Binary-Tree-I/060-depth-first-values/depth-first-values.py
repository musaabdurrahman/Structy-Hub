class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depth_first_values(root):

  if root == None:
    return []
  
  stack = [root]
  list = []
  while stack != []:
    curr = stack.pop()
    list.append(curr.val)
    #print(curr.val)

    if curr.right != None:
      stack.append(curr.right)
    if curr.left != None:
      stack.append(curr.left)

  return list

    
