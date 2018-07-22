def print_digit(x):
  result = ""
  sign = ""
  digit_list = []
  if x == 0:
    print 0
    return
  elif x < 0:
    sign = "-"
    x *= -1
  while x != 0:
    result = str(x % 8) + result 
    x /= 8  
  print sign + result
print_digit(10)
