# open() function will open a file and return it
file = open("my_file.txt")
# read() will read the complete file and return its contents as string
content = file.read()
print(content)
# Its always good to close the resources once you're done
file.close()
