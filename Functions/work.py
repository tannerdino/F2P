import math
from MonsterStats import *
def experience(inputlvl):
    sum = 0
    lvl = 1
    for x in range(lvl, inputlvl):
        sum += (math.floor(x + 300 * 2**(x/7)))
    realsum = math.floor(sum/4)

    return (realsum)

def xpneeded(inputlvl,inputlvl2):
    return experience(min(inputlvl2,99)) - experience(min(inputlvl,99))

def successchance(inputlvl,low,high):
    return (math.floor(low*(99-inputlvl)/98) + math.floor(high*(inputlvl-99)/98) + 1)/256

def bigformula(monster1,monster2,combatxpstart,combatxpgoal): #clean this NOW
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



xpperhour = 14000
xpperhour2 = 23000
lawslap = (3.5*37.5)
lawspent = xpperhour2/lawslap
lawsomething = (xpperhour2-xpperhour)/lawspent

increaseperlaw = 1 - xpperhour/(xpperhour+lawsomething)


Oc = ogress.craftper
Oh = ogress.hp
D = 13034431*4
C = 13034431
S = 13034431

def DPSS(monstertype,weapon,strengthlvl,attacklvl,pray): #AGGRESSIVE
    import math
    strpray = pray
    attpray = pray
    weaponbonus = max(weapon.stab,weapon.slash,weapon.crush)
    effstr = (math.floor(((strengthlvl + math.floor((strengthlvl * 0.1) + 3)) * strpray)) + 3) + 8
    maxhit1 = math.floor(((effstr * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
    maxhit2 = math.floor(((effstr * (weapon.str + powerammy.str + feet.str + 64)) + 320)/640)

    if maxhit1 == maxhit2:
        necklace = powerammy
    else:
        necklace = strammy

    maxhit = math.floor(((effstr * (weapon.str + necklace.str + feet.str + 64)) + 320)/640)


    if weapon.bonus == stab:
        bonusdef = monstertype.stabdef
    elif weapon.bonus == slash:
        bonusdef = monstertype.slashdef
    elif weapon.bonus == crush:
        bonusdef = monstertype.crushdef
    else:
        bonusdef = monstertype.slashdef

    defroll = (monstertype.deflvl + 9) * (bonusdef+64) #defence roll


    effatt = (math.floor(attacklvl * attpray)+0+8)
    attroll = math.floor(effatt * (weaponbonus + necklace.acc + 64))

    if attroll > defroll:
        accuracy = (1-((defroll+2)/(2*(attroll+1))))

    else:
        accuracy = (attroll/(2*(defroll+1)))
    Y = min(maxhit,monstertype.hp)
    hit = ((accuracy*Y*(Y+1)) / (monstertype.hp*(maxhit+1) )) * ( 0.5 * (maxhit+monstertype.hp+1) - ((1/3) * (2*Y+1)))
    dps = hit/ (0.6*4)
    i = round(dps*3600*4,0)
    result = i
    return result,necklace.name

def DPSA(monstertype,weapon,strengthlvl,attacklvl,pray):
    import math
    strpray = pray
    attpray = pray
    weaponbonus = max(weapon.stab,weapon.slash,weapon.crush)
    effstr = (math.floor(((strengthlvl + (math.floor((strengthlvl * 0.1) + 3))) * strpray)) + 0)+8
    maxhit1 = math.floor(((effstr * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
    maxhit2 = math.floor(((effstr * (weapon.str + powerammy.str + feet.str + 64)) + 320)/640)

    if maxhit1 == maxhit2:
        necklace = powerammy
    else:
        necklace = strammy
        
    maxhit = math.floor(((effstr * (weapon.str + necklace.str + feet.str + 64)) + 320)/640)


    if weapon.bonus == stab:
        bonusdef = monstertype.stabdef
    elif weapon.bonus == slash:
        bonusdef = monstertype.slashdef
    elif weapon.bonus == crush:
        bonusdef = monstertype.crushdef
    else:
        bonusdef = monstertype.slashdef

    defroll = (monstertype.deflvl + 9) * (bonusdef+64) #defence roll

    
    effatt = (math.floor(attacklvl * attpray)+3+8)
    attroll = math.floor(effatt * (weaponbonus + necklace.acc + 64))

    if attroll > defroll:
        accuracy = (1-((defroll+2)/(2*(attroll+1))))

    else:
        accuracy = (attroll/(2*(defroll+1)))

    Y = min(maxhit,monstertype.hp)
    hit = ((accuracy*Y*(Y+1)) / (monstertype.hp*(maxhit+1) )) * ( 0.5 * (maxhit+monstertype.hp+1) - ((1/3) * (2*Y+1)))
    dps = hit/ (0.6*4)
    i = round(dps*3600*4,0)
    result = i
    
    return result,necklace.name

def DPSD(monstertype,weapon,strengthlvl,attacklvl,pray):
    strpray = pray
    attpray = pray
    weaponbonus = max(weapon.stab,weapon.slash,weapon.crush)
    pot = 1
    effstr = (math.floor(((strengthlvl + (math.floor((strengthlvl * 0.1) + 3 - 2)*pot)) * strpray)) + 0)+8
    maxhit1 = math.floor(((effstr * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
    maxhit2 = math.floor(((effstr * (weapon.str + powerammy.str + feet.str + 64)) + 320)/640)

    if maxhit1 == maxhit2:
        necklace = powerammy
    else:
        necklace = strammy
        
    maxhit = math.floor(((effstr * (weapon.str + necklace.str + feet.str + 64)) + 320)/640)


    if weapon.bonus == stab:
        bonusdef = monstertype.stabdef
    elif weapon.bonus == slash:
        bonusdef = monstertype.slashdef
    elif weapon.bonus == crush:
        bonusdef = monstertype.crushdef
    else:
        bonusdef = monstertype.slashdef

    defroll = (monstertype.deflvl + 9) * (bonusdef+64) #defence roll

    
    effatt = (math.floor(attacklvl * attpray)+0+8)
    attroll = math.floor(effatt * (weaponbonus + necklace.acc + 64))

    if attroll > defroll:
        accuracy = (1-((defroll+2)/(2*(attroll+1))))

    else:
        accuracy = (attroll/(2*(defroll+1)))

    Y = min(maxhit,monstertype.hp)
    hit = ((accuracy*Y*(Y+1)) / (monstertype.hp*(maxhit+1) )) * ( 0.5 * (maxhit+monstertype.hp+1) - ((1/3) * (2*Y+1)))
    dps = hit/ (0.6*4)
    i = round(dps*3600*4,0)
    result = i
    
    return result,necklace.name


def nextmaxhit(weapon,strlvl,strpray,strpot):
    startstrlvl = strlvl
    strpot = (strpot/2)
    effstr = (math.floor(((strlvl + (math.floor((strlvl * 0.1) + 3))) * strpray)) + 0)+8
    maxhit1 = math.floor(((effstr * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
    maxhit2 = math.floor(((effstr * (weapon.str + powerammy.str + feet.str + 64)) + 320)/640)
    for i in range(strlvl,130):
        strlvl += 1
        effstr = (math.floor(((strlvl + (math.floor((strlvl * 0.1) + 3))) * strpray)) + 0)+8
        effstr1 = (math.floor((((strlvl-1) + (math.floor(((strlvl-1) * 0.1) + 3))) * strpray)) + 0)+8
        maxhit = math.floor(((effstr * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
        maxhit1 = math.floor(((effstr1 * (weapon.str + strammy.str + feet.str + 64)) + 320)/640)
        if maxhit > maxhit1:
            return strlvl
        elif strlvl>=99:
            return startstrlvl
        else:
            continue


def hrstoMaxHit(weapon,strlvl,attlvl,pray,strpot,monstertype):
    sumhours = 0
    for i in range(strlvl,nextmaxhit(weapon,strlvl,pray,strpot)+1):
        xpperhour = DPSS(monstertype,weapon,strlvl,attlvl,pray)[0]
        hours = xpneeded(strlvl, strlvl+1)/xpperhour
        sumhours += hours
        strlvl += 1
    return sumhours - hours

def MeleeOrder(monstertype,weapon,strlvl,attlvl, deflvl,pray):
    sumhours = 0
    hours = 0
    for i in range(strlvl+attlvl,99*2): #attack and strength
        hourstomaxhit = hrstoMaxHit(weapon,strlvl,attlvl,pray,0,monstertype)-hrstoMaxHit(weapon,strlvl,attlvl+1,pray,0,monstertype)
        atthours = DPSA(monstertype,weapon,strlvl,attlvl,pray)[0]
        trueatthours = xpneeded(attlvl, attlvl+1)/atthours
        if hourstomaxhit < trueatthours:
            strlvl = min(strlvl + 1,100)
            if strlvl == 100:
                attlvl = min(attlvl + 1,100)
                xphours = DPSA(monstertype,weapon,strlvl,attlvl,pray)[0]
                truexphours = DPSA(monstertype,weapon,strlvl-1,attlvl-1,pray)[0]
                necklace = DPSA(monstertype,weapon,strlvl,attlvl,pray)[1]
                lvl = attlvl
                style = "Attack"
                style2 = "Accurate"
            else:
                xphours = DPSS(monstertype,weapon,strlvl,attlvl,pray)[0]
                truexphours = DPSS(monstertype,weapon,strlvl,attlvl,pray)[0]
                necklace = DPSS(monstertype,weapon,strlvl,attlvl,pray)[1]
                lvl = strlvl
                style = "Strength"
                style2 = "Aggressive"
        else:
            attlvl = min(attlvl + 1,100)
            xphours = DPSA(monstertype,weapon,strlvl,attlvl,pray)[0]
            truexphours = DPSA(monstertype,weapon,strlvl-1,attlvl-1,pray)[0]
            necklace = DPSA(monstertype,weapon,strlvl,attlvl,pray)[1]
            lvl = attlvl
            style = "Attack"
            style2 = "Accurate"
        hours = (xpneeded(lvl-1, lvl))/truexphours
        sumhours += hours   
        print(lvl,style,xphours,style2,necklace,round(sumhours,3))

    for i in range(deflvl,100): #defence
        defencexphr = DPSD(monstertype,weapon,strlvl,attlvl,pray)[0]
        deflvl += 1
        style = "Defensive"
        style2 = "Defence"
        xphours =  xpneeded(deflvl,deflvl+1)/defencexphr
        sumhours += xphours
        necklace = DPSD(monstertype,weapon,strlvl,attlvl,pray)[1]
        print(deflvl,style2,defencexphr, style,necklace,round(sumhours-xphours,3))
    return

