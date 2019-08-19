def remove_duplicate_words(s):
    #s = list(dict.fromkeys( s.split() ))
    #s = list(dict(s.split()))
    print(set( s.split() ))

remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
remove_duplicate_words("my cat is my cat fat")