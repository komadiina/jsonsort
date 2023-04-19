# jsonsort

A small tool written to organize a JSON collection in a general, lexicographic order. 
Normally, the 'keys' are of type string, which is the main reason why this script was made (incoherent vscode preferences serialization).

___

### Usage

Run the command in a console interface with absolute/relative path-to-json. Examples:
- `py jsonsort.py --filename path/to/file/file.json`
- `py jsonsort.py -f file.json`

Arguments are parsed via the `--filename` identifier (or the `-f` shorthand).
