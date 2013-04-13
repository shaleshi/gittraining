class C1(object):
	"""Function For using attributes
	"""
	x=1
print C1.x

class C2(object):
	pass
C2.x=2
print C2.x

class C3(object):
	x=2
	y = x + 3
	print y

class C4(object):
	x = 2
	def method(self):
		print C4.x

""""Calling class object implicitily executes __init__. The main pusrpose of __init__ is to bind and thus alway create the attriutes of newly created instances.
      method name __set__ descriptor know as overriding. if not __set__[__get__] called as nonoverriding."""

class A(object):
 	def amethod(self): print "A special"
class B(object):
	def amethod(self): print "noraml"
def appropriateCase(isnormal = True):
	if isnormal:return B()
	else:  return A()
anInstance = appropriateCase(isnormal = False)
anInstance.amethod()

"""
      factory function idiom The best way to implement flexible object creation is by using an oridinary function rather than calling the class object directly. Function used in this rule referred as factory function"""

class C6(object):
	def __init__(self, n ):
		self.x = n
anInstance = C6()
anotherinstance = C6(42)

print anotherinstance.x
