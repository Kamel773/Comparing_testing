
import subprocess

def execute_command(command):
    # Use a list of arguments instead of a string to avoid shell injection
    if isinstance(command, str):
        command = command.split()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return process.returncode, output, error
