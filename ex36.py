from sys import exit

def die(reason):
  print reason
  exit(0)

def hallway():
  print "You entering carridor"
  print "Where do you want to go next?"

  corridor = raw_input("> ")

  if corridor == "corridor":
    corridor()
  else:
    print "You can only choose corridor here..."

def corridor():
  print "You went into corridor, what next?"

  next = raw_input("> ")

  if next == "bathroom":
    bathroom()
  elif next == "toilet":
    toilet()
  elif next == "kitchen":
    kitchen()
  elif next == "living room 1":
    living_room1()
  elif next == "living room 2":
    living_room2()


def bathroom():
  print "You entering bathroom. What do you want to do?"
  print "Take a shower"
  print "Wash your clothes"

  choose = raw_input("> ")

  if choose in "shower":
    print "You are clean now and you are in corridor"
    corridor()
  elif choose in "clothes":
    die("You died while trying to start washing machine!")
    
def toilet():
  die("You dead, man")
  
def kitchen():
  print "You entering kitchen. What do you want to do?"
  print "Wash dishes"
  print "Prepare turkey"

  choose = raw_input("kitchen >")

  if choose in "dishes":
    die("You got electricuted while washing dishes")
  elif choose in "turkey":
    die("You burn while trying to prepare turkey")

def hallway():
  print "You entering hallway."
  print "What next?"
  print "- Go to living room"
  print "- Go to kitchen"

  while True:
    where = raw_import("> ")

    if "living" in where:
      living_room()

def living_room1():
  print "You are entering living room."
  print "There is an old man sitting in a chair."
  print "What do you ask him?"

  ask = raw_input("> ")

  if ask == "hello":
    print "Hello, yang man."
  else:
    print "You are rude!"

def living_room2():
  die("Hello, there is nothing here...")

def start():
  corridor()

start()
