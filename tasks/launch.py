import subprocess
import os


def run():
    subprocess.call(
        ["adb",
         "-e",
         "install", os.path.join("bin", "final.apk")]
    )