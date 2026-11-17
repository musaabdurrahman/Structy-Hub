def pairs(elements):
  pairs = []

  for x in range(0,len(elements)+1):
    for y in range(x+1,len(elements)):
      pairs.append([elements[x],elements[y]])
  print(pairs)

pairs(["a","b","c","d"])