'''
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
    if len(s)%2 != 0:
        op = op + s[-1].upper()
        op2 = op2 + s[-1].lower()
    print(op)
    print(op2)


'''
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    print([s, s.swapcase()])
    return [s, s.swapcase()]

capitalize("abcdef")
capitalize("codewars")
capitalize("abcdefg")
