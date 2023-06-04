import openDict

db_dict = openDict.OpenDict("a.txt", True)
db_dict.show_data()
db_dict.__data = {}
db_dict.search_data('torturously')
db_dict.delete_word("calciphilia")
db_dict.add_word('calciphilia', 'this is test')
db_dict.add_word('calciphilia', 'test3')
db_dict.show_data()
