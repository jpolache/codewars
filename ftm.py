def min_value(digits):
    d_str = ''.join(str(e) for e in digits)
    tn = (''.join(str(e) for e in sorted(set(digits))))
    #print(d_str, tn)
    print(''.join(str(e) for e in digits) == ''.join(str(e) for e in sorted(set(digits))))

min_value([1, 3, 1])


