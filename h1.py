def histogram(results):
    for i, x in enumerate(results):
        if x > 0:
            print(str(6-i) + '!')
            for y in x:
                print('#', end = '')
            print(' ' + str(x))

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