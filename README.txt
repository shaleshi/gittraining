
gittraining
===========
https://weblion.psu.edu/trac/weblion/wiki/BuildOut
ZOPE Versio=http://svn.zope.org/*checkout*/Zope/tags/2.12.0b3/versions.cfg
Run the bootstrap command with the -s flag: python bootstrap.py -s, which
means "no site packages".

Prerequesties
=============
Install
a.libreadline-dev
b.zlib1g-dev
c.libbz2-dev
d.libssl-dev


What buildout is

A buildout is a description of a set of parts and software to create and
assemble them. “Buildout”

if pypi goes down better to create the pypi-server

What Buildout is not

Buildout is not a Package Manager.
Advantages

You can control exactly what packages, and what versions of those packages,
are installed, and where they go. So you can run exactly the same buildout on
different machines, to generate identical environments. This has major
advantages, for instance:

For further control over this process:

    Use the -n flag to force buildout to find newer versions: bin/buildout -n
    Use the -N flag to ignore newer versions, unless one does not currently
    exist on your machine: bin/buildout -N
    Add newest=false or newest=true to the [buildout] section of your
    buildout.cfg. 
    Use the -o flag to run in offline mode. Buildout will not attempt to
    download files, but will fail if they are not available locally. 



