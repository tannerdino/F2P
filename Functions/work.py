
def experience(inputlvl):
    import math
    sum = 0
    lvl = 1
    for x in range(lvl, inputlvl):
        sum += (math.floor(x + 300 * 2**(x/7)))
    realsum = math.floor(sum/4)

    return (realsum)

def xpneeded(inputlvl):
    import math
    return experience(min(inputlvl + 1,99)) - experience(inputlvl)
