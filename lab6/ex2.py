
import sys
import os


def main():
    if len(sys.argv) != 2:
        print("not enough args")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("error")
        sys.exit(1)

    for i, file in enumerate(os.listdir(directory)):
        try :
            os.rename(os.path.join(directory, file), os.path.join(directory, str(i) + file))
        except IOError:
            print("error")


if __name__ == '__main__':
    main()