import os
import subprocess

def prepare():
    # Update apt-get
    subprocess.run(["apt-get", "update"])

    # Install imjoy-elfinder
    subprocess.run(["pip3", "install", "imjoy-elfinder"])

    # Install aria2 and python3pip
    print("Installing aria2 downloader...")
    subprocess.run(["apt", "install", "-y", "aria2"])

    # Define an empty file path
    devnull = open(os.devnull, 'w')

    # Set standard output and standard error streams to redirect to an empty file
    command = "imjoy-elfinder --root-dir=/kaggle --port=8076"
    process = subprocess.Popen(command, shell=True, stdout=devnull, stderr=subprocess.STDOUT)
    devnull.close()

# Call the prepare function
prepare()
