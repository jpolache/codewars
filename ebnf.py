def even_numbers_before_fixed(sequence, fixed_element):
    op = 0
    count = 0
    if fixed_element in sequence:
        for i in sequence:
            if i % 2 == 0 and i != fixed_element:
                count += 1
            elif i == fixed_element:
                if count > 0:
                    op = count
                break
    else:
        op = -1
    print(str(op))
    return op


even_numbers_before_fixed([1, 4, 2, 6, 3, 1], 6)
even_numbers_before_fixed([2, 2, 2, 1], 3)
even_numbers_before_fixed([2, 3, 4, 3], 3)
even_numbers_before_fixed([1, 3, 4, 3], 3)

'''
def even_numbers_before_fixed(s, f):
    return len([x for x in s[:s.index(f)] if x%2 == 0]) if f in s else -1
'''