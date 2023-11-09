
def log_error(directory):
    file = open(directory, 'a')
    file.write("an execution error has been registered")
    file.close()
