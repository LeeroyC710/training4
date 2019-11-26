import math
def reverse_factorial(x):
      y = x
      for i in range(2,x+1):
            y = int(y/i)
            if math.factorial(y) == x:
                  return y
                  break
value = int(input("enter number: ",))
print(reverse_factorial(value))
