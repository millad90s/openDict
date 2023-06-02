import openDict

db_dict = openDict.OpenDict("a.txt")
db_dict.show_data()

db_dict.add_word("m4", "e4")
db_dict.show_data()
