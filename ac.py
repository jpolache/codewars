def capitalize(s):
    #ss = list(s)
    print(s)
    mapped = zip(s[::2].upper(), s[1::2].lower())
    print(set(mapped))
    
capitalize("abcdef")
capitalize("codewars")