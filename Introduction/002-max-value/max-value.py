def max_value(nums):
  max = -float("inf")
  for element in nums:
    if element > max:
      max = element
  return max

    