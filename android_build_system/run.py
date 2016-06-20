import sys

from android_build_system.tasks import project_creation, compile, launch, package

from android_build_system.pre_checks.env_check import (
    EnvCheck, AAPTCheck, ZIPALIGNCheck, CmdCheck)


def pre_check():
    print("Doing some pre-check now...")

    if all([
        EnvCheck().check(),
        AAPTCheck().check(),
        ZIPALIGNCheck().check()
    ] + [
        CmdCheck(cmd).check() for cmd in [
            "javac",
            "keytool",
            "jarsigner",
            "adb"]
    ]):
        print("All check passed [OK]")
    else:
        sys.exit("Not all requirements met.")


def _print_help():
    print(
            "\nusage:\n"
            "create: create a new project\n"
            "compile: run this at the root of your project and compile it\n"
            "package: run this at the root of your project and make .apk\n"
            "launch: run this at the root of your project and launch your apk in the emulator\n"
        )


def main():
    pre_check()

    if len(sys.argv) == 1:
        _print_help()
        return

    if sys.argv[1] == "create":
        project_creation.run()
    elif sys.argv[1] == "compile":
        compile.run()
    elif sys.argv[1] == "package":
        package.run()
    elif sys.argv[1] == "launch":
        launch.run()
    elif sys.argv[1] == "help":
        _print_help()
    else:
        sys.exit("We don't know what to do with {},"
                 " please type help for supported command".format(sys.argv[1]))


if __name__ == "__main__":
    main()