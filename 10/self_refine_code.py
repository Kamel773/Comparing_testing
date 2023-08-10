
import subprocess
import shlex

def execute_command(command):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-./")
    if not set(command) <= allowed_chars:
        raise ValueError("Invalid characters in command")
    if any(c in command for c in "|&;<>()$`\\"):
        raise ValueError("Invalid shell metacharacters in command")
    args = shlex.split(command)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return process.returncode, output, error
