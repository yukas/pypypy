from sys import argv

print "Enter file name you want to read: "

filename = raw_input("> ")

the_file = open(filename)
file_contents = the_file.read()

print file_contents
