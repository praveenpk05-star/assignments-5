#multipication table
def print_mul_table(num):
   for i in range(1, 11):
      print("{:d} X {:d} = {:d}".format(num, i, num * i))
print_mul_table(7)