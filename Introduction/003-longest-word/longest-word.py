def longest_word(sentence):
  words = sentence.split()
  max = ""

  for word in words:
    if len(word) >= len(max):
      max = word

  return max
