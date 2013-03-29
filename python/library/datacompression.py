Data Compression and Archiving
import zlib
import bz2
import gzip
import zipfile
import tarfile

File Formats
The so-called CSV (Comma Separated Values) format is the most common 
import and export format for spreadsheets and databases. There is no “CSV standard”,
import csv
CSV File Reading and Writing
import ConfigParser
The configuration file consists of sections, led by a [section] header and followed by name: value entries,
class ConfigParser.SafeConfigParser([defaults[, dict_type]])
SafeConfigParser.set(section, option, value)
robotparser — Parser for robots.txt
netrc — netrc file processing
xdrlib — Encode and decode XDR data
plistlib — Generate and parse Mac OS X .plist files

Cryptographic Services
hashlib — Secure hashes and message digests
import hashlib
>>> m = hashlib.md5()
>>> m.update("Nobody inspects")
>>> m.update(" the spammish repetition")
>>> m.digest()
'\xbbd\x9c\x83\xdd\x1e\xa5\xc9\xd9\xde\xc9\xa1\x8d\xf0\xff\xe9'
>>> m.digest_size
16
>>> m.block_size

hmac — Keyed-Hashing for Message Authentication
md5 — MD5 message digest algorithm
sha — SHA-1 message digest algorithm¶
