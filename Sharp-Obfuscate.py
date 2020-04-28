import os
import sys
import string
import re
import random
import argparse
import codecs
import shutil

# TODO: Bug in Design classes, have to generate to fix?
# blacklist for false positives in declaration (will not search any line including these for names to obfuscate, will also blacklist any vars in those lines)
blacklist = ["using", "goto", "extern","override","partial"]
# blacklist for strings precursors (will not add string precursed with this)
strBlacklist = ['DllImport\(','DllExport\(','\[Guid\(','\[ProgId\('] 
# blacklist for function and parameter names
funcBlacklist = [] 

# is randomly generated and added to string blacklist
decodeFunc = "DecObfu"

# TODO: add a data struct to catch if same obfuscated name is used again
# return random obfuscated names
def obfuWord(length=10):
    allLetters = string.ascii_letters
    upLetters = string.ascii_uppercase
    return random.choice(upLetters) + ''.join(random.choice(allLetters) for i in range(length))

# parse function parameters and names
def addFunc(funcLine):
    match = re.findall("(?<= )(?<!\<)([a-zA-Z0-9_]+,|[a-zA-Z0-9_]+\)|[a-zA-Z0-9_]+\()",funcLine)
        # (?<= ) check if space is present without adding to match
    variables = []
    for variable in match:
        if variable not in funcBlacklist:
            variables.append(re.sub('(,|\)|\()','',variable))
    return variables
    

def getNames(code):
    global blacklist
    # can probably regex over whole text block, but need to check for functions
    lines = code.split('\n')
    variables = []
    for i in lines:
        # blacklisted words check
        if any(word in i for word in blacklist):
            if "public" in i or "private" in i or "protected" in i:
                varTemp = addFunc(i)
                variables = [x for x in variables if x not in varTemp]
                blacklist = list(set().union(blacklist , varTemp))
            # TODO: also add excluded variable declaration to blacklist
            continue

        # if function extract parameters & name
        if "public" in i or "private" in i or "protected" in i:
            variables = list(set().union(variables , addFunc(i)))
            continue

        # check for variable declarations
        match = re.search("^(\t| )*[a-zA-Z0-9_\[\]\<\>]+ [a-zA-Z0-9_]+( |)(;|=)", i)
        if match != None:
            # add declarations, removing ';'
            var = match.group(0)
            var = re.sub(';','',var.split()[1])
            if var not in variables:
                variables.append(var)
    return variables

def strToBytes(s):
    return "-".join("{:02x}".format(ord(c)) for c in s)

# csharp literal strings dereference double quotes to singles
def trimDoubleQuotes(s):
    return re.sub('""','"',s)

def escapeChars(s):
    return codecs.decode(s,"unicode-escape")

# literal string to function call
def litStrToCall(s):
    # s.group(1) returns the first subgroup '()'
    return decodeFunc+'("'+strToBytes(trimDoubleQuotes(s.group(1)))+'")'

# string to function call (escapes characters)
def strToCall(s):
    # s.group(1) returns the first subgroup '()'
    if s.group(1) != "":
        return s.group(0)
    else:
        return decodeFunc+'("'+strToBytes(trimDoubleQuotes(escapeChars(s.group(2))))+'")'

def genRegString(blacklist):
    regPrepend = '(?<!(?:@|"))"(?!")(.*?)(?<!")"(?!")'
    # add words as optionals to the front of regex string
    regex = ""
    for word in blacklist:
        regex += word+'|'
    regex = '('+regex+')'+regPrepend
    return regex

def obfuscateStrings(code):
    # generate decode Function name
    global decodeFunc
    global strBlacklist
    strBlacklist.append(decodeFunc+'\(')

    # decFunc = """
	# public static string %s(string enc){
	# 	String[] arr = enc.Split('-');
	# 	if(arr[0] == ""){return "";}
	# 	byte[] array = new byte[arr.Length];
	# 	for(int i=0; i<arr.Length; i++) array[i]=Convert.ToByte(arr[i],16);
	# 	string dec = Encoding.UTF8.GetString(array);	
	# 	return dec;
	# }
    # """ % decodeFunc
    obf = code
    # TODO: obfuscate obfuscation class name
    # obf = "using static Obfu.Obfu;"+obf
    # obf = "using System.Text;\nusing System;\n"+obf

    # string literal @"" obfuscate
    # calls strToCall function with match-object
    obf = re.sub('@"(?!")((.|\s)*?)(?<!")"(?!")',litStrToCall,obf,re.DOTALL)
        # group 1 (), not include " before or after(?<!")"(?!"), lazy match first occurance .*?, \s include newline

    # generate a regex string with blacklisted words
    regString = genRegString(strBlacklist)
    # normal string "" obfuscate
    # need to be done after literals since multiline screws with reg strings
    obf = re.sub(regString,strToCall,obf)
        # don't capture group (?:)

    # obf = re.sub('(class (?:.|\s)*?{)',r'\1'+"\n\t\t"+decFunc,obf,1)
    return obf

def getFilenames(projNames):
    # determine os type for path syntax
    isPosix = os.name == 'posix'

    filenames = []
    lines = ""
    for name in projNames:
        directory = os.path.dirname(name)
        try:
            with open(name,'r') as myfile:
                lines = myfile.read()
        except:
            print("[!] Error opening %s" % name)
            quit()

        match = re.findall('"([^".]*\.cs)"',lines)
        for fpath in match:
            # TODO: check if obfu works with AssemblyInfo.cs
            # special file AssemblyInfo.cs
            if "AssemblyInfo.cs" in fpath:
                continue

            # append filename
            path = ""
            if isPosix:
                path = os.path.join(directory,fpath.replace("\\",'/'))
            else:
                path = os.path.join(directory,fpath)
            
            if path not in projNames:
                filenames.append(path)

    return filenames

def getProjnames(solutionFile):
    # determine os type for path syntax
    isPosix = os.name == 'posix'

    directory = os.path.dirname(solutionFile)
    try:
        with open(solutionFile,'r') as myfile:
            code = myfile.read()
    except:
        print("[!] Error opening %s" % solutionFile)
        quit()

    # check for project files
    match = re.findall('"([^"]*?\.csproj)"',code)

    projNames = []
    for proj in match:
        # append filename
        path = ""
        if isPosix:
            path = os.path.join(directory,proj.replace("\\",'/'))
        else:
            path = os.path.join(directory,proj)
        
        if path not in projNames:
            projNames.append(path)

    return projNames

def getCode(filenames):
    code = ""
    for name in filenames:
        try:
            with open(name,'r') as myfile:
                code += myfile.read()
        except:
            print("[!] Error opening %s" % name)
            quit()
    return code

def obfuscateNames(code,varObfuMap):
    obf = code
    for var in varObfuMap:
        # soft check if string is less then 5 long remove
        if len(var) <= 5:
            continue
        # check for non encapsulated word i.e: don't replace str in string

        obf = re.sub("( |\)|\.|\(|\[|,|\t|~)"+var+"( |\-|\+|\.|\n|\(|\)|;|,|=|\[|\]|\t)",r"\1"+varObfuMap[var]+r"\2",obf)
    return obf


def genObfuMap(variables):
    varObfuMap = {}
    for i in variables:
        varObfuMap[i] = obfuWord()
    return varObfuMap

def obfuscateFiles(filenames, variables):
    # generate name to obfuscation dictionary
    varObfuMap = genObfuMap(variables)
    # global decodeFunc
    # decodeFunc = obfuWord()

    for name in filenames:
        try:
            with open(name,'r') as myfile:
                obf = myfile.read()
        except:
            print("[!] Error opening %s" % name)
            quit()

        obf = obfuscateNames(obf,varObfuMap)
        obf = obfuscateStrings(obf)

        try:
            f = open(name,"w")
            f.write(obf)
            f.close()
        except:
            print("[!] Error writing to %s" % name)
            quit()

# adds obfuscation file to compilation targets, every proj folder, and file
def addDecoder(projNames,filenames):
    global decodeFunc
    decodeFunc = obfuWord()
    compSig = '<Compile Include='
    compInc = '    <Compile Include="Obfu.cs" />\n'

    for path in projNames:
        # add compile target to project files
        try:
            f = open(path,"r")
            contents = f.readlines()
            f.close()
        except:
            print("[!] Error reading %s" % path)
            quit()
        # enumerate for index and insert new file
        for i, line in enumerate(contents):
            if compSig in line:
                contents.insert(i,compInc)
                break
        try:
            f = open(path,"w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        except:
            print("[!] Error writing %s" % path)
            quit()
            
        # add decoder file to projects
        directory = os.path.dirname(path)
        path = os.path.join(directory,"Obfu.cs")

        # decoder contents
        global strBlacklist
        strBlacklist.append(decodeFunc+'\(')
        contents = """using System;
using System.Text;

namespace Obfu
{
    public class Obfu
    {
        public static string %s(string enc)
        {
            String[] arr = enc.Split('-');
            if (arr[0] == "") { return ""; }
            byte[] array = new byte[arr.Length];
            for (int i = 0; i < arr.Length; i++) array[i] = Convert.ToByte(arr[i], 16);
            string dec = Encoding.UTF8.GetString(array);
            return dec;
        }
    }
}
""" % decodeFunc

        # write decoder to file
        try:
            f = open(path,"w")
            f.write(contents)
            f.close()
        except:
            print("[!] Error writing %s" % path)
            quit()

    for path in filenames:
        with open(path, 'r') as original: data = original.read()
        with open(path, 'w') as modified: modified.write("using static Obfu.Obfu;\n" + data)

def copyProj(solution):
    # create new obfuscated project
    dirOrig = os.path.dirname(solution)
    dirObfu = dirOrig+"Obfucated"
    shutil.copytree(dirOrig,dirObfu)

    return os.path.join(dirObfu,os.path.basename(solution))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Obfuscate C# Function,Parameter, Variable Names and Encode Strings')
    # required not needed for positional (none flag) arguments
    parser.add_argument('filename',metavar='SolutionFile',type=str)
    # parser.add_argument('-o', metavar='OutFile',type=str)
    # parser.add_argument('-s', help='use solution file (.sln)', action='store_true')
    args = parser.parse_args()

    # TODO: probably doesn't work now without solutionfile
    solution = args.filename
    filenames = []
    solution = copyProj(solution)
    # get all project file names 
    projNames = getProjnames(solution)
    filenames = getFilenames(projNames)
    # add decoder file to project
    addDecoder(projNames,filenames)

    # get code from all files
    allCode = getCode(filenames)
    
    # get all variable, function, and param names
    variables = getNames(allCode)

    # obfuscate
    obfuscateFiles(filenames,variables)
