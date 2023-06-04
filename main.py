import openDict

db_dict = openDict.OpenDict("a.txt", True)
db_dict.show_data()
db_dict.__data = {}
db_dict.show_data()
