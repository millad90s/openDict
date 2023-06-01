import subprocess
import sys


def add_to_dic(keyword):                            # to read the argument
    with open('dic-a.txt', 'a') as f:
        f.write(str(keyword) + '\n')


# Using command line arguments
if __name__ == "__main__":                         # If the file is executed directly (script file)
    if len(sys.argv) > 1 and sys.argv[1] == '-a':  # to read the argument
        if len(sys.argv) > 2:                      # At least two input arguments (after -a)
            keyword = eval(sys.argv[2])            # Convert (key & value dictionary) to Dic
            add_to_dic(keyword)
        else:
            print("No keyword provided.")
    else:
        print("Invalid command. Use this command: dic.py -a <keyword> <\"['values']\">")


