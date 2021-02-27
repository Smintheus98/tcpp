#!/usr/bin/env python3

import re
import os
import sys
import datetime

AUTHOR = "Yannic Kitten"

pattern_classname       = r"^[a-zA-Z_]([a-zA-Z0-9_])*(.cpp|.h)?$"
pattern_mainfilename    = r"^[a-zA-Z_]([a-zA-Z0-9_])*(.cpp|.c)?$"
pattern_normalfilename  = r"^[a-zA-Z_]([a-zA-Z0-9_])*(.cpp|.c|.h)@$"

c_style_flag            = False
force_overwrite_flag    = False

class_list              = []
main_list               = []
normal_list             = []

def error_message(errmsg):
    print(" ERROR:", errmsg)
    print("     Try option '--help' for more intormation")
    sys.exit(1)

def warning_message(warnmsg, scndline = ""):
    print(" WARNING:", warnmsg)
    if len(scndline) > 0:
        print("    ", scndline)
    
def help_message():
    print("\ntcpp - Generator for C/C++ template files\n")
    print("Usage:")
    print("  bash tcpp [OPTIONS]\n")
    print("Options:")
    print("  -h --help                            Shows this help message and exits")
    print("  -C --C-style                         Uses C-standard instead of C++-standard")
    print("                                       Is ignored in modes 'class' and 'multiple'")
    print("  -f --force                           Overwrites files that already exists")
    print("  -c CLASSNAME --class=CLASSNAME       Creates header and source templates for class")
    print("                                       if they do not exist already")
    print("                                       Files are named like class")
    print("  -m SOURCEFILE --main=SOURCEFILE      Creates sourcefile template for main-program")
    print("  -l F1 [...] --multiple=\"F1 [...]\"    Creates multiple files depending on suffix")
    print("                                       Using '-l' it must be last option in line")
    print("Examples:")
    print("  ./tcpp -c ClassName  -  creates files ClassName.h and ClassName.cpp if they does not exist")
    print("  ./tcpp -m main.cpp  -  creates main.cpp file that is an main-program")
    print("  ./tcpp --force -l file1.c file2.cpp file3.c file4.h  -  creates/overwrites files")
    
def build_file_header(ffname):
    header = ""
    header += "/*\n"
    header += " *   " + ffname + "\n"
    header += " *\n"
    header += " * Created on: " + datetime.datetime.now().strftime("%^b %d, %Y") + "\n"
    header += " *     Author: " + AUTHOR + "\n"
    header += " */\n"
    return header

def build_main_body(ffname):
    body = ""
    if ffname.endsWith(".c"):
        body += "#include <stdio.h>\n\n"
    else:
        body += "#include <iostream>\n\n"
        body += "using namespace std;\n\n"
    body += "int main(int argc, char* argv[]) {\n"
    body += "    \n"
    body += "    return 0;\n"
    body += "}"
    return body

def build_class_body(ffname):
    cname, suffix = ffname.split(".")[0:2]
    body = ""
    if suffix == h:
        body += "#pragma once\n\n"
        body += "class " + cname + " {\n"
        body += "    private:\n"
        body += "        \n"
        body += "    public:\n"
        body += "        " + cname + "();\n"
        body += "        ~" + cname + "();\n"
        body += "\n"
        body += "        \n"
        body += "};\n"
    else:   # cpp
        body += "#include \"" + cname + ".h\"\n\n"
        body += cname + "::" + cname + "() {\n"
        body += "    \n"
        body += "}\n"
        body += "\n"
        body += cname + "::~" + cname + "() {\n"
        body += "    \n"
        body += "}\n"
        pass
    return body

def build_normal_body(ffname):
    fname, suffix = ffname.split(".")[0:2]
    body = ""
    if suffix == h:
        body += "#pragma once\n\n"
    elif suffix == cpp:
        body += "#include <iostream>\n\n"
        body += "using namespace std;\n\n"
    elif suffix == c:
        body += "#include <stdio.h>\n\n"
    return body

def build_class(name):
    cname = name.split(".")[0]
    suffix = "" if len(name.split(".")) <= 1 else name.split(".")[1]
    fnames = []
    count_error = 0
    if suffix:
        fnames.append(cname + ".h")
        fnames.append(cname + ".cpp")
    else:
        fnames.append(cname + suffix)

    for fname in fnames:
        pass

def build_main(fname):
    pass

def build_normal(fname):
    pass

def main():
    pass
