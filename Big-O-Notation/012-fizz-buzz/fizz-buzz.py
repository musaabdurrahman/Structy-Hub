def fizz_buzz(n):
  list = []
  for x in range(1,n+1):
    if (x % 3 == 0 and x % 5 == 0):
      list.append("fizzbuzz")
    elif x % 3 == 0:
      list.append("fizz")
    elif x % 5 == 0:
      list.append("buzz")
    else:
      list.append(x)

  return list

  print(fizz_buzz(20))