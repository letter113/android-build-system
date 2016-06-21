import os
import sys

from android_build_system.utils import run_cmd


EXPECTED_APK_PATH = os.path.join("bin", "final.apk")


def run():
    ensure_has_apk()
    run_cmd(
        ["adb",
         "-e",
         "install",
         EXPECTED_APK_PATH]
    )


def ensure_has_apk():
    if os.path.isfile(EXPECTED_APK_PATH):
        return
    sys.exit("{} does not exist or it's not a file".format(EXPECTED_APK_PATH))