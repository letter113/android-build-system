import sys

from tasks import project_creation, compile, package


def main():
    if sys.argv[1] == "create":
        project_creation.run()
    elif sys.argv[1] == "compile":
        compile.run()
    elif sys.argv[1] == "package":
        package.run()
    else:
        sys.exit("We don't know what to do with {}".format(sys.argv[1]))


if __name__ == "__main__":
    main()