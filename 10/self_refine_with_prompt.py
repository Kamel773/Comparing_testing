
import subprocess
import shlex

def execute_command(command):
    # Split the command into a list of arguments
    command_list = shlex.split(command)
    process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return process.returncode, output, error
