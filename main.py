import openDict

db = {"Milad": ["reborn"]}
nw = "Reza"
mn = "son of sun"

print(db)
my_dict = openDict.Dict()
my_dict.add_word(db, nw, mn)
print(db)

my_dict.save_to_file('db.txt', db)

my_dict.delete_word(db, 'Ali')
print(db)

my_dict.save_to_file('db.txt', db)

