file = open('my_file.txt','a')
file.write("New login")
file.close()

file = open('my_file.txt','r')
print(file.read())
file.close
