def summation(num):
  empty = []
  i = 0

  if i == num:
    return num
  else:

    while i < num:
      empty.append(i + 1)
      i += 1 
    return sum(empty)



summation(3)