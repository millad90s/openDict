import openDict


db_dict = openDict.OpenDict("a.txt", False)
db_dict.search_data('car', True)
db_dict.search_data('book', True)
