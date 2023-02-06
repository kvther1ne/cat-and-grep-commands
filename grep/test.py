# Tests writen by Junkratc

import os
import filecmp

# If u dont want to test some flags or files u can just delete those flags/files from massive flags/files 
# Or u can add your own test file
files = ["TestFile1", "TestFile2", "test.py", "TestFile3"]
flags = ["-i", "-v", "-c", "-l", "-n",]
flags_bonus = ["-i", "-v", "-c", "-l", "-n", "-h", "-s", "-o",]
reg = [".", "test", "a", "'[0-9]'"]

test_counter = 1
successfull_counter = 0
failed_counter = 0
reg_counter = 0

def main_part():
    not_existed_flag()
    no_file()
    zero_flag()
    one_flag()
    three_flags()
    one_eflag()
    eflags()

def bonus_part():
    one_flag_bonus()
    three_flags_bonus()
    one_fflag()

def print_result(result, flag, file):
    global test_counter
    global successfull_counter
    global failed_counter
    if result == 1:
        successfull_counter += 1
        print('\033[0m', end = "")
        print(test_counter, end = "/")
        print('\033[92m', end = "")
        print(successfull_counter, end= "/")
        print('\033[91m', end = "")
        print(failed_counter, end= " ")
        print('\033[92m', end = "")
        print('Success', '\033[0m', './s21_grep',flag,file)
    else:
        failed_counter += 1
        print('\033[0m', end = "")
        print(test_counter, end = "/")
        print('\033[92m', end = "")
        print(successfull_counter, end= "/")
        print('\033[91m', end = "")
        print(failed_counter, end= " ")
        print('Fail', '\033[0m', './s21_grep',flag,file)

    # os.system("valgrind --vgdb=no --leak-check=full --show-leak-kinds=all --track-origins=yes  --log-file=test_valgrind ./s21_grep {} {} > a".format(flag,file))
    # os.system("grep ERROR test_valgrind")

    test_counter += 1

def no_file(): 
    os.system("grep {} no_file > test_func_python".format(reg[0]))
    os.system("./s21_grep {} no_file > test_func_python_2".format(reg[0]))
    f1 = "test_func_python"
    f2 = "test_func_python_2"
    print_result(filecmp.cmp(f1, f2, shallow=False), reg[0], "no_file")

def zero_flag():
    for j in range(len(files)):
        for i in range(len(reg)):
            os.system("grep {} {}> test_func_python".format(reg[i],files[j]))
            os.system("./s21_grep {} {}> test_func_python_2".format(reg[i],files[j]))
            f1 = "test_func_python"
            f2 = "test_func_python_2"
            print_result(filecmp.cmp(f1, f2, shallow=False), reg[i], files[j])

def one_flag():
    i = 0
    while i < len(flags):
        a = 0 
        while a < len(reg):
            for j in range(len(files)):
                os.system("grep {} {} {}> test_func_python".format(flags[i], reg[a], files[j]))
                os.system("./s21_grep {} {} {}> test_func_python_2".format(flags[i], reg[a], files[j]))
                f1 = "test_func_python"
                f2 = "test_func_python_2"
                flags_print = "{} {}".format(flags[i], reg[a])
                print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
            a += 1
        i += 1


def three_flags():
    i = 0
    while i < len(flags) - 2:
        k = i + 1
        while k < len(flags) - 1:
            h = k + 1
            while h < len(flags):
                a = 0
                while a < len(reg):
                    for j in range(len(files)):
                        os.system("grep {} {} {} {} {}> test_func_python".format(flags[i], flags[k], flags[h], reg[a], files[j]))
                        os.system("./s21_grep {} {} {} {} {}> test_func_python_2".format(flags[i], flags[k], flags[h], reg[a], files[j]))
                        f1 = "test_func_python"
                        f2 = "test_func_python_2"
                        flags_print = "{} {} {} {}".format(flags[i], flags[k], flags[h], reg[a])
                        print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
                    a += 1
                h += 1
            k += 1
        i += 1

def not_existed_flag():
    os.system("grep -z a {}> test_func_python".format(files[0]))
    os.system("./s21_grep -z a {}> test_func_python_2".format(files[0]))
    f1 = "test_func_python"
    f2 = "test_func_python_2"
    print_result(filecmp.cmp(f1, f2, shallow=False), "-z a", files[0])

def one_eflag():
    i = 0
    while i < len(flags):
        a = 0 
        while a < len(reg):
            for j in range(len(files)):
                os.system("grep {} -e {} {}> test_func_python".format(flags[i], reg[a], files[j]))
                os.system("./s21_grep {} -e {} {}> test_func_python_2".format(flags[i], reg[a], files[j]))
                f1 = "test_func_python"
                f2 = "test_func_python_2"
                flags_print = "{} -e {}".format(flags[i], reg[a])
                print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
            a += 1
        i += 1

def eflags():
    i = 0
    while i < len(flags):
        a = 0 
        while a < len(reg) -1:
            k = a + 1
            while k < len(reg):
                for j in range(len(files)):
                    os.system("grep {} -e {} -e {} {}> test_func_python".format(flags[i], reg[a], reg[k], files[j]))
                    os.system("./s21_grep {} -e {} -e {} {}> test_func_python_2".format(flags[i], reg[a], reg[k], files[j]))
                    f1 = "test_func_python"
                    f2 = "test_func_python_2"
                    flags_print = "{} -e {} -e {}".format(flags[i], reg[a], reg[k])
                    print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
                k += 1
            a += 1
        i += 1

def one_flag_bonus():
    i = 0
    while i < len(flags_bonus):
        a = 0 
        while a < len(reg):
            for j in range(len(files)):
                os.system("grep {} {} {}> test_func_python".format(flags_bonus[i], reg[a], files[j]))
                os.system("./s21_grep {} {} {}> test_func_python_2".format(flags_bonus[i], reg[a], files[j]))
                f1 = "test_func_python"
                f2 = "test_func_python_2"
                flags_print = "{} {}".format(flags_bonus[i], reg[a])
                print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
            a += 1
        i += 1

def three_flags_bonus():
    i = 0
    while i < len(flags_bonus) - 2:
        k = i + 1
        while k < len(flags_bonus) - 1:
            h = k + 1
            while h < len(flags_bonus):
                a = 0
                while a < len(reg):
                    for j in range(len(files)):
                        os.system("grep {} {} {} {} {}> test_func_python".format(flags_bonus[i], flags_bonus[k], flags_bonus[h], reg[a], files[j]))
                        os.system("./s21_grep {} {} {} {} {}> test_func_python_2".format(flags_bonus[i], flags_bonus[k], flags_bonus[h], reg[a], files[j]))
                        f1 = "test_func_python"
                        f2 = "test_func_python_2"
                        flags_print = "{} {} {} {}".format(flags_bonus[i], flags_bonus[k], flags_bonus[h], reg[a])
                        print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
                    a += 1
                h += 1
            k += 1
        i += 1

def one_fflag():
    i = 0
    while i < len(flags_bonus):
        a = 0 
        while a < len(reg):
            for j in range(len(files)):
                os.system("grep {} -f TestFile1 {}> test_func_python".format(flags_bonus[i], files[j]))
                os.system("./s21_grep {} -f TestFile1 {}> test_func_python_2".format(flags_bonus[i], files[j]))
                f1 = "test_func_python"
                f2 = "test_func_python_2"
                flags_print = "{} -f TestFile1".format(flags_bonus[i])
                print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
            a += 1
        i += 1


# U can delete some func from here if u dont want test some cases

main_part()
# bonus_part()

os.remove("test_func_python")
os.remove("test_func_python_2")