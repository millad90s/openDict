"""
This module supposed to add/update/delete words and it's meaning to a datatype
it should be able to write it to a file
"""

import os


class Dict:
    def __init__(self):
        self.filename = None
        self.word = None
        self.dbdict = None
        self.meaning = None
        self.new_word = None

    def add_word(self, dbdict, new_word, meaning):
        self.dbdict = dbdict
        self.new_word = new_word
        self.meaning = meaning
        mydict = self.dbdict
        if self.new_word in self.dbdict:
            print(f"{self.new_word} exists in db, let's update meaning")
            current_meaning = self.dbdict.get(self.new_word)
            current_meaning.append(self.meaning)
            self.dbdict[self.new_word] = current_meaning
        else:
            print(f"{self.new_word} does not exists in db, let's add it")
            mydict[self.new_word] = [self.meaning]

    # todo: delete words(key) if exists in my dictionary
    def delete_word(self, dbdict, word):
        self.dbdict = dbdict
        self.word = word
        mydict = self.dbdict
        if self.word in mydict:
            del mydict[self.word]
            print(f"Deleted {self.word} in dictionary")
        else:
            print(f"There isn't {self.word} in Dictionary for delete")

    # Todo: need a function to write changes into a file in filesystem
    def save_to_file(self, filename, dbdict):
        self.filename = filename
        self.dbdict = dbdict
        path = os.getcwd() + "/" + self.filename
        my_file = open(path, 'w')
        my_file.write(str(self.dbdict))
        my_file.close()

