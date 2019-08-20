def remove_duplicate_words(s):
    op = []
    for item in s.split():
        if  item not in op:
            op.append(item)
    return op

remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
remove_duplicate_words("my cat is my cat fat")