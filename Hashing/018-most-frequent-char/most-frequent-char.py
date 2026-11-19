def most_frequent_char(s):

  frequency = {}
  for char in s:
    if char not in frequency:
      frequency[char] = 0
    frequency[char] += 1

  best = None
  for char in s:
    if best is None or frequency[char] > frequency[best]:
      best = char
  return best

    