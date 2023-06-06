import nltk
from nltk.corpus import words, wordnet
import random
from colorama import init, Fore, Back, Style
import gtts, os
from playsound import playsound


class OpenDict:
    __data = {}
    filename = ""

    __PATH = ".tmp/"

    def __init__(self, filename, is_load_random=False):
        self.filename = filename
        if not is_load_random:  # False
            # load DB with random words and their meaning
            with open(filename, 'r') as file:
                self.__data = eval(file.read())
        else:
            # Download required data
            nltk.download('wordnet')
            nltk.download('words')

            word_list = words.words()
            for wrd in range(100):
                random_word = random.choice(word_list)
                # add word and meanings into db
                meanings = wordnet.synsets("word")
                self.add_word(random_word, meanings[0].definition())

    def show_data(self):
        # print(self.__data)
        mydict = dict(self.__data)
        for k, v in mydict.items():
            print(Fore.GREEN + str(k) + Fore.RED + ":" + Fore.WHITE + str(v))

    def __save_data(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.__data))

    # add/update a word into dictionary
    def add_word(self, new_word, meaning):
        if new_word in self.__data:
            # the key exists in db, let's update meaning"
            current_meaning = self.__data.get(new_word)  # get(key) = meanings
            if meaning in current_meaning:
                # no need to add , it is already in db
                print(f"{Fore.LIGHTBLUE_EX}{new_word} no need to add , it is already in dictionary")
                return
            current_meaning.append(meaning)
            self.__data[new_word] = current_meaning
            self.__save_data()
            print(f"{Fore.LIGHTMAGENTA_EX}{meaning} added to {new_word}")
        # if it doesn't exist then let's add it in the meaning lists
        else:
            # the key does not exist in db, let's add it
            self.__data[new_word] = [meaning]
            self.__save_data()
            print(f"{Fore.LIGHTGREEN_EX}{new_word} Add to Dictionary")

    # delete a word from dictionary
    def delete_word(self, word):
        if word in self.__data.keys():
            self.__data.pop(word)
            self.__save_data()
            print(f"{Fore.LIGHTRED_EX}{word} deleted")
        return f"{word} does not exists in dictionary"

    # a function to search a word in db and return its values
    def search_data(self, my_word, audio):
        if my_word in self.__data.keys():
            print(Fore.LIGHTYELLOW_EX + 'Result search: ' + Fore.BLUE + my_word, ":", self.__data[my_word])
            self.__play_word(my_word + " means " + self.__data[my_word][0]) if audio else None
        else:
            print(Fore.LIGHTRED_EX + f"There isn't {Fore.LIGHTYELLOW_EX} {my_word} {Fore.LIGHTRED_EX} in dictionary")
            # if a searched word, does not exist in db, then use a 3rd party app
            meaning = wordnet.synsets(my_word)
            self.add_word(my_word, meaning[0].definition())
            self.__play_word(my_word + " means " + meaning[0].definition()) if audio else None

    def __play_word(self, my_word):
        my_tts = gtts.gTTS(my_word)
        my_tts.save(self.__PATH + my_word)
        playsound(self.__PATH + my_word)
        os.remove(self.__PATH+my_word)

# todo: different init based on database { file | postgresql )

# todo: to get the meaning and add it to the database and also return to the user, /// Done

# todo: we need the capability of speech in our application. /// Done :)

# todo: improve show_data function, /// Done

# todo: implement API with request library

# todo: handle errors
