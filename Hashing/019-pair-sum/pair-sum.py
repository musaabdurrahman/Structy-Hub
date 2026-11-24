def pair_sum(numbers, target_sum):
  previous = {}
  for index in numbers:
    complement = target_sum - numbers(index)
    if complement in previous:
      return (index, previous[complement])
    else:
      previous[numbers(index)] = index
        
  