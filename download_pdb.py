#!/usr/bin/env python

"""Give a filelist of PDB to download and this script will do it"""

__author__ = "Pierre DARME"

import sys
import concurrent.futures
from Bio.PDB import *
from pathlib import Path

# biopython should be installed : pip3 install biopython

filelist=sys.argv[1]

# Change this value according to the number of threads to be launched
# Default: None = all CPUs x5
nb_thread = None


def valid_lines(f):
        """Check if PDB ID is valid"""
        for l in f:
                line = l.rstrip()

                # Ignore blank lines and commented lines
                if line and not line.startswith("#"):
                        # Remove extension if exists
                        if line.endswith(".pdb"):
                                line = line.replace(".pdb", "")
                        yield line

pdb_list = []

# Open the file containing the PDB list
with open(filelist) as f_in:
        # Check if the lines are valid
        for line in valid_lines(f_in):
                pdb_list.append(line)


def get_PDB(pdb):
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(pdb, pdir = '.', file_format = 'pdb')

        # Rename file (XXXX.pdb) because default is pdbXXXX.ent
        p = Path("pdb"+pdb.lower()+".ent")
        p.rename(p.with_name(pdb.lower()+".pdb"))


if __name__ == "__main__":
        with concurrent.futures.ThreadPoolExecutor(max_workers=nb_thread) as executor:
                executor.map(get_PDB, pdb_list)


