def comment_rem(path_base,path_comless):
 file=open(path_base,"r")
 file2=open(path_comless,"w")
 str=file.read() #to read file
 i=0
 k=0
# print("Before # Comment Removal\n")
# print(str)
# print("\nAfter # Comment Removal\n")
 while(i!=len(str)):
     if(str[i]=='\"' and str.startswith("\"\"",i+1)): #to remove block comments
         if(str.find("\"\"\"",i+3)!=-1):
          k=str.find("\"\"\"",i+3)
          i=k+3
         else:
             print("Error!!! Comment not closed")
             
     elif(str.startswith("#",i) and str[i+1]!="\"" and str[i+1]!="\'"): #to remove # comments
      k=str.find("\n",i)
      i=k+1
     else: #to print remaining code
         #print(str[i],end='')
         file2.write(str[i])
         i=i+1
 file.close()
 file2.close()


