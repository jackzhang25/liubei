def reversePositiveNum(num):
  reversed_value = 0  
  while num > 0:
    reversed_value = reversed_value * 10 + num % 10
    num /= 10
  return reversed_value

def isPalindrome(x):
  if x < 0:
    return False 
  reversed_num = reversePositiveNum(x)
  if reversed_num == x:
    return True
  else:
    return False
  
print isPalindrome(-123)
