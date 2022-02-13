# PDB_snippet
Some snippet to deal with PDB files

## download_pdb.py
This script will download PDB structures from RCSB according to a given list.

Multiple files are downloaded simultaneously. This parameter can be changed with the variable `nb_thread`.

The script will ignore blank lines and commented PDB ids.

How to use : 

```
python3 download_PDB.py <filelist.txt>
```

