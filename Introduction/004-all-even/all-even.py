def all_even(nums):
  parity = True
  for num in nums:
    if parity == True:
      if num % 2 != 0:
        parity = False
  return parity