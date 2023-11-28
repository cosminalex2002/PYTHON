
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

    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                total_size += os.path.getsize(os.path.join(root, file))
            except IOError:
                print("error")

    print("Total size:" + total_size)

if __name__ == '__main__':
    main()