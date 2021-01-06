 # function to find sum, count, and reverse of the given number
def find(list):
    s = sum(list)
    print("sum:", s)
    c = list.count(3)
    print("count:", c)
    list.reverse()
    print(list)




find([2,3,4,3])