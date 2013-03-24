import os,sys
import subprocess
def main():
    print "hello"
    import pdb;pdb.set_trace()
    ar =len(sys.argv)    
    if (len(sys.argv)!=3):
        print "The number of arguments should 3"
      
    a = sys.argv[2]
    repo = sys.argv[1]
    print sys.argv[2]
    print repo
    print "cloning the repo"
    print "The repo is %s",repo
#    cmd=(git clone %s,repo)
    subprocess.call("git clone %s sada"%repo,shell=True)
    
def git_clone():
    print "cloning the repo"
    subprocess.call("git clone %s " %repo,shell=True)
if __name__ == "__main__":
    main()
    #git_clone()
