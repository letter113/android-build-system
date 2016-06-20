import sys

from android_build_system.tasks import project_creation, compile, launch, package
from android_build_system.config import AAPT, ZIPALIGN
from android_build_system.utils import init_logger


def pre_check():
    if not AAPT:
        sys.exit("We could not find aapt in path or under %ANDROID_HOME%")
    if not ZIPALIGN:
        sys.exit("We could not find aapt in path or under %ANDROID_HOME%")


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
    else:
        sys.exit("We don't know what to do with {}".format(sys.argv[1]))


if __name__ == "__main__":
    init_logger()
    main()