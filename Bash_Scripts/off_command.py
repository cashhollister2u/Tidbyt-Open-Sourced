import subprocess

def off_switch():
    command = ['sudo', 'shutdown', '-h', 'now']
    subprocess.run(command, check=True)