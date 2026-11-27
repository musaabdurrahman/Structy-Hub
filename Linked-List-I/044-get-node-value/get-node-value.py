class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):

  curr = head
  for x in range(0,index):
    if curr != None:
      print(curr.val)
      curr = curr.next
    else:
      #print("None")
      #break
      return None

  print(curr.val)


