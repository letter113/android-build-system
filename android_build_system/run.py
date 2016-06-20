import sys
import os
import shutil

from android_build_system.tasks import project_creation, compile, launch, package
from android_build_system.config import AAPT, ZIPALIGN


def pre_check():
    print("## Doing some pre-check now...")
    if not AAPT:
        sys.exit("We could not find aapt in path or under %ANDROID_HOME%")
    if not ZIPALIGN:
        sys.exit("We could not find aapt in path or under %ANDROID_HOME%")

    for env in ["JAVA_HOME", "ANDROID_HOME"]:
        if not os.environ.get(env):
            sys.exit("{} is not defined as system environment".format(env))

    for exe in ["javac", "keytool", "jarsigner"]:
        if not shutil.which(exe):
            sys.exit("{} is not in system path".format(exe))

    print("## All check passed")


def main():
    pre_check()

    if sys.argv[1] == "create":
        project_creation.run()
    elif sys.argv[1] == "compile":
        compile.run()
    elif sys.argv[1] == "package":
        package.run()
    elif sys.argv[1] == "launch":
        launch.run()
    elif sys.argv[1] == "help":
        print(
            "usage:\n"
            "create: create a new project\n"
            "compile: run this at the root of your project and compile it\n"
            "package: run this at the root of your project and make .apk\n"
            "launch: run this at the root of your project and launch your apk in the emulator\n"
        )
    else:
        sys.exit("We don't know what to do with {},"
                 " please type help for supported command".format(sys.argv[1]))


if __name__ == "__main__":
    main()