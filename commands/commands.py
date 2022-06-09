import os
import subprocess as sp

def exec_command_need(command):
    output = sp.getoutput(command)
    return output

def exec_command(command):
    output = sp.getoutput(command)
    if output.startswith('Error'):
        return output
    else:
        return True
