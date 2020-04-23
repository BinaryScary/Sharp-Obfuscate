import os
import sys
import string
import re
import random
import argparse

# change to accomidate false positives in declarations
blacklist = ["using", "goto"]

# return random obfuscated names
def obfuWord(length=10):
    allLetters = string.ascii_letters
    upLetters = string.ascii_uppercase
    return random.choice(upLetters) + ''.join(random.choice(allLetters) for i in range(length))

# parse function parameters and names
def addFunc(funcLine):
    match = re.findall("([a-zA-Z0-9_]+,|[a-zA-Z0-9_]+\)|[a-zA-Z0-9_]+\()",funcLine)
    variables = []
    for variable in match:
        variables.append(re.sub('(,|\)|\()','',variable))
    return variables
    

def getNames(code):
    # can probably regex over whole text block, but need to check for functions
    lines = code.split('\n')
    variables = []
    for i in lines:
        # check for variable declarations
        match = re.search("^(\t| )*[a-zA-Z0-9_\[\]\<\>]+ [a-zA-Z0-9_]+( |)(;|=)", i)

        # if function extract parameters & name
        if "public" in i:
            variables = variables + addFunc(i)
            continue
        if match != None:
            var = match.group(0)
            # blacklisted words check
            if any(word in var for word in blacklist):
                continue
            else:
                # add declarations, removing ';'
                variables.append(re.sub(';','',var.split()[1]))
    return variables

def obfuscateNames(code,variables):
    obf = code
    for var in variables:
        # soft check if string is less then 5 long remove
        if len(var) <= 5:
            continue
        # check for non encapsulated word
        obf = re.sub("( |\)|\.|\(|\[|,|\t{1})"+var+"( |\-|\+|\.|\n|\(|\)|;|,|=|\[|\]|\t{2})",r"\1"+obfuWord()+r"\2",obf)
    return obf


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Obfuscate C# Function,Parameter, and Variable names')
    # required not needed for positional (none flag) arguments
    parser.add_argument('filename',metavar='File',type=str)
    parser.add_argument('-o', metavar='OutFile',type=str)
    args = parser.parse_args()

    try:
        with open(args.filename,'r') as myfile:
            code = myfile.read()
    except:
        print("[!] Error opening %s" % args.filename)
        quit()

    variables = getNames(code)

    obf = obfuscateNames(code,variables)

    if args.o == None:
        print(obf)
    else:
        try:
            f = open(args.o, "a")
            f.write(obf)
        except:
            print("[!] Error writing to %s" % args.o)
            print("[-] Printing obfuscated code\n")
            print(obf)