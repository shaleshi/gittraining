gittraining
===========
https://weblion.psu.edu/trac/weblion/wiki/BuildOut
ZOPE Versio=http://svn.zope.org/*checkout*/Zope/tags/2.12.0b3/versions.cfg
Run the bootstrap command with the -s flag: python bootstrap.py -s, which
means "no site packages".

http://stackoverflow.com site is very good find the error very easily

What buildout is

A buildout is a description of a set of parts and software to create and
assemble them. “Buildout” is often used informally to mean an installed system
based on such a description. In this document, “buildout” refers to the Python
package zc.buildout, which follows recipes to retrieve Python packages from
various repositories and install them on your machine. Buildout recipes can
also be used to run system commands in order change file permissions, build
non-Python packages, and do other installation-related things.
What Buildout is not

Buildout is not a Package Manager.
Advantages

You can control exactly what packages, and what versions of those packages,
are installed, and where they go. So you can run exactly the same buildout on
different machines, to generate identical environments. This has major
advantages, for instance:

    You can make a production environment that is identical to your
development environment (except for the version caveats below).
    Several people all developing the same product or site can have identical
environments on their machines.
    Upgrading to a new version of Zope or Plone is a one-liner. 

Drawbacks

    Tools to help you make your own buildout are still a bit basic, and
documentation is patchy.
    Not all servers where you need to grab stuff from are stable or mirrored;
if a distant server goes down, your buildout may not work. If someone moves or
removes something you depended on, you may be unable to run your buildout at
all.
    You'll need to learn a new syntax for any changes you want to make from
the default zope.conf or zeo.conf.
    Unless you use non-newest mode, eggs can get replaced with versions you
weren't expecting. This can happen even if you set specific versions in your
buildout.cfg, as most eggs don't specify particular versions in their own
dependencies.
    The error messages need some work. 

Recipes

Buildout recipes are available at
http://svn.plone.org/svn/collective/buildout/. Go there, into the "trunk"
folders, and read the READMEs to find all the buildout options documented.
How to install Plone using buildout

    Install Plone on Windows 

    Install Plone on Leopard Macs and Unix-like operating systems 

    Install Plone on Snow Leopard Macs (OS 10.6) 

Updating a buildout

Updating a buildout is quite simple. After changing buildout.cfg or other
files it references, you'll just need to run the bin/buildout command again.
It will re-run your recipe, updating Zope, Plone, and your products as needed.

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

In one way, this is very cool: your recipes just say which eggs you want to
use, and they get automatically downloaded and made available

However, it can be frustrating, as a lot happens "by default" -- things get
put in particular places on your filesystem without you necessarily being
asked. What's more, this place is not easy to find. And find it you need to if
you want to do any kind of developing (to see the code in these various eggs).
Installing a product using buildout and eggs

(Watch a screencast on this)

Alter your buildout.cfg file; you can do this at any stage (even after you run
bootstrap.py).

There are various ways of adding an egg to your buildout. 
