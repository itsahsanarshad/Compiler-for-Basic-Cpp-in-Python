import re
from comment_rem import comment_rem
from syntax import syntax

# List of C++ keywords
keywords = [
'null',	
'default',	
'goto']

DT=[ 'nil',
'bin',
'str',
'alpha',
'lfract',
'fract',
'integer']

# Regular expressions for identifying different types of tokens
identifier_regex = r'[a-zA-Z_][a-zA-Z0-9_]*'
invalid_identifier_regex=r"[^a-zA-Z_$][a-zA-Z0-9_$]*"
integer_regex = r'\d+'
string_regex = r'"(?:\\.|[^\\"])*"'
char_regex = r'\'(?:\\.|[^\\\'])*\''
punctuation_regex = r'[{}()\[\];,\.<>=+-/*%&|^!]'
operator_regex = r'&&|\|\||\+\+|--|[!=]=|[+\-/*%&|^<>]'
float_regex = r'[+-]?[0-9]+\.[0-9]+'    

# Combine all regular expressions into a single pattern
token_pattern = r'(\s+)|'+ '|'.join([ identifier_regex,float_regex, integer_regex, string_regex, char_regex,operator_regex, punctuation_regex])


def lexer(code):
    # Split the code into lines
    lines = code.split('\n')
    
    # Keep track of the current line number
    line_number = 1
    # Iterate through the lines of code
    for line in lines:
        # Use the regular expression to find all tokens in the line
        match = re.match(token_pattern, line)
        while match:
            token = match.group(0)
            if token in keywords:
                yield ('KW', token, line_number)
            elif token=='while':
                yield ('while', token, line_number)
            elif token=='for':
                yield ('for', token, line_number)
            elif token=='do':
                yield ('do', token, line_number)
            elif token=='if':
                yield ('if', token, line_number)
            elif token=='else':
                yield ('else', token, line_number)
            elif token=='write':
                yield ('write', token, line_number)
            elif token=='read':
                yield ('read', token, line_number)
            elif token=='struct':
                yield ('struct', token, line_number)
            elif token=='break':
                yield ('break', token, line_number)
            elif token=='switch':
                yield ('switch', token, line_number)
            elif token=='case':
                yield ('case', token, line_number)
            elif token=='return':
                yield ('return', token, line_number)
            elif token=='main':
                yield ('main', token, line_number)
            elif token.isdigit():
                yield ('Int_Const', token, line_number)
            elif '.' in token:
                yield ('Flt_Const', token, line_number)
            elif token in DT:
                yield ('DT', token, line_number)
            elif token.startswith('\"'):
                yield ('Str_Const', token, line_number)
            elif token.startswith('\''):
                yield ('Ch_Const', token, line_number)
            elif token in ['&&']:
                yield ('And Operator', token, line_number)
            elif token in ['||']:
                yield ('Or Operator', token, line_number)
            elif token in ['!']:
                yield ('Not Operator', token, line_number)
            elif token in ['=', '+=', '-=', '*=', '/=','%=']:
                yield ('Aop', token, line_number)
            elif token in ['{']:
                yield ('RParen', token, line_number)
            elif token in ['}']:
                yield ('LParen', token, line_number)
            elif token in ['[']:
                yield ('RSqBrac', token, line_number)
            elif token in [']']:
                yield ('LSqBrac', token, line_number)
            elif token in ['(']:
                yield ('RRdBrac', token, line_number)
            elif token in [')']:
                yield ('LRdBrac', token, line_number)
            elif token in [';']:
                yield (';', token, line_number)
            elif token in ['.']:
                yield ('Dot', token, line_number)
            elif token in [',']:
                yield ('comma', token, line_number)
            elif token in ['!=', '==', '<', '>', '<=', '>=']:
                yield ('RO', token, line_number)
            elif token in ['+', '-']:
                yield ('AddSub', token, line_number)
            elif token in ["++", '--']:
                yield ('IncDec', token, line_number)
            elif token in ['*', '/', '%']:
                yield ('DivMul Operator', token, line_number)
            elif token.isspace():
                print("",end="")
            elif token == "true" or token=="false":
                yield ('Bool_Const', token, line_number)
            else:
                yield ('ID', token, line_number)
            line = line[match.end():]
            match = re.match(token_pattern, line)
        if line.strip():
            yield 'error'
            yield ('ERROR', f"Invalid token found on line {line_number}",line.strip())
            break
            
            
        line_number += 1	


def class_part (token,path):
    file=open(path,"a")
    cp = token[0]
    file.write(cp)
    file.write("\n")
    file.close()



path_base_file="D:\Compiler for Basic C++\Compiler For Basic C++\code.txt"
path_comless_file="D:\Compiler for Basic C++\Compiler For Basic C++\code_comless.txt"
path_token_file="D:\Compiler for Basic C++\Compiler For Basic C++\lexer.txt"
path_cp_file="D:\Compiler for Basic C++\Compiler For Basic C++\Cp.txt"
comment_rem(path_base_file,path_comless_file)
file_comless=open(path_comless_file,"r")
string_comless=file_comless.read()
file_comless.close()
file_token=open(path_token_file,"w")
file_cp=open(path_cp_file,"a")
file_cp.truncate(0)
file_cp.close()
file=open(path_comless_file,"r")
inp=file.read()

for token in lexer(string_comless):
   if token == 'error':
    print("Lexical Error Reported")
    file_token.truncate(0)
   else: 
    file_token.write(str(token))
    file_token.write("\n")
    class_part(token,path_cp_file)
from semantic import main,check_type_mismatch
syn=syntax()
file_token.close()
syn.check_syntax()
main()
if check_type_mismatch(inp.split(' ')):
  print('Type mismatch found')
else:
  print('No type mismatch')
    
 