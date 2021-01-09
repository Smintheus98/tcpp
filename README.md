# tcpp
A script for generic C and CPP file generation

## Usage Examples

For getting a help menu type
```
bash tcpp -h
```
To create a new class with generated header and source files type
```
./tcpp -c myclass       # -> myclass.h myclass.cpp
```
For generating a main-program type
```
./tcpp -m main.cpp      # -> main.cpp
./tcpp -m main -f       # -> overwriting main.cpp
./tcpp -m main -C       # -> main.c
./tcpp -m main.c -f     # -> overwriting main.c
```
For generating multiple independent and generic files type
```
./tcpp -l file1.h file2.c file3.cpp
```
This is the only option really requiring file-suffixes (.c,.cpp,.h).
When using with other options this one needs to be the last or use the other option syntax.

### TODO
* port script to easier language (Python or Nim)
* export files structures to object notation files for easier changes (XML or JSON)
