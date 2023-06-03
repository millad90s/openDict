import nltk
from nltk.corpus import words, wordnet
import random


class OpenDict:

    data = {}
    filename = ""

    def __init__(self, filename, is_load_random=False):
        self.filename = filename
        if not is_load_random:
            # load DB with random words and their meaning
            with open(filename, 'r') as file:
                self.data = eval(file.read())
        else:
            # Download required data
            nltk.download('wordnet')
            nltk.download('words')

            word_list = words.words()
            for wrd in range(100):
                random_word = random.choice(word_list)
                # add word and meanings into db
                meanings = wordnet.synsets("word")
                self.add_word(random_word,meanings[0].definition())

    def show_data(self):
        print(self.data)

    @staticmethod
    def save_data(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.data))

    # add/update a word into dictionary
    def add_word(self, new_word, meaning):
        if new_word in self.data:
            # the key exists in db, let's update meaning"
            current_meaning = self.data.get(new_word)
            if meaning in current_meaning:
                # no need to add , it is already in db
                return
            current_meaning.append(meaning)
            self.data[new_word] = current_meaning
            self.save_data(self)
        # if it doesn't exist then let's add it in the meaning lists
        else:
            # the key does not exist in db, let's add it
            self.data[new_word] = [meaning]
            self.save_data(self)

    # delete a word from dictionary
    def delete_word(self, word):
        if word in self.data.keys():
            self.data.pop(word)
            self.save_data(self)
        return f"{word} does not exists in dictionary"




# todo: different init based on database { file | postgresql )

# todo: a function to search a word in db and return it's values

# todo: if a searched word, does not exist in db, then use a 3rd party app
#  to get the meaning and add it to the database and also return to the user

# todo: we need the capability of speech in our application :)

# todo: remove the words that has no meaning in my dictionary

# todo: improve show_data function

