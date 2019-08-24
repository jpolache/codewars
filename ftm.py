def min_value(digits):
    return (int(''.join(str(x) for x in sorted(set(digits)))))

'''
 def min_value(digits):
     return int("".join(map(str, sorted(set(digits)))))
'''

min_value([1, 3, 1])


