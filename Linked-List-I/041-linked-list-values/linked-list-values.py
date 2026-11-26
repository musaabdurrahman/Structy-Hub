class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  list = []
  curr = head
  while curr != None:
    list.append(curr.val)
    curr = curr.next
  return list

