def histogram(results):

    op = []
    for i, x in enumerate(results):
        line = ""
        line = line + str(6-i)
        line = line + ("!")
        if x > 0:
            for y in range(x):
                line = line + ('#')
            line = line + (' ' + (str(x)))
        print(line)
    print("\n")
    #op.append(line)
    #print(op)

histogram([0,0,0,0,0,0])
histogram([3,6,2,4,6,1])

'''
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