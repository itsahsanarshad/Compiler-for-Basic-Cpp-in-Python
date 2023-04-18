
class syntax:
 id_const={"Int_Const":True , "Flt_Const" : True ,"Str_Const":True,"Ch_Const" : True, "ID": True , "Bool_Const":True}

 def class_part (self,token,path):
    file=open(path,"a")
    cp = token[0]
    file.write(cp)
    file.write("\n")
    file.close()

    
 def check_decl(self,start_line_num, lines):
    if "DT"in lines[start_line_num] :
      if "ID" in lines[start_line_num+1]:
          if "Aop" in lines[start_line_num+2]:
            if  syntax.id_const[lines[start_line_num + 3].strip()]:
              if ";" in lines[start_line_num + 4]:
                end_line_num = start_line_num + 4
                return end_line_num
              else:
                print("expected ;")
                return -1
            else:
             print("expected Const")
             return -1
          elif ";" in lines[start_line_num+2]:
              end_line_num= start_line_num+2
              return end_line_num
          else:
           print("expected Aop or ;")
           return -1
 def check_assign(self,start_line_num, lines):
    if "ID"in lines[start_line_num] :
          if "Aop" in lines[start_line_num+1]:
            if syntax.id_const[lines[start_line_num + 2].strip()]:
              if ";" in lines[start_line_num + 3]:
                end_line_num = start_line_num + 3
                return end_line_num
              else:
                print("expected ;")
                return -1
            else:
             print("expected Const")
             return -1
          elif "IncDec" in lines[start_line_num+1]:
              if ";" in lines[start_line_num+2]:
                  end_line_num = start_line_num + 2
                  #print("Increment or Decrement Structure found")
                  return end_line_num
          else:
           print("expected Aop or INCDEC")
           return -1
    else:
           print("expected ID")
           return -1

 def check_else(self,start_line_num,lines):
    if "else" in lines[start_line_num]:
        if "RParen" in lines[start_line_num + 1] and "LParen" not in lines[start_line_num + 2]:
                end_line_num_body=syntax.check_body(self,start_line_num + 2,lines)
                if end_line_num_body != -1:
                        end_line_num = end_line_num_body
                        return end_line_num 
                     
                elif "LParen" in lines[start_line_num + 2]:
                        end_line_num = start_line_num + 2
                        return end_line_num
                else:
                        print("expected }")
                        return -1
        else:
                        print("expected {")
                        return -1
            
    else:
        print("Expected else")
        return -1
     
 def check_if(self,start_line_num, lines):
    if "if" in lines[start_line_num]:
        if "RRdBrac" in lines[start_line_num + 1]:
          if syntax.id_const[lines[start_line_num + 2].strip()]:
            if "RO" in lines[start_line_num+3]:
              if syntax.id_const[lines[start_line_num + 4].strip()]:
                if "LRdBrac" in lines[start_line_num + 5]:
                  if "RParen" in lines[start_line_num + 6] and "LParen" not in lines[start_line_num + 7]:
                    end_line_num_body=syntax.check_body(self,start_line_num + 7,lines)
                    if end_line_num_body != -1:
                        start_line_num = end_line_num_body
                        if "LParen" in lines[start_line_num + 1] and "else"  not in lines[start_line_num + 2] :
                          end_line_num = start_line_num + 1
                          return end_line_num
                        if "LParen" in lines[start_line_num + 1] and "else"  in lines[start_line_num + 2] :
                          end_line_num=syntax.check_else(self,start_line_num+2,lines)
                          if end_line_num != -1:
                           print(f"Correct if else found at line {start_line_num+1} and ends at {end_line_num + 1}")
                           return end_line_num
                        else:
                           print("No correct if else structure found")    
                           return -1
      
                     
                  elif "LParen" in lines[start_line_num + 7] and "else"  not in lines[start_line_num + 8] :
                        end_line_num = start_line_num + 7
                        return end_line_num
                  elif "LParen" in lines[start_line_num + 7] and "else"  in lines[start_line_num + 8] :
                        end_line_num=syntax.check_else(self,start_line_num+8,lines)
                        if end_line_num != -1:
                          print(f"Correct if else found at line {start_line_num+1} and ends at {end_line_num + 1}")
                          return end_line_num
                        else:
                           print("No correct while loop found")    
                           return -1
                  else:
                        print("expected }")
                        return -1
                else:
                        print("expected {")
                        return -1
            else:
                        print("expected )")
                        return -1
        else:
                        print("expected (")
                        return -1
    else:
        print("Expected if")
        return -1


 def check_for_loop(self,start_line_num, lines):
    if "for" in lines[start_line_num]:
        if "RRdBrac" in lines[start_line_num + 1]:
            if "LRdBrac" in lines[start_line_num + 2]:
                if "RParen" in lines[start_line_num + 3] and "LParen" not in lines[start_line_num + 4]:
                    end_line_num_body=syntax.check_body(self,start_line_num + 4,lines)
                    if end_line_num_body != -1:
                        end_line_num = end_line_num_body
                        return end_line_num 
                     
                elif "LParen" in lines[start_line_num + 4]:
                        end_line_num = start_line_num + 4
                        return end_line_num
                    
                else:
                        print("expected { or }")
                        return -1
            else:
                        print("expected )")
                        return -1
        else:
                        print("expected (")
                        return -1
    else:
        print("Expected for")
        return -1
    

 def check_do_while_loop(self,start_line_num, lines):
  if "do" in lines[start_line_num]:
   if "RParen" in lines[start_line_num + 1] and "LParen" not in lines[start_line_num + 2]:
    end_line_num_body=syntax.check_body(self,start_line_num + 2,lines)
    if end_line_num_body != -1:
     start_line_num = end_line_num_body 
                     
     if "LParen" in lines[start_line_num + 1]:
      if "while" in lines[start_line_num + 2]:
       if "RRdBrac" in lines[start_line_num + 3]:
        if syntax.id_const[lines[start_line_num + 4].strip()]:
         if "RO" in lines[start_line_num+5]:
          if syntax.id_const[lines[start_line_num + 6].strip()]:
           if "LRdBrac" in lines[start_line_num + 7]:
            if ";" in lines[start_line_num + 8]:
             end_line_num = start_line_num + 8
             return end_line_num
            else:
                        print("expected ;")
                        return -1
           else:
                        print("expected )")
                        return -1
          else:
                        print("expected Const or Variable")
                        return -1
         else:
                        print("expected RO")
                        return -1
        else:
                        print("expected Const or Variable")
                        return -1   
       else:
                        print("expected (")
                        return -1               
      else:
            print("expected while")
            return -1
    else:
        print("Expected { or }")
        return -1
    
  else:
        print("Expected do")
        return -1

 def check_while_loop(self,start_line_num, lines):
    if "while" in lines[start_line_num]:
        if "RRdBrac" in lines[start_line_num + 1]:
          if syntax.id_const[lines[start_line_num + 2].strip()]:
            if "RO" in lines[start_line_num+3]:
             if syntax.id_const[lines[start_line_num + 4].strip()]:
               if "LRdBrac" in lines[start_line_num + 5]:
                 if "RParen" in lines[start_line_num + 6] and "LParen" not in lines[start_line_num + 7]:
                    end_line_num_body=syntax.check_body(self,start_line_num + 6,lines)
                    if end_line_num_body != -1:
                        end_line_num = end_line_num_body
                        return end_line_num 
                     
                 elif "LParen" in lines[start_line_num + 7]:
                        end_line_num = start_line_num + 7
                        return end_line_num
                    
                 else:
                        print("expected { or }")
                        return -1
                    
               
               else:
                        print("expected )")
                        return -1
             else:
                        print("expected Const or Variable")
                        return -1
            else:
                        print("expected RO")
                        return -1   
          else:
                        print("expected Const or variable")
                        return -1               
        else:
            print("expected (")
            return -1
    else:
        print("Expected while")
        return -1
 def check_body(self,start_line_num, lines):
       syn=syntax()
       i=start_line_num
       line_num=0
       while i < len(lines):
        line_num=i
        line=lines[i]
        if "while" in line:
            end_line_num = syn.check_while_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct while loop found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                line_num=i
                return end_line_num
            else:
                print("No correct while loop found")  
                return -1
                
        if "for" in line:
            end_line_num = syn.check_for_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct for loop found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
                
            else:
                print("No correct for loop found")
                return -1
        if "do" in line:
            end_line_num = syn.check_do_while_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct do while loop found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
                
            else:
                print("No correct Do while loop found")
                return -1
        if "if" in line:
            end_line_num = syn.check_if(line_num, lines)
            if end_line_num != -1:
                print(f"Correct if structure found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
                
            else:
                print("No correct if structure found")
                return -1
        if "DT" in line:
         if "main" in lines[i+1]:
             i+=1
             continue
         elif "ID" in lines[i+1]:
             end_line_num = syn.check_decl(line_num, lines)
             if end_line_num != -1:
                print(f"Correct Decl or Init structure found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
            
             else:
                print("No correct Decl found")
                return -1
        if "ID" in line:
            end_line_num = syn.check_assign(line_num, lines)
            if end_line_num != -1 and end_line_num!=line_num+2:
                print(f"Correct Assign structure found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
            elif end_line_num==line_num+2:
                print(f"Correct INCDEC Structure found at line {i+1} and ends at {end_line_num + 1}")
                i=end_line_num
                return end_line_num
                
            else:
                print("No correct Init structure found")
                return -1
        
        if "}" in line:
            i+=1
            end_line_num=i
            return end_line_num
            
        else:
            i+=1
        

 def check_struct(self,start_line_num, lines):
     if "struct" in lines[start_line_num]:
           if "RParen" in lines[start_line_num+1] and "LParen" not in lines[start_line_num + 2]:
              end_line_num_body=syntax.check_body(self,start_line_num + 2,lines)
              if end_line_num_body != -1:
                        start_line_num = end_line_num_body
                        if "LParen" in lines[start_line_num+1]:
                         if ";" in lines[start_line_num+2]:
                            end_line_num = start_line_num + 2
                            return end_line_num
                         else:
                            print("Expected ;")
                            return -1
                        else:
                            print("Expected }")
                            return -1
                     
           elif "LParen" in lines[start_line_num+2]:
               if ";" in lines[start_line_num+3]:
                    end_line_num = start_line_num + 3
                    return end_line_num
               else:
                    print("Expected ;")
                    return -1
           else:
                    print("Expected }")
                    return -1
     else:
                    print("Expected struct")
                    return -1
 def check_syntax(self):
  path_cp_file = "D:\Compiler for Basic C++\Compiler For Basic C++\Cp.txt"
  syn=syntax()
  line_num =0
  i=0
  with open(path_cp_file, 'r') as f:
    lines = f.readlines()
    while i < len(lines):
        line_num=i
        line=lines[i]
        if "while" in line:
            end_line_num = syn.check_while_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct while loop found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                line_num=i
            else:
                print("No correct while loop found")    
                break
        if "for" in line:
            end_line_num = syn.check_for_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct for loop found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                
            else:
                print("No correct for loop found")
                break
        if "do" in line:
            end_line_num = syn.check_do_while_loop(line_num, lines)
            if end_line_num != -1:
                print(f"Correct do while loop found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                
            else:
                print("No correct Do while loop found")
                break
        if "if" in line:
            end_line_num = syn.check_if(line_num, lines)
            if end_line_num != -1:
                print(f"Correct if structure found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                
            else:
                print("No correct if structure found")
                break
        if "DT" in line:
         if "main" in lines[i+1]:
             i+=1
             continue
         elif "ID" in lines[i+1]:
             end_line_num = syn.check_decl(line_num, lines)
             if end_line_num != -1:
                print(f"Correct Decl or Init structure found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
            
             else:
                print("No correct Decl found")
                break
        if "ID" in line:
            end_line_num = syn.check_assign(line_num, lines)
            if end_line_num != -1 and end_line_num!=line_num+2:
                print(f"Correct Assign structure found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
            elif end_line_num==line_num+2:
                print(f"Correct INCDEC Structure found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                
            else:
                print("No correct Init structure found")
                break
        if "struct" in line:
            end_line_num = syn.check_struct(line_num, lines)
            if end_line_num != -1:
                print(f"Correct struct found at line {i+1} and ends at {end_line_num + 2}")
                i=end_line_num
                
            else:
                print("No correct struct structure found")
                break
        if "$" in line:
            i+=1
        else:
            i+=1
    print(f'Code has checked file till line number {line_num+1}')
