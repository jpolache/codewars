def histogram(results):
    results.reverse()
    for i, x in enumerate(results):
        line = ""
        line = line + str(6-i)
        line = line + ("|")
        if x > 0:
            for y in range(x):
                line = line + ('#')
            line = line + (' ' + (str(x)))
        print(line + "\n", end='')

histogram([0,0,0,0,0,0])
histogram([3,6,2,4,6,1])

'''
def histogram(results):
    return "".join("{}|{} {}\n".format(7 - i, f * "#", f) for i, f in enumerate(reversed(results), 1)).replace(" 0", "")

A 6-sided die is rolled a number of times and the results
are plotted as a character-based histogram.

Example:

6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
'''