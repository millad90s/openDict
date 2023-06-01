import argparse
import read_write

parser = argparse.ArgumentParser(description='read & view dic files')
parser.add_argument('-a', '--add', nargs=2, type=str, metavar=('key', 'synonym'), help='Add to dic. Example: python3 add_dic.py --add city "['"town"']"')
args = parser.parse_args()

if not args.add:
    print("Invalid command. Use this command: dic.py -a <keyword> <\"['values']\">")
else:
    input_key = args.add[0]
    input_synonym = eval(args.add[1])

    # Write to file
    write_word = read_write.write_dic(args.add[0], eval(args.add[1]))  # use function write_dic in ead_write file import
    write_word_str = str(write_word).replace('{', '').replace('}', '')
    write_word_str = write_word_str + ','
    with open('dic-a.txt', 'a') as ff:
        ff.write(str(write_word_str))
    print('Keyword added successfully.')
    print('Dictionary now= ', read_write.read_dic())


'''
for k in iter_keys:
    print(k)
    if k == write_word.keys():
        print('This word is repeated')
        break

    else:
        print('Add New Keyword')
        f.write(str(write_word))
'''
