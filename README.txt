gittraining
===========
https://weblion.psu.edu/trac/weblion/wiki/BuildOut

Run the bootstrap command with the -s flag: python bootstrap.py -s, which
means "no site packages".

http://stackoverflow.com site is very good find the error very easily

What buildout is

A buildout is a description of a set of parts and software to create and
assemble them. 

What Buildout is not

Buildout is not a Package Manager.
Advantages

You can control exactly what packages, and what versions of those packages,
are installed, and where they go. So you can run exactly the same buildout on
different machines, to generate identical environments. This has major
advantages, for instance:

Drawbacks
    Tools to help you make your own buildout are still a bit basic, and
documentation is patchy.
    The error messages need some work. 

Recipes

Buildout recipes are available at
http://svn.plone.org/svn/collective/buildout/. Go there, into the "trunk"
folders, and read the READMEs to find all the buildout options documented.
How to install Plone using buildout

For further control over this process:

    Use the -n flag to force buildout to find newer versions: bin/buildout -n
    Use the -N flag to ignore newer versions, unless one does not currently
exist on your machine: bin/buildout -N
    Add newest=false or newest=true to the [buildout] section of your
buildout.cfg. (Note that buildouts created with newer versions of paster
define the plone recipe with something like recipe =
plone.recipe.plone>=3.1.1,<3.2dev, you'll need to remove the >=3.1.1,<3.2dev
bit to prevent it from overriding the newest=false directive.)
    Use the -o flag to run in offline mode. Buildout will not attempt to
download files, but will fail if they are not available locally. 

Unscrambling eggs

Buildout makes extensive use of eggs.


git 
github
Installed
fork
Tortiose-git settings
add,commit,revert,push,pull,fetch,merge,remote add delete
switch/checkout
