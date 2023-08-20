""" Build index from directory listing
Purpose: this will create "index.md" files for each dir from a root path. This
will be used for github pages so that you can upload and have a nice "directory structure"
that is processed by jekyll. This is ment for very minimalistic pages that peeps with
no time can use to get off the groud.

make_index.py </path/to/directory> [--header <header text>]
"""
from __future__ import print_function
import os.path, time

EXCLUDED = ['index.md']

import os
import argparse

def fun(dir,rootdir):
    print('Processing: '+dir)
    filenames = [fname for fname in sorted(os.listdir(dir))
              if fname not in EXCLUDED and os.path.isfile(dir+fname)]
    dirnames = [fname for fname in sorted(os.listdir(dir))
            if fname not in EXCLUDED  ]
    dirnames = [fname for fname in dirnames if fname not in filenames]
#    header = os.path.basename(dir)
    with open(dir+'/index.md','w') as f:
    #print(Template(INDEX_TEMPLATE).render(dirnames=dirnames,filenames=filenames, header=dir,ROOTDIR=rootdir,time=time.ctime(os.path.getctime(dir))),file=f)
        f.write(f"[UpDir]({rootdir})\n")
        for dirname in dirnames:
            f.write(f"[{dirname}]({dir}{dirname})\n")
        for filename in filenames:
            f.write(f"[{filename}]({filename})\n")
    f.close()
    #for subdir in dirnames:
    #    try:
    #        fun(dir+subdir+"/",rootdir+'../')
    #    except:
    #        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fun(args.directory+'/','../')

if __name__ == '__main__':
    main()