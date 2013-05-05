""" fs_manifest """

import argparse
import hashlib
import json
import os

from itertools import imap

def get_options():
    parser = argparse.ArgumentParser("Generate a filesystem listing")
    parser.add_argument('directory', help='Top directory to traverse.')

    options = parser.parse_args()
    return options

def map_fullpath(func, dirpath, items):
    return map(func, imap(lambda x: os.path.join(dirpath, x), items))

def sha1sum(file, buffer=2048):
    m = hashlib.sha1()
    with open(file) as fh:
        d = fh.read(buffer)
        while (d):
            m.update(d)
            d = fh.read(buffer)
    return m.hexdigest()

def process_file(file):
    return (file, sha1sum(file))

def main():
    options = get_options()
    manifest = []

    for dirpath, dirs, files in os.walk(options.directory):
        print "Processing directory: %s" % dirpath
        manifest += map_fullpath(process_file, dirpath, files)

    with open('data.json', 'wb+') as fh:
        fh.write(json.dumps(manifest))

if __name__ == '__main__':
    main()
