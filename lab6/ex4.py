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

    ext_dict = {}

    for file in os.listdir(directory):
        ext = os.path.splitext(file)[1]
        if ext in ext_dict:
            ext_dict[ext] += 1
        else:
            ext_dict[ext] = 1

    for ext, count in ext_dict.items():
        print(ext, count)


if __name__ == '__main__':
    main()
