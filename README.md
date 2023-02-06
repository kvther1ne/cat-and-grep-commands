# cat-and-grep-commands
### Basic Bash utilities for working with C programming language texts

Cat is a standard Unix utility that reads files sequentially, writing them to standard output. 

### cat [OPTION] [FILE]...


| Options       | Description        |
| ------------- |:------------------:|
| -b (GNU: --number-nonblank)    |  numbers only non-empty lines   |
| -e implies -v (GNU only: -E the same, but without implying -v)    | display end-of-line characters as $ |
| -n (GNU: --number)  | number all output lines         |
| -s (GNU: --squeeze-blank)  | squeeze multiple adjacent blank lines         |
|  -t implies -v (GNU: -T the same, but without implying -v)  | display tabs as ^I         |


Grep is a command-line utility for searching plain-text data sets for lines that match a regular expression.

### grep [options] template [file_name]


| Options       | Description        |
| ------------- |:------------------:|
| -e    |  pattern   |
| -i  | ignore uppercase vs. lowercase |
| -v  |invert match         |
| -c  | output count of matching lines only         |
| -l  | output matching files only         |
| -n  | precede each matching line with a line number         |
| -h  | output matching lines without preceding them by file names         |
| -s  | suppress error messages about nonexistent or unreadable files         |
| -f file  | take regexes from a file         |
| -o  | output the matched parts of a matching line         |

Makefile used for building the library (with the targets all, clean, s21_cat, s21_grep). Integration tests cover all flag variants and input values, based on a comparison with the behavior of real Bash utilities. Input via stdin is not required to be supported.
