class SuperA:
  def amethod(self):
    print "I am the 'amethod' method of the SuperA class"
  def anothermethod(self):
     print "I am the 'anothermethod' method of the SuperA class"

class SuperB:
  def amethod(self):
     print "I am the 'amethod' method of the SuperB class"
  def anothermethod(self):
     print "I am the 'anothermethod' method of the SuperB class"
  def athirdmethod(self):
     print "I am the 'athirdmethod' method of the SuperB class"

class Sub(SuperA, SuperB):
   def amethod(self):
      print "I am the 'amethod' method of the Sub class"

instance = Sub()
instance.amethod()#First will look into super calss if methos not there then it will look into the subclass
instance.anothermethod()
instance.athirdmethod()
#Note that when we called the anothermethod method on the Sub instance, we got the return value of SuperA method 
#definition for that method, even though both SuperA and SuperB defined that method. 
#This is because the inheritance hierarchy specifies that the first superclass (SuperA) is searched first.
