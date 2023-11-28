
import sys
import os

def main():
    if len(sys.argv) != 3:
        print("not enough args")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isdir(directory):
        print("error")
        sys.exit(1)

    for file in os.listdir(directory):
        if file.endswith(extension):
            try:
                with open(os.path.join(directory, file), 'r') as f:
                    print(f.read())
            except IOError:
                print("error")

if __name__ == '__main__':
    main()
