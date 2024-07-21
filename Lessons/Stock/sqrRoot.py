# Find square root of a number by dividing the number by 2 on target digit

def sqrRoot(target):
    if target == 0:
        return 0
    elif target < 0:
        return -1

    left = 0
    right = 999
    previousAnswer = 0

    while True:
        mid = (left + right) / 2
        if mid == previousAnswer:
            return mid
        else:
            previousAnswer = mid
        print("mid: ", mid)
        if mid * mid == target:
            return mid
        elif mid * mid < target:
                left = mid
        else:
                right = mid

    # Check the digit length of current


target = 10
answer = sqrRoot(target)
