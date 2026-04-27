import random
def max_min(mlist):
    minimum = mlist[0]
    for num in mlist:
        if num < minimum:
            minimum = num
        print(f"Value is {minimum}")
    pass

mlist = random.sample(range(1,30), 5)
print(mlist)
max_min(mlist)
