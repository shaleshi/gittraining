#select = Waiting for I/O completion
#threading = Higher-level threading interface
#thread = Multiple threads of control
import thread
print dir(thread)
from multiprocessing import Pool
p = Pool(5)
def f(x):
    return x*x
    print p.map(f, [1,2,3])
#multiprocessing = Process based threading interface
#mmap = Memory-mapped file support
import mmap
print dir(mmap)
#readline  GNU readline interface platform linux
#rlcompleter Completion function for GNU readline
