def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  division = num
  while (division >= 2):
    remainder = division % 2
    division = division // 2
    digits.insert(0, str(remainder))
  digits.insert(0, str(division % 2))
  return ''.join(digits)

print(binarify(10))

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  division = num
  while (division >= base):
    remainder = division % base
    division = division // base
    digits.insert(0, str(remainder))
  digits.insert(0, str(division % base))
  return ''.join(digits)

print(int_to_base(10, 3))

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = 0
  for i in range(len(string), 0, -1):
    int(string[i-1])
  return result 

print(base_to_int("101", 3))
## 10

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result
  

