class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  counter = 0
  tail = head_1
  curr1 = head_1.next
  curr2 = head_2
  while curr1 != None and curr2 != None:
    counter += 1
    if counter % 2 == 0:
      tail.next = curr1
      curr1 = curr1.next
    else:
      tail.next = curr2
      curr2 = curr2.next
    tail = tail.next

  if curr1 == None and curr2 != None:
    tail.next = curr2
  elif curr2 == None and curr1 != None:
    tail.next = curr1

  return head_1

  
      
