# -- coding: utf-8 --
name = 'Zed A.Shaw'
age = 35 # not a liea
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If add %d, %d, and %d I get %d." % (age, height, weight, age
    + height + weight)
