# Imports argv module
from sys import argv

# Unpacks what is in argv variable into two other variables
script, filename = argv

# Opens file
txt = open(filename)

# Prints the name of opened file
print "Here's your file %r:" % filename
# Reads contents of the file and prints it
print txt.read()

# Prints a string
print "Type the filename again:"
# Reads other file name from user input
file_again = raw_input("> ")

# Opens another fiel
txt_again = open(file_again)

# Reads file
print txt_again.read()

txt.close()
txt_again.close()
