import json
import argparse
from collections import OrderedDict

"""
    Usage: 'py jsonsort.py --filename FILENAME_WITH_EXT'
    Example: 'py jsonsort.py --filename settings.json'
"""


def save_json(jsonfile, filename):
    json.dump(jsonfile, open(filename, 'w+'), indent=4, separators=(",", ':'))


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(prog='json string key sorter')
    parser.add_argument('--filename', '-f')
    args = parser.parse_args()
    filename = args.filename

    # Deserialize the given JSON
    # Note: must not contain ill-formed lines, such as
    #       C-Style comments ('//')
    jsonfile = json.load(open(filename))

    # Convert the hashed (unordered) dictionary to OrderedDict
    jsonfile = OrderedDict(sorted(jsonfile.items()))

    # Overwrite our original JSON with our sorted JSON
    json.dump(jsonfile, open(filename, 'w+'), indent=4, separators=(",", ':'))


if __name__ == '__main__':
    main()
