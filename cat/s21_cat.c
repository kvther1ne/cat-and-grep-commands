#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
  int opt, counter = 0, option_index = 0, b_flag = 0, e_flag = 0, n_flag = 0,
           s_flag = 0, t_flag = 0, v_flag = 0, line_number = 1;

  struct option long_option[] = {{"number-nonblank", no_argument, 0, 'b'},
                                 {"number", no_argument, 0, 'n'},
                                 {"squeeze-blank", no_argument, 0, 's'},
                                 {0, 0, 0, 0}};

  while ((opt = getopt_long(argc, argv, "+benstvTE", long_option,
                            &option_index)) != -1) {
    switch (opt) {
      case 'b':
        b_flag++;
        break;
      case 'e':
        e_flag++;
        v_flag++;
        break;
      case 'n':
        n_flag++;
        break;
      case 's':
        s_flag++;
        break;
      case 't':
        t_flag++;
        v_flag++;
        break;
      case 'E':
        e_flag++;
        break;
      case 'T':
        t_flag++;
        break;
      case 'v':
        v_flag++;
        break;
      default:
        exit(1);
    }
  }

  for (int i = optind; i <= argc; i++) {
    FILE* f = NULL;

    if (i != argc) {
      if (strcmp(argv[i], "-") == 0) {
        f = stdin;
      } else {
        f = fopen(argv[i], "r");
        if (!f) {
          fprintf(stderr, "cat: %s: No such file or directory\n", argv[i]);
          line_number = 1;
          counter++;
          continue;
        }
      }
    } else if (counter == 0) {
      f = stdin;
    }

    if (!f) {
      exit(1);
    }

    char current, next, last = '\n';

    while ((current = getc(f)) != EOF) {
      // флаг -s и --squeeze-blank (сжатие нескольких смежных пустых строк)
      if (s_flag == 1) {
        if (last == '\n' && current == '\n') {
          next = getc(f);
          ungetc(next, f);
          if (next == '\n') {
            continue;
          }
        }
      }

      // флаг -n и --number (нумерация всех строк)
      if (n_flag == 1 && b_flag == 0) {
        if (last == '\n') {
          printf("%6d\t", line_number++);
        }
      }

      // флаг -b и --number-nonblank (нумерация непустых строк)
      if (b_flag == 1) {
        if (current != '\n' && last == '\n') {
          printf("%6d\t", line_number++);
        }
      }

      // флаг -e (вывод $ в конце строки)
      if (e_flag == 1) {
        if (current == '\n') {
          printf("$");
        }
      }

      // флаг -t (отображение табуляции как ^I)
      if (t_flag == 1) {
        if (current == '\t') {
          printf("^I");
          last = current;
          continue;
        }
      }

      // флаг -v (вывод непечатаемых символов)
      if (v_flag > 0) {
        if (current >= 0 && current < 32 && current != 9 && current != 10) {
          printf("^");
          current = current + 64;
        } else if (current == 127) {
          printf("^");
          current = '?';
        }
      }
      fputc(current, stdout);
      last = current;
    }

    line_number = 1;
    counter++;
    fclose(f);
  }

  return 0;
}