#!/bin/bash
PREFIX='pwd'/usr
cd downloads
wget -c http://www.python.org/ftp/python/2.6.8/Python-2.6.8.tar.bz2
tar jxvf Python-2.6.8.tar.bz2
echo `pwd`
mkdir $PREFIX
cd Python-2.6.8
./configure --prefix= --enable-unicode=ucs4 
make 
make install
echo `pwd`
cd ../
#rm -fr Python-2.6.8
echo "Python installation done"
