import subprocess
import sys
import os


def run_cmd(cmd, timeout=30):
    print("##Running: ")
    print(" ".join(a for a in cmd))
    subprocess.call(cmd, timeout=timeout)


def ensure_at_project_dir():
    if not os.path.isfile("project.properties"):
        sys.exit("We could not locate project.properties, are you at the root of a project?")