
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

def successchance(inputlvl,low,high):
    return (math.floor(low*(99-inputlvl)/98) + math.floor(high*(inputlvl-99)/98) + 1)/256

def ogresspercentage(monster1,monster2,combatxpstart,combatxpgoal): #kinda scuffed atm, doesnt include proper craft and smith variables
    a = monster1.lawsper
    b = monster1.hp
    c = monster1.natsper
    d = combatxpgoal
    e = combatxpstart
    f = monster2.natsper
    g = monster2.hp
    h = monster2.lawsper
    i = monster1.craftper
    j = monster2.craftper
    #y = 1 - x
    x = 1
    y = 1
    step2expr1 = ((((a/(b*4)) + ((c/(b*4*37.5)/(3.5*37.5)))) * ((d-e)*4)) - (((d)*(((1-((1-(i/(b)))*(13.7/52.5)))))/(37.5*3.5)) + (d*(1-(i/(b)))/(21*52.5))))
    step2expr2 = (((d * (1-(j/(g)))/(21*52.5)) + d*(1-((1-(j/(g)))*(13.7/52.5)))/(37.5*3.5)) - ((((f/(g*4)*37.5)/(3.5*37.5)) + (h/(g*4))) *((d-e)*4)))
    finalstep = step2expr2/step2expr1
    findperc = (1/finalstep)/(1+(1/finalstep))
    return findperc #ogress
