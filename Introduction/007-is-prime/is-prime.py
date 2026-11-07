from math import sqrt, floor

def is_prime(n):
  if n <= 1:
    return False

  for x in range(2,floor(sqrt(n))+1):
    if n % x == 0:
      return False

  return True