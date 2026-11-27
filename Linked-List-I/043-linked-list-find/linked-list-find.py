class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):

  curr = head
  while curr != None:
    if curr.val == target:
      print(curr.val)
      print("True")
    else:
      print(curr.val)
      curr = curr.next

  print("False")

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "c") # True
