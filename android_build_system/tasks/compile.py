import subprocess
import os
import sys


from android_build_system.config import AAPT
from android_build_system.utils import run_cmd


def run():
    ensure_at_project_dir()
    android_jar_path = get_android_jar_path()
    _create_R_file(android_jar_path)
    _compile(android_jar_path)


def _create_R_file(android_jar_path):
    run_cmd(
        [AAPT,
         "package",
         "-v",
         "-f",
         "-m",
         "-S", "res",
         "-J", "src",
         "-M", "AndroidManifest.xml",
         "-I", android_jar_path],
        timeout=30
    )


def _get_all_java_files():
    java_files = []
    for dirName, _, fileList in os.walk(os.getcwd()):
        for fname in fileList:
            _, ext = os.path.splitext(fname)
            if ext == ".java":
                java_files.append(os.path.join(dirName, fname))
    print(java_files)
    return java_files


def _compile(android_jar_path):
    seq = ";" if sys.platform == "win32" else ":"
    call = ["javac",
         "-verbose",
         "-d", "obj",
         "-classpath", android_jar_path + seq + "obj",
         "-sourcepath", "android_build_system",
         ] + _get_all_java_files()
    print(call)
    subprocess.call(
        call,
        timeout=60
    )


def ensure_at_project_dir():
    pass


def get_api_level():
    with open("project.properties") as handler:
        line = handler.readline()
        while line:
            if "target=" in line:
                value = line.split("target=")[1]
                if value.startswith("android-"):
                    return value.split("android-")[1].strip()
                return value.rsplit(":", maxsplit=1)[1].strip()
            line = handler.readline()
    raise Exception("We can't understand project.properties")


def get_android_jar_path():
    return os.path.join(
         os.environ["ANDROID_HOME"],
         "platforms",
         "android-" + get_api_level(),
         "android.jar")