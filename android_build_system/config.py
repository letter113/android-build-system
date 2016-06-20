import os
import sys
import shutil
import glob


ANDROID_EXE = "android.bat" if sys.platform == "win32" else "android"
ANDROID_CMD = os.path.join(os.environ.get("ANDROID_HOME", ""), "tools", ANDROID_EXE)
AAPT_EXE = "aapt.exe" if sys.platform == "win32" else "aapt"
ZIPALIGN_EXE = "zipalign.exe" if sys.platform == "win32" else "zipalign"


def get_exe(exe_name):
    cmd = shutil.which(exe_name)
    if cmd:
        return cmd
    cmd = glob.glob(os.path.join(os.environ.get("ANDROID_HOME", ""), "build-tools", "*", exe_name))
    if cmd:
        return cmd[0]


AAPT = get_exe(AAPT_EXE)
ZIPALIGN = get_exe(ZIPALIGN_EXE)