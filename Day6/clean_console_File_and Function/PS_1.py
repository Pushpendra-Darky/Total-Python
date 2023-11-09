from pathlib import Path

def open_read(directory):

    file = open(directory, 'r')
    return file.read()


dir = Path("C:\Total Python\Day6\clean_console_File_and Function\exc.txt")
ret = open_read(dir)
print(ret)

