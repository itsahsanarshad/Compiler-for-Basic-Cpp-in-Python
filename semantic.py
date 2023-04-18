import re
file=open("D:\Compiler for Basic C++\Compiler For Basic C++\code_comless.txt","r")
inp=file.read()
dt=['nil',
'bin',
'str',
'alpha',
'lfract',
'fract',
'integer']
tab=[]
tok=[]
tok=inp.split(' ')


def check_type_mismatch(code): 
  pattern = re.compile(r'(integer|fract|lfract|alpha|str|bin)\s+\w+\s*(=\s*\S+)?(,|;)')
 
  lines = code
  found_mismatch = False
 
  for line in lines:
 
    match = pattern.search(line)
    if match:
      
      variable_type = match.group(1)
      variable_value = match.group(2)

      if variable_value:      
        variable_value = variable_value.strip('= ')
      
        if (variable_type == 'integer' and not variable_value.isdigit()) or \
           (variable_type == 'fract' and not variable_value.replace('.', '', 1).isdigit()) or \
           (variable_type == 'lfract' and not variable_value.replace('.', '', 1).isdigit()):
      
          found_mismatch = True
          print(f'Type mismatch in declaration: {line}')
        elif variable_type == 'alpha' and not (variable_value.startswith("'") and variable_value.endswith("'")):
          found_mismatch = True
          print(f'Type mismatch in declaration: {line}')
        elif variable_type == 'str' and not (variable_value.startswith('"') and variable_value.endswith('"')):
          found_mismatch = True
          print(f'Type mismatch in declaration: {line}')

  return found_mismatch





def lookup(name,scope):
    i=0
    if len(tab)!=0:
        while(i<len(tab)):
            if name in tab[i] and scope in tab[i]:
                return False
            else:
                i+=1
        return True
    else:
        return True

def insert(name,typee,scope):
    tab.append([name,typee,scope])

def main():
    error=False
    flag=True
    scopee=1
    i=0
    while(i<len(tok)):
        if tok[i]=='{':
            flag=True
        scopee =scopee+1
        i+=1
        while(i<len(tok) and flag==True):
            namee=""
            tipe=""
            if tok[i] in dt:
                tipe=tok[i]
                i+=1
                if re.match('^[a-zA-Z]+$',tok[i]):
                    namee=tok[i]
                    if lookup(namee,scopee):
                        insert(namee,tipe,scopee)
                    else:
                        print("ERROR:",namee," is already defined at scope",scopee)
                        error=True
                i+=1
                if tok[i]=='=':
                    None
                    i+=1
                    if tok[i-3]=='integer' and re.match('^[0-9]+$',tok[i]):
                        i+=1
                    elif tok[i-3]=='alpha' and re.match("^'[A-Za-z0-9]'$",tok[i]):
                        i+=1
                    else:
                        print("ERROR:",namee,"'s Datatype Mismatch at scope",scopee)
                        error=True
                        i+=1
                if tok[i]==';':
                    i+=1
                else:
                    print("ERROR:",namee,"'s Terminator missing at scope",scopee)
                    error=True
                if tok[i]=='}':
                    i+=1
                    scopee = scopee-1
                    flag=False
            elif re.match('^[a-zAZ]+$',tok[i]):
                print("ERROR:",tok[i]," is not Declared as scope",scopee)
                error=True
                i+=1
            else:
                i+=1
        else:
            i+=1
    if(not error):
        print("No Error Found!!!")
 
