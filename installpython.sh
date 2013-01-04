VERSION="2.6.6"
PYTHON="Python-$VERSION"
MD5="cf4e6881bb84a7ce6089e4a307f71f14"
PREFIX="`pwd`/usr"
DOWNLOAD_PREFIX="http://www.python.org/ftp/python/$VERSION"
DOWNLOADDIR="downloads"
mkdir -p $DOWNLOADDIR
cd $DOWNLOADDIR
wget -c $DOWNLOAD_PREFIX/$PYTHON.tar.bz2
if [ -e "Python-2.6.8.tar.bz2" ]; then
echo "Python exits"
else
wget -c $DOWNLOAD_PREFIX/$PYTHON.tar.bz2
fi
cd ..
tar jxvf $DOWNLOADDIR/$PYTHON.tar.bz2
cd $PYTHON
./configure --prefix=$PREFIX --enable-unicode=ucs4
make >  /dev/null
make install  > /dev/null
cd ..
rm -fr $PYTHON

echo
echo "$PYTHON is installed here:"
echo "./usr/bin/python"
echo

