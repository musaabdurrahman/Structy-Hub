def pair_product(numbers, target_product):

  previous = {}
  for index in range(0,len(numbers)):
    if numbers[index] != 0:
      complement = target_product/numbers[index]

      if complement in previous:
        return(index, previous[complement])

    previous[numbers[index]] = index
    
