import subprocess
import os
import sys


def run():
    ensure_at_project_dir()
    api_level = get_api_level()
    android_jar_path =os.path.join(
             os.environ["ANDROID_HOME"],
             "platforms",
             "android-" + api_level,
             "android.jar")
    _create_R_file(api_level)
    _compile(android_jar_path)


def _create_R_file(api_level):
    subprocess.call(
        ["aapt",
         "package",
         "-v",
         "-f",
         "-m",
         "-S",
         "res",
         "-J",
         "src",
         "-M",
         "AndroidManifest.xml",
         "-I",
         os.path.join(
             os.environ["ANDROID_HOME"],
             "platforms",
             "android-" + api_level,
             "android.jar")],
        timeout=30
    )


def _compile(android_jar_path):
    seq = ";" if sys.platform == "win32" else ":"
    subprocess.call(
        ["javac",
         "-verbose"
         "-d", "obj",
         "-classpath", android_jar_path + seq + "obj",
         "-sourcepath", "src",
         "**/*.java"],
        timeout=60
    )


def ensure_at_project_dir():
    pass


def get_api_level():
    with open("project.properties") as handler:
        line = handler.readline()
        if "target=" in line:
            value = line.split("target=")[1]
            if value.startswith("android-"):
                return value.split("android-")[1]
            return value.rsplit(":", maxsplit=1)[1]
    raise Exception("We can't understand project.properties")