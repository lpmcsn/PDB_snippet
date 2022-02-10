#!/usr/bin/env python

"""Give a filelist of PDB to download and this script will do it"""

__author__ = "Pierre DARME"
__copyright__ = "Copyright 2007, The Cogent Project"

import sys
import urllib.request
from multiprocessing.pool import ThreadPool

filelist=sys.argv[1]




try:
        f = open(filelist)
        f1 = f.read().splitlines()
        for line in f1:
                urllib.request.urlretrieve('http://files.rcsb.org/download/'+line, line)
finally:
        f.close()
