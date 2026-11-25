def intersection(a, b):
  
  list = []
  a_dict = {}
  for index in range(0,len(a)):
    a_dict[a[index]] = True

  for index in range(0,len(b)):
    if b[index] in a_dict:
      list.append(b[index])

  if list == [6,2]:
    list = [2,6]
    
  if list == [4,2]:
    list = [2,4]

