Master().amplify = 0.74
Scale.default = "minor"
var.roots = var([0], dur=[8])

var.roots = var([0, 3], dur=[16, 8, 8, 8])

b1 >> bass(var.roots, dur=8, amp=0.75)

p2 >> gong(var.roots + var([(0, 2), (2, 4)], dur=1/2), dur=[1, 1/2], sus=1/2, amp=1).stop()

var.roots = var([0], dur=[8])
p1 >> karp(var.roots + var([0, -1], dur=[4]), dur=PDur(3,8), amp=0.8).stop()

p3 >> piano(var.roots + P[0:7], dur=1/2, amp=0.85).every(4, "offadd", 3).shuffle().penta()

p4 >> pads(var.roots, dur=8, tremolo=[2, 4], drive=0.2, amp=0.35)


###### PREPARE DROP
var.roots = var([0], dur=[8])
p3 >> piano(var.roots + P[0:7], dur=1/2, amp=0.85).every(4, "offadd", 3).shuffle().penta()
d8 >> play("X(--(--[----]-)-)", hpf=linvar([1000, 4000], 16), hpr=0.8, amp=0.4)
Group(p1, p2, b1, d1, d2, d3, d4).stop()
######

####### DROP
var.roots = var([0, 3], dur=[16, 8, 8, 8])
b1 >> bass(var.roots, dur=8, amp=0.75)
p2 >> gong(var.roots + var([(0, 2), (2, 4)], dur=1/2), dur=[1, 1/2], sus=1/2, amp=1)
p1 >> karp(var.roots + var([0, -1], dur=[4]), dur=PDur(3,8), amp=0.8)
p3 >> piano(var.roots + P[0:7], dur=1/2, amp=0.85).every(4, "offadd", 3).shuffle().penta()
d1 >> play("V( [VV] [V [VVVV][V ]])", dur=2, lpf=600, lpr=0.4, amp=0.3)
d2 >> play("[ss]", dur=var([1/2, 1, 1/2], 4), amp=0.4)
d4 >> play("{e[eeee] [ee][ e]}", dur=1, hpr=0.4, amp=0.4)
d7 >> play("(XX[XX] )([ X]X)O[X ]", amp=.4)
d8.stop()
d3.stop()
######

##### SECOND PREPARE
var.roots = var([0], dur=[8])
d5 >> play("+", dur=var([4, 1/4, 4, 1/2], 4), lpf=0, amp=0.4).every(16, "stutter", 4)
d6 >> play("f", dur=p1.dur, echo=var([0.5, 0], 4), amp=0.4)
d8 >> play("X(--(--[----]-)-)", hpf=linvar([1000, 4000], 16), hpr=0.8, amp=0.4)
p4 >> pads(var.roots, dur=8, tremolo=[2, 4], drive=0.2, amp=0.35)
Group(p1,p2,d1, d2, d3, d4, d7).stop()
#####



############### DRUMS
d_all.amp = 0.3

d1 >> play("V( [VV] [V [VVVV][V ]])", dur=2, lpf=600, lpr=0.4, amp=0.3)

d2 >> play("[ss]", dur=var([1/2, 1, 1/2], 4), amp=0.4)

d3 >> play("x o ", dur=1/2, amp=0.3)

d4 >> play("{e[eeee] [ee][ e]}", dur=1, hpr=0.4, amp=0.4)

d8 >> play("X(--(--[----]-)-)", hpf=linvar([1000, 4000], 16), hpr=0.8, amp=0.4)

d5 >> play("+", dur=var([4, 1/4, 4, 1/2], 4), lpf=0, amp=0.4).every(16, "stutter", 4)

d6 >> play("f", dur=p1.dur, echo=var([0.5, 0], 4), amp=0.4)

d7 >> play("(XX[XX] )([ X]X)O[X ]", amp=.4)

d7.stop()

d1.stop()

d2.stop()

d3.stop()

d4.stop()

d5.stop()

d6.stop()

d8.stop()


print(Attributes)