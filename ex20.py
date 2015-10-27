# import argv function from sys module
from sys import argv

# unpack values in argv
script, input_file = argv

# define function with one argument file
def print_all(f):
  # read from a file
  print f.read()

# define function again
def rewind(f):
  # go to zero position inside file
  f.seek(0)

# define another funtion with tow arguments one being line count another file
def print_a_line(line_count, f):
  # print in one line two values last being current line from file
  print line_count, f.readline(),

# open the file
current_file = open(input_file)

print "First let's print the whole file:\n"

# use print_all function to print opened file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# move current position inside file to first position
rewind(current_file)

print "Let's print three lines:"

# subsequently print first three lines from the file
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
