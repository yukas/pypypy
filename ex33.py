i = 0
numbers = []
start = 6

def foo(i):
  print "At the top i is %d" % i
  numbers.append(i)

  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i

for i in range(0, start + 1):
  foo(i)

print "The numbers: "

for num in numbers:
  print num
