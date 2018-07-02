"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(nums):
    flag = 0
    #flag2 = 1
    for i in nums:
        if i == 0:
            flag= flag+1
            continue
        if flag == 2:
            if i == 7:
                return True
        else:
            #print(i)
            continue
    return False
                
spy_game([1,2,4,0,0,7,5])