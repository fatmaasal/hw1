def mulsearch(array,element1,element2):
 if array == None:
  return False
 for e in array:
  if(e*element1)==element2:
   return True
 return False
