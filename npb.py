
def number(bus_stops):
     print([(x[0]-x[1]) for x in bus_stops])

number([[10,0],[3,5],[5,8]])


'''
def number(bus_stops):
    op = 0
    print([(x[0]-x[1]) for x in bus_stops])
        op = op + (x[0]-x[1])
    print(str(op))

number([[10,0],[3,5],[5,8]])

x = [[1,2,3],[4,5,6],[7,8,9]]
print([[number for number in group] for group in x])
'''