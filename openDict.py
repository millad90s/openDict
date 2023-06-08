import random

import gtts
import nltk
import os
from colorama import Fore
from nltk.corpus import words, wordnet
from playsound import playsound


class OpenDict:
    __data = {}
    filename = ""

    __PATH = ".tmp/"

    def __init__(self, filename, is_load_random=False):
        try:
            self.filename = filename
            if not is_load_random:  # if is_load_random = False
                # load DB with random words and their meaning
                with open(filename, 'r') as file:
                    self.__data = eval(file.read())
            else:  # if is_load_random = True
                # Download required data
                nltk.download('wordnet')
                nltk.download('words')

                word_list = words.words()
                for wrd in range(100):
                    random_word = random.choice(word_list)
                    # add word and meanings into db
                    meanings = wordnet.synsets("word")
                    self.add_word(random_word, meanings[0].definition())
        except FileNotFoundError:
            print(f"{Fore.LIGHTRED_EX}'{filename}' File not found in Method __init__")
        except Exception:
            print(f"{Fore.LIGHTRED_EX} There is an error in '__init__' Method")


    def show_data(self):
        # print(self.__data)
        mydict = dict(self.__data)
        for k, v in mydict.items():
            print(Fore.GREEN + str(k) + Fore.RED + ":" + Fore.WHITE + str(v))

    def __save_data(self):
        try:
            with open(self.filename, 'w') as file:
                file.write(str(self.__data))
        except IOError:
            print(f'{Fore.LIGHTRED_EX} IOError occurred in Method __save_data')
        except Exception:
            print(f"{Fore.LIGHTRED_EX} There is an error in '__save_data' Method")

    # add/update a word into dictionary
    def add_word(self, new_word, meaning):
        try:
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
        except KeyError:
            print(f'Sorry {Fore.LIGHTRED_EX} Key Error occurred in Method add_word')
        except Exception:
            print(f"{Fore.LIGHTRED_EX} There is an error in 'add_word' Method")

    # delete a word from dictionary
    def delete_word(self, word):
        try:
            if word in self.__data.keys():
                self.__data.pop(word)
                self.__save_data()
                print(f"{Fore.LIGHTRED_EX}{word} deleted")
            return f"{word} does not exists in dictionary"
        except KeyError:
            print(f'Sorry {Fore.LIGHTRED_EX} Key Error occurred in Method delete_word')
        except Exception:
            print(f"{Fore.LIGHTRED_EX} There is an error in 'delete_word' Method")

    # a function to search a word in db and return its values
    def search_data(self, my_word, audio):
        try:
            if my_word in self.__data.keys():
                print(Fore.LIGHTYELLOW_EX + 'Result search: ' + Fore.BLUE + my_word, ":", self.__data[my_word])
                self.__play_word(my_word + " means " + self.__data[my_word][0]) if audio else None
            else:
                print(
                    Fore.LIGHTRED_EX + f"There isn't {Fore.LIGHTYELLOW_EX} {my_word} {Fore.LIGHTRED_EX} in dictionary")
                # if a searched word, does not exist in db, then use a 3rd party app
                meaning = wordnet.synsets(my_word)
                self.add_word(my_word, meaning[0].definition())
                self.__play_word(my_word + " means " + meaning[0].definition()) if audio else None
        except KeyError:
            print(f'Sorry {Fore.LIGHTRED_EX} Key Error occurred in Method search_data')
        except Exception:
            print(f"{Fore.LIGHTRED_EX} There is an error in 'search_data' Method")

    def __play_word(self, my_word):
        try:
            my_tts = gtts.gTTS(my_word)
            my_tts.save(self.__PATH + my_word)  # __PATH = ".tmp/"
            playsound(self.__PATH + my_word)
            os.remove(self.__PATH + my_word)
        except FileNotFoundError:
            print(
                f"{Fore.LIGHTRED_EX}Directory '{self.__PATH}' not found. Resolve:Create '.tmp' directory in the same path")
        except PermissionError:
            print(f'{Fore.LIGHTRED_EX} Permission Error for {self.__PATH}  file occurred in Method __play_word')
        except Exception:
            print('There is an error in Method __play_word')
        else:
            print('Successfully')

# todo: different init based on database { file | postgresql )

# todo: to get the meaning and add it to the database and also return to the user, /// Done

# todo: we need the capability of speech in our application. /// Done :)

# todo: improve show_data function, /// Done

# todo: implement API with request library

# todo: handle errors
