record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]

file = open('register.txt','w')
'''
for n in record_last_session:
    file.writelines(n + '\t')
'''
file.writelines(["John\t", "12/20/2022\t", "08:17:32 pm\t", "No loading errors\t"])
file.close()

file = open('register.txt','r')
print(file.read())
file.close()
'''
record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]
file = open("register.txt", "a")
file.writelines("\t".join(record_last_session))
file.close()
file = open("register.txt", "r")
print(file.read())
'''
