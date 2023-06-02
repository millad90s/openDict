
"""
This module supposed to add/update/delete words and it's meaning to a datatype
it should be able to write it to a file
"""


# add new world with meaning into db or update it if key exists
def add_word(dbdict, new_word, meaning):
    mydict = dbdict
    # if this word does not exist in the dictionary:
    # then add it + it's meaning
    if new_word in dbdict:
        print("the key exists in db, let's update meaning")
        current_meaning = dbdict.get(new_word)
        current_meaning.append(meaning)
        dbdict[new_word] = current_meaning
    # if it doesn't exist then let's add it in the meaning lists
    else:
        print("key does not exists in db, let's add it")
        mydict[new_word] = [meaning]


# Todo: need a function to write changes into a file in filesystem
# def save_to_file(path, filename, dict)

# todo: delete words(key) if exists in my dictionary
# def delete_word(dict, word)

# todo: Implement through OOP
