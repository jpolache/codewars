def capitalize(s):
    op = ""
    op2 = ""
    print(s)
    mapped = zip(s[::2].upper(), s[1::2].lower())
    mapped2 = zip(s[::2].lower(), s[1::2].upper())
    for i in mapped:
        for x in i:
            op = op + str(x)
    for i in mapped2:
        for x in i:
            op2 = op2 + str(x)

    print(op)
    print(op2)

capitalize("abcdef")
capitalize("codewars")