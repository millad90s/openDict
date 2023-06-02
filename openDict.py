class OpenDict:

    data = {}
    filename = ""

    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r') as file:
            self.data = eval(file.read())

    def show_data(self):
        print(self.data)

    @staticmethod
    def save_data(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.data))

    def add_word(self, new_word, meaning):
        if new_word in self.data:
            print("the key exists in db, let's update meaning")
            current_meaning = self.data.get(new_word)
            current_meaning.append(meaning)
            self.data[new_word] = current_meaning
            self.save_data(self)
        # if it doesn't exist then let's add it in the meaning lists
        else:
            print("key does not exists in db, let's add it")
            self.data[new_word] = [meaning]
            self.save_data(self)


# Todo: need a function to write changes into a file in filesystem
# def save_to_file(path, filename, dict)

# todo: delete words(key) if exists in my dictionary
# def delete_word(dict, word)

# todo: different init based on database { file | postgresql )
