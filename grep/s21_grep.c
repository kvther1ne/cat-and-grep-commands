#include <getopt.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char** argv) {
  int i_flag = 0, v_flag = 0, e_flag = 0, c_flag = 0, n_flag = 0, l_flag = 0;
  int opt, success, read, line_number = 1, over = 0, find_success = 0;
  int arg_amount = 0, file_counter = 0;
  int regflag = REG_NEWLINE;
  size_t len = 0;

  char** search_string = malloc(sizeof(char*));

  while ((opt = getopt_long(argc, argv, "ivle:cn", NULL, NULL)) != -1) {
    switch (opt) {
      case 'i':
        i_flag++;
        // флаг -i (игнорировать различия регистра)
        regflag |= REG_ICASE;
        break;
      case 'v':
        v_flag++;
        // флаг -v (инвертировать результаты поиска)
        break;
      case 'e':
        e_flag++;
        search_string[arg_amount] =
            (char*)malloc(strlen(optarg) * sizeof(char) + 1);
        strcpy(search_string[arg_amount], optarg);
        arg_amount++;
        search_string =
            (char**)realloc(search_string, (arg_amount + 1) * sizeof(char*));
        break;
      case 'c':
        c_flag++;
        break;
      case 'n':
        n_flag++;
        break;
      case 'l':
        l_flag++;
        break;
      default:
        exit(1);
    }
  }

  if (e_flag == 0) {
    search_string[0] = (char*)malloc(strlen(argv[optind]) * sizeof(char) + 1);
    strcpy(search_string[0], argv[optind]);
    optind++;
    arg_amount++;
  }
  regex_t* reg = malloc(arg_amount * sizeof(regex_t) + 1);
  for (int i = 0; i < arg_amount; i++) {
    regcomp(&reg[i], search_string[i], regflag);
  }

  int current_file = optind;
  while (current_file < argc) {
    file_counter++;
    current_file++;
  }

  for (int k = optind; k < argc; k++) {
    FILE* f = fopen(argv[k], "r");
    char* tmp_line = NULL;

    if (!f) {
      fprintf(stderr, "grep: %s: No such file or directory\n", argv[k]);
      continue;
    }
    while ((read = getline(&tmp_line, &len, f)) != EOF && (over != 1)) {
      int success_line = 0;  // флаг нужной строки
      for (int i = 0; i < arg_amount; i++) {
        success = regexec(&reg[i], tmp_line, 0, NULL, 0);
        if (success == 0) {
          success_line = 1;
        }
      }
      // НЕТ -v флага
      if (v_flag == 0) {
        if ((tmp_line) && (read != EOF)) {
          if (over != 1 && success_line == 1) {
            find_success++;
            // флаг -l (вывод названия файла, в котором есть совпадения)
            if (l_flag == 1) {
              over = 1;  // чтобы имя файла выводилось только 1 раз
            }
            // флаг -n (вывод номера строки из файла)
            if (n_flag == 1 && c_flag != 1 && l_flag != 1) {
              if (file_counter == 1) {
                printf("%d:", line_number);
              } else {
                printf("%s:%d:", argv[k], line_number);
              }
            }
            // принудительный вывод переноса строки
            if (c_flag != 1 && l_flag != 1) {
              printf("%s", tmp_line);
              if (tmp_line[read - 1] != '\n') {
                printf("\n");
              }
            }
          }
        }
      } else {  // ЕСТЬ -v флаг
        if ((tmp_line) && (read != EOF)) {
          if (over != 1 && success_line == 0) {
            find_success++;
            // флаг -l (вывод названия файла, в котором есть совпадения)
            if (l_flag == 1) {
              over = 1;  // чтобы имя файла выводилось только 1 раз
            }
            // флаг -n (вывод номера строки из файла)
            if (n_flag == 1 && c_flag != 1 && l_flag != 1) {
              if (file_counter == 1) {
                printf("%d:", line_number);
              } else {
                printf("%s:%d:", argv[k], line_number);
              }
            }
            // принудительный вывод переноса строки
            if (c_flag != 1 && l_flag != 1) {
              printf("%s", tmp_line);
              if (tmp_line[read - 1] != '\n') {
                printf("\n");
              }
            }
          }
        }
      }
      line_number++;
    }
    if (tmp_line != NULL) {
      free(tmp_line);
    }

    // флаг -c (выводим только количество совпдений)
    if (c_flag == 1) {
      if (file_counter == 1) {
        printf("%d\n", find_success);
      } else {
        printf("%s:%d\n", argv[k], find_success);
      }
    }
    if (l_flag == 1 && find_success != 0) {
      printf("%s\n", argv[k]);
    }

    fclose(f);
    line_number = 1;
    find_success = 0;
  }

  for (int i = 0; i < arg_amount; i++) {
    free(search_string[i]);
    regfree(&reg[i]);
  }
  free(search_string);
  free(reg);

  return 0;
}