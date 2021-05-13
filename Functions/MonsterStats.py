class Monster():

    def __init__(self, hp, deflvl, stabdef, slashdef, crushdef, craftper, lawsper, natsper, prayper):
        self.hp = hp
        self.deflvl = deflvl
        self.stabdef = stabdef
        self.slashdef = slashdef
        self.crushdef = crushdef
        self.craftper = craftper
        self.lawsper = lawsper
        self.natsper = natsper
        self.prayper = prayper
ogress = Monster(
82,
82,
10,
12,
12,
10.69,
0.694,
0.649,
15)

moss = Monster(
60,
30,
0,
0,
0,
50/128 + 67.5/256 + 85/512 + 107.5/2048 + (96.25*5*3/118)/(60.24*0.9366666666),
3/32 + (800/118)/(60.24*(0.9366666666)),
6/42.67 + (600/118)/(60.24*(0.9366666666)),
15 + (15/(60.24*(0.9366666666)))
)
hill = Monster(
35,
26,
0,
0,
0, 
50/170.67 + 67.5/341.33 + 85/682.67 + 107.5/2730.67 + (96.25*5*5/118)/(128*0.9366666666),
6/128 + ((12*((50+99)/2))/118)/(128*0.9366666666),
12/128 + ((7*((40+79)/2))/118)/(128*0.9366666666),
15 + 1/(128*0.9366666666) + (400/118)/(128*0.9366666666)
)
#ice

class neckwear():
    pass
strammy = neckwear()
strammy.name = "Str-Ammy"
strammy.str = 10
strammy.acc = 0

powerammy = neckwear()
powerammy.name = "Power-Ammy"
powerammy.str = 6
powerammy.acc = 6

class footwear():
    pass
goldboots = footwear()
goldboots.str = 1
goldboots.acc = 0

none = footwear()
none.str = 0
none.acc = 0

class wep(): 
    pass  
#initialize
slash = 0
stab = 0
crush = 0

scim = wep()
scim.stab = 7
scim.slash = 45
scim.crush =  -2
scim.str = 44

sword = wep()
sword.stab = 38
sword.slash = 26
sword.crush =  -2
sword.str = 39

golemmace = wep()
golemmace.stab = 20
golemmace.slash = -2
golemmace.crush = 40
golemmace.str = 40

scim.bonus = slash
sword.bonus = stab
golemmace.bonus = crush
