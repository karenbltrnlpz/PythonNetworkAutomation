# ABSOLUTE AND RELATIVE PATHS

# Absolute paths are when you specify the location of a
# file/directory from the root directory

# when calling the file by its name only, Python is pulling the file from a
# relative path from the current working directory
# to use a relative path, you need to use double backslashes to point to the slash in the directory

#f = open('C:\\Users\\belka\\PycharmProjects\\NetworkAutomation\\settings.txt')

# you can also use the RAAS string marked by the r to treat back slashes as literal
# there are also helpful for regular expression patterns
f = open(r'C:\Users\belka\PycharmProjects\NetworkAutomation\settings.txt')

# . => current working directory

# .. => parent directory

#current directory
open('./settings.txt')