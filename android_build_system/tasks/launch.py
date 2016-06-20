import subprocess
import os

from android_build_system.utils import run_cmd


def run():
    run_cmd(
        ["adb",
         "-e",
         "install", os.path.join("bin", "final.apk")]
    )