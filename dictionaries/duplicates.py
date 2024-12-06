dict1 = {'id1': {'name':'ajay', 'class':'3p', 'si': 'english, maths, science'},
         'id2': {'name': 'evan', 'class': '3p', 'si': 'english, maths, literature'},
         'id3': {'name':'ajay', 'class':'3p', 'si': 'english, maths, science'}}

dict2 = {}

for i in dict1:
    if dict1[i] not in dict2.values():
        dict2[i]=dict1[i]

print(dict2)
        