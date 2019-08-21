def capitalize(s):
    op = ""
    print(s)
    mapped = zip(s[::2].upper(), s[1::2].lower())
    for i in mapped:
        for x in i:
            op = op + str(x)
    print(op)

capitalize("abcdef")
capitalize("codewars")