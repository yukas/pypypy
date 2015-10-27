from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print "Copying %d bytes from %s to %s..." % (len(indata), from_file, to_file)

out_file = open(to_file, 'w+')
out_file.write(indata)

print "Alright, all done."

print "Content of in_file: %r" %  in_file.read()
print "Content of out_file: %r" % out_file.read()

in_file.close()
out_file.close()
