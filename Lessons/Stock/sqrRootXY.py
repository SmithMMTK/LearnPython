# Find square root of a number by dividing the number by 2 on target digit

def sqrRoot(target,y):
    if target == 0:
        return 0
    elif target < 0:
        return -1
    
    if y < 2:
        return -1

    left = 0
    right = 10
    previousAnswer = 0
    

    while True:
        mid = (left + right) / 2
        if mid == previousAnswer:
            return mid
        else:
            previousAnswer = mid
        print("mid: ", mid)
        midValue = 1
        ## Multiply mid by itself y times
        for i in range(0,y):
            midValue = midValue * mid

        if midValue == target:
            return mid
        elif midValue < target:
                left = mid
        else:
                right = mid

    # Check the digit length of current


target = 9
answer = sqrRoot(target,3)
