# COMP 211 Final Project: Tar Heel Shell
Simple "Tar Heel" shell! The shell specified is merely capable of changing directories and executing system programs such as `pwd` and `ls`. The goal of this assignment is to familiarize myself with system-related library functions.

## Project Structure
Four files are included in this project:
* `Makefile`- contains information used to compile your program with the `make` command.
* `shell.h`- includes declarations and specifications for all of the functions in `shell.c`.
* `shell.c`- contains function definitions for all functions in `shell.c`. In particular, your goal for this assignment will be to implement `find_fullpath` and `execute`.
* `driver.c`- contains the main function, which is just a loop that reads in a command and uses the functions written in `shell.c` to determine whether the command is valid and handle it appropriately.
