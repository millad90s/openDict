#  Write to file Dictionary
def write_dic(key, synonym):
    dictionary = {key: synonym}
    return dictionary


#  Read file Dictionary
def read_dic():
    with open('dic-a.txt', 'r+') as f:
        file_content = f.read()
        file_content = file_content.rstrip(file_content[-1])  # use index -1 because remove lase character in dic-a.txt

        if file_content:
            dic_in_file = eval('{' + file_content + '}')  # Change to Dictionary type
            # print('from read file: ', dic_in_file)
            iter_keys = iter(dic_in_file.keys())
            first_key = next(iter_keys)
        else:
            dic_in_file = {}
    return dic_in_file
