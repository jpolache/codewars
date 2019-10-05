'''
# Python Program to find numbers divisible 
# by thirteen from a list using anonymous 
# function 

# Take a list of numbers. 
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ] 

# use anonymous function to filter and comparing 
# if divisible or not 
result = list(filter(lambda x: (x % 13 == 0), my_list)) 

# printing the result 
print(result) 
'''

def find_missing_letter(chars):
    i_ord = ord(chars[0])
    print([chr(i+i_ord) for i, item in enumerate(chars) if (item != chr(i+i_ord))][0])


find_missing_letter(['a','b','c','d','f']) #, 'e'

'''
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))

def find_missing_letter(chars):
    i_ord = ord(chars[0])
    for i, item in enumerate(chars):
        #print("***item: ", item, "chr(i+i_ord): ", chr(i+i_ord), "***")
        if item != chr(i+i_ord):
            #print(chr(i+i_ord))
            break
    return chr(i+i_ord)


test.describe("kata tests")
test.it("example tests")
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
'''
