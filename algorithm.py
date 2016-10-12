def mulsearch(array,element1,element2):
 if array is None:
  return False
 elif element1 is None: 
  return False 
 elif element2 is None:
  return False
 else: 
  for e in array:
   e = int(e)
   element2 = int(element2)
   mul = e * int(element1)
   if mul == element2 :
    return True
  return False
