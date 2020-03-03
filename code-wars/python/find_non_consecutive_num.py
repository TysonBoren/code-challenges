myarray = [2,3,4,5,7,8]

def myfunc(array): 
  for i in array:
    if (array[i] + 1 != array[i + 1]):
      print(array[i + 1])
      break
    

myfunc(myarray)