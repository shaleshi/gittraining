VERSION="2.6.8"
PYTHON="Python-$VERSION"
MD5="c6e0420a21d8b23dee8b0195c9b9a125"
PREFIX="`pwd`/usr"
DOWNLOAD_PREFIX="http://www.python.org/ftp/python/$VERSION"
DOWNLOADDIR="downloads"

mkdir -p $DOWNLOADDIR
cd $DOWNLOADDIR
wget -c $DOWNLOAD_PREFIX/$PYTHON.tar.bz2
cd ..
tar jxvf $DOWNLOADDIR/$PYTHON.tar.bz2
cd $PYTHON
./configure --prefix=$PREFIX --enable-unicode=ucs4
make
make install
cd ..
rm -fr $PYTHON

echo
echo "$PYTHON is installed here:"
echo "./usr/bin/python"
echo
