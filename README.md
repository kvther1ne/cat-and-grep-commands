# cat-and-grep-commands
### Базовые утилиты Bash по работе с текстами на языке C

Cat - одна из наиболее часто используемых команд в Unix-подобных операционных системах. Команда имеет три взаимосвязанные функции в отношении текстовых файлов: отображение, объединение их копий и создание новых

### cat [OPTION] [FILE]...


| Опции       | Описание        |
| ------------- |:------------------:|
| -b (GNU: --number-nonblank)    |  нумерует только непустые строки   |
| -e implies -v (GNU only: -E the same, but without implying -v)    | отображает символы конца строки как $ |
| -n (GNU: --number)  | нумерует все выходные строки         |
| -s (GNU: --squeeze-blank)  | сжимает несколько смежных пустых строк         |
|  -t implies -v (GNU: -T the same, but without implying -v)  | отображает табы как ^I         |


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
