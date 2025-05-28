import sys, os
if not './test/' in sys.path:
    sys.path.append('./test/')
from TestUtils import TestCodeGen


# Biến toàn cục
file_name = None

def main():
    global file_name

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Error: You must provide exactly one file.")
        sys.exit(1)

    file_name = sys.argv[1]
    
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

    if not file_name.endswith(".mng"):
        print("Error: The file must be a .mng file.")
        sys.exit(1)

    TestCodeGen.check(file_name)


if __name__ == "__main__":
    main()
