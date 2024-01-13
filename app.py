import os
import subprocess
import time

def prepare():
    # Define an empty file path
    devnull = open(os.devnull, 'w')

    # Set standard output and standard error streams to redirect to an empty file
    command = "imjoy-elfinder --root-dir=/ --port=7860"
    process = subprocess.Popen(command, shell=True, stdout=devnull, stderr=subprocess.STDOUT)
    devnull.close()

print("starting--")
os.system('imjoy-elfinder --root-dir=/ --port=7860')
# Call the prepare function
prepare()
time.sleep(99999999)
