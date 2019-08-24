def min_value(digits):
    return (''.join(str(e) for e in sorted(set(digits))))

min_value([1, 3, 1])


