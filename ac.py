def capitalize(s):
    ss = s.split()
    for i in ss[1::2]:
        print(i)

capitalize("abcdef")
capitalize("codewars")