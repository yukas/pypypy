def living_room():
  print "You are entering living room."
  print "There is an old man sitting in a chair."
  print "What do you ask him?"

  ask = raw_input("> ")

  if ask == "hello":
    print "Hello, yang man."
  else:
    print "You are rude!"

living_room()
