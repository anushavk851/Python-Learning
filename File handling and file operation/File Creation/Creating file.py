#FILE HANDLING/FILE OPERATIONS
  
#create file
#f=open("student.txt","x")
#f.close()

#adding content
# f=open("student.txt","a")    #output-anusha
# f.write("Anusha")
# f.close()

# #reading file
# f=open("student.txt","r")
# data=f.read()
# print(data)
# f.close()

#adding another content
# f=open("student.txt","a")          #output-anusha                                             
# f.write("\nrahul")                         rahul
# f.close()

#writing mode
# f=open("student.txt","w")                                                      
# f.write("keerthana")          #output became keerthana(the file removes anusha and rahul and only added keerthana when we used write mode)         
# f.close()

#to write in multiple line
#method 1
    # f=open("student.txt","w")                                                      
    # f.write("keerthana")
    # f.write("\narun")   
    # f.write("\namaya")      
    # f.close()

#method 2-creating list of students name.
    # students=["anu\n","anusree\n","bindu\n","anil\n"]
    # f=open("student.txt","w")
    # f.writelines(students)
    # f.close()

#with-context manager ,where file handling will be managed automatically
# name=input("enter a name: ")
# with open("student.txt","a") as f:
#     #print(f.read())
#     f.write("\n"+name)
# print("name saved")

# with open(r"C:\Users\ACCURATE\Desktop\demp.txt","r") as f:            #to create a file of external folder copy the path of folder
#     print(f.read())
