import os
#Operating module that lets program interact with operating system.

# getcwd()--Returns current working directory.
print(os.getcwd())

# listdir()--Lists files and folders.
print(os.listdir())

# mkdir()--Creates a new directory.
#os.mkdir("DemoFolder")

# makedirs()--Creates multiple directories.
#os.makedirs("Folder1/Folder2")

# rmdir()--Removes a directory.
#os.rmdir("DemoFolder")

# remove()--Deletes a file.
#os.remove("sample.txt")

# rename()--Renames a file or folder.
#os.rename("old.txt", "new.txt")

# chdir()--Changes current directory.
#os.chdir(".")

# path.exists()--Checks if a path exists.
print(os.path.exists("."))

# system()--Executes a system command.
print("\n10. system()")
if os.name == "nt":      # Windows
    os.system("dir")
else:                    # Linux/macOS
    os.system("ls")





