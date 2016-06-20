import subprocess


def run_cmd(cmd, timeout=30):
    print("##Running: ")
    print(" ".join(a for a in cmd))
    subprocess.call(cmd, timeout=timeout)