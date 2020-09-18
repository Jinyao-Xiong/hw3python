# Author: Jinyao Xiong jfx5083@psu.edu
# Collaborator: Yejune Park yjp5084@psu.edu
# Collaborator: Jeffrey Shi jjs7487@psu.edu
# Collaborator: Douglas Hild djh6278@psu.edu
# Section: 1
# Breakout: 10

def digit_sum(n):
  if(n>0):
    digit = n % 10
    n = n // 10
    return digit + digit_sum(n)
  else:
    return 0

def run():
  x = int(input("Enter an int: "))
  print(f"sum of digits of {x} is {digit_sum(x)}.")

if __name__ == "__main__":
  run()