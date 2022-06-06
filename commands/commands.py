import os

#execute command and print output
def exec_command(command):
    a= []
    with os.popen(command) as pipe:
        for line in pipe:
            a.append(line.strip())
    return a
