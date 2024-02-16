# reading and writing to files, we don't need to import modules in Python
# 3 because it handles it natively

# built in open function which opens files and returns a file
# object. The function takes in an argument which is the name of the text
# file you can have the text files within the same directory to be able to easily
# open the file (absolute/relative paths need to be passed into the function)
# there is a second optional argument that tells the OS what mode the file should be opened
# in, read, write or append. 'read' is read only and is the default mode.

#Text files - sequence of line encoded in UTF-8, the lines are terminated with
# \n or EOL (end of line)

# binary files like PDF, Excel, video, and audio files use specific apps to open them

# storing the object in variable named 'f' and the objects
# methods/attributes to manipulate the file that you want to open
# 'rt' to open text file in read only or 'rb' to open binary files
f = open('configuration.txt', 'rt')

# use read() method to read the contents of the file
content = f.read()
print(content)

# to know if the file is open or closed. If open, this will return False
print(f.closed)

# good idea to always close a file after reading/using it
f.close()
print(f.closed)