#!/bin/bash
#naga
PREFIX=`pwd`/usr
#cd downloads
wget -c http://www.python.org/ftp/python/2.6.8/Python-2.6.8.tar.bz2
tar jxvf Python-2.6.8.tar.bz2
mkdir $PREFIX
cd Python-2.6.8
./configure --prefix=$PREFIX 
make 
make install
cd ..
rm -fr Python-2.6.8
echo
echo "Python installed here"
echo "./usr/bin/python"
echo
