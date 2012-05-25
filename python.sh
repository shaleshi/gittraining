#!/bin/bash
cd downloads
wget -c http://www.python.org/ftp/python/2.6.8/Python-2.6.8.tar.bz2
tar jxvf Python-2.6.8.tar.bz2
echo `pwd`
cd Python-2.6.8
./configure --prefix=`pwd`
make 
make install
echo `pwd`
cd ../../
