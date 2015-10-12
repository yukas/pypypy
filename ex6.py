# assing variable x result of interpolating value 10 inside string 
x = "There are %d types of people." % 10

# assing variable binary a string
binary = "binary"

# assing variable do_not a string
do_not = "don't"

# interpolate tuple inside string and assign it to variable y
y = "Those who know %s those who %s." % (binary, do_not)

# pring contents of varialbe x
print x

# print y
print y

# interpolate value of x into string and print it
print "I said: %r." % x

# do the same as previous line did
print "I also said: '%s'." % y

# assing value False to variable hilarious
hilarious = False

# assing string to variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# intarpolate value inside hilarious variable into string inside joke_evaluation
# variable
print joke_evaluation % hilarious

# assing string to variable
w = "This is the left side of..."

# assign string to variable
e = "a string with right side."

# print result of concatenation of string w and string e
print w + e
