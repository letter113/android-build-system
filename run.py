import sys

from tasks import project_creation, compile


def main():
    if sys.argv[1] == "create":
        project_creation.run()
    elif sys.argv[1] == "compile":
        compile.run()
    else:
        sys.exit("We don't know what to do with {}".format(sys.argv[1]))


if __name__ == "__main__":
    main()