Scale.default = "minor"
Root.default = "G"
Clock.bpm = 110
Root.default -= 12

Master().amplify=0.89


vol_karp = 0.8
vol_b1 = 0.8
vol_bass=0.8

vol_d2 = 0.4
vol_d6 = 0.3
vol_d8 = 0.7

############## intro
var.roots = var([0], dur=[8])
p1 >> karp(P[var.roots,4,7].loop(4)|P[2,2,2,2].loop(2), dur=PDur(15,16), amp=vol_karp, pan=-1)

p2 >> karp(P[3,2,var.roots].loop(4)|P[4,4,4,4].loop(2), dur=PDur(15,16), amp=vol_karp, pan=1)

d1 >> play("(-   )n", dur=[1/2, 1/4, 1/4], amp=0.5)

d5 >> play("X [(X[xx] [x xx]) ][X ][[X ]X]", dur=var([1, 2, 1], 16), lpf=1600, lpr=0.7, amp=0.5)

######### parte 1
b1 >> bass(var.roots, dur=[2, 1/2, 1/2
, rest(1), 1/4, 1/2, 1/4, 1/2, rest(1/2), 1/2, 1/2, rest(1/2), 1/4, 1/4], amp=vol_b1, oct=5)
d2 >> play("V ", dur=2, drive=0.1, amp=vol_d2)

var.roots = var([0, -1], dur=[8])


######## Bumbo caixa
d6 >> play("X(OOOOOO(O[OOOO] ))", dur=1, hpf=1900, hpr=0.8, sample=1, amp=vol_d6) 

d3 >> play("e{     [ e][ee][eeee][ee][ e][ee][e ]e}", dur=1/2, amp=0.4, rate=0.95)

######## parte 2

d3.stop()
b1 >> bass(var.roots, dur=1/4, sus=1/4, amp=vol_bass)
p1 >> karp(P[var.roots,4,7].loop(4)|P[2,2,2,2].loop(2), dur=1/4, amp=vol_karp, pan=-1)
p2 >> karp(P[3,2,var.roots].loop(4)|P[4,4,4,4].loop(2), dur=1/4, amp=vol_karp, pan=1)
Group(p1, p2, b1).amplify = var([1,0], dur=PDur(5,8))


######## parte 1: el retuerno
p1 >> karp(P[var.roots,4,7].loop(4)|P[2,2,2,2].loop(2), dur=PDur(15,16), amp=vol_karp, pan=-1)
p2 >> karp(P[3,2,var.roots].loop(4)|P[4,4,4,4].loop(2), dur=PDur(15,16), amp=vol_karp, pan=1)
d1 >> play("(-   )n", dur=[1/2, 1/4, 1/4], amp=0.5)
d5 >> play("X [(X[xx] [x xx]) ][X ][[X ]X]", dur=var([1, 2, 1], 16), lpf=1600, lpr=0.7, amp=0.5)
b1 >> bass(var.roots, dur=[2, 1/2, 1/2, rest(1), 1/4, 1/2, 1/4, 1/2, rest(1/2), 1/2, 1/2, rest(1/2), 1/4, 1/4], amp=vol_b1, oct=5)
d2 >> play("V ", dur=2, drive=0.1, amp=vol_d2)
d6 >> play("X(OOOOOO(O[OOOO] ))", dur=1, hpf=1900, hpr=0.8, sample=1, amp=vol_d6) 
d3 >> play("e{     [ e][ee][eeee][ee][ e][ee][e ]e}", dur=1/2, amp=0.4, rate=0.95)
Group(p1, p2, b1).amplify = var([1], dur=PDur(5,8))


####### parte 2: cerro abajo
d3.stop()
b1 >> bass(var.roots, dur=1/4, sus=1/4, amp=vol_bass)
p1 >> karp(P[var.roots,4,7].loop(4)|P[2,2,2,2].loop(2), dur=1/4, amp=vol_karp, pan=-1)
p2 >> karp(P[3,2,var.roots].loop(4)|P[4,4,4,4].loop(2), dur=1/4, amp=vol_karp, pan=1)
Group(p1, p2, b1).amplify = var([1,0], dur=PDur(5,8))

d8 >> play("({[PP][PPPP] [PP]P    })PP", dur=[1/2, 1/4, 1/4], lpf=linvar([1000, 2800], 16), lpr=0.5, amp=vol_d8)

d6.stop()

d4 >> play("f", dur=[1/2, rest(1/8), 1/8, rest(1/4)], rate=1, amp=0.5)


############# bad
Group(p1, p2, b1,d1,d2, d3,d5,d6,d7, d4).stop()
b2 >> sawbass(var.roots, dur=[2, 1/2, 1/2, rest(1), 1/4, 1/2, 1/4, 1/2, rest(1/2), 1/2, 1/2, rest(1/2), 1/4, 1/4], amp=1, oct=4)

p3 >> piano(var.roots + P[0:7], dur=[3,8,3,2], amp=0.25, drive=0.5).penta().shuffle().every(16, "stutter", 4, pan=0).every(8, "offadd", 4)

d4 >> play("(f[ff])~", dur=[1/2, rest(1/8), 1/8, rest(1/4)], rate=linvar([0.7, 0.05], 16))

d8 >> play("({[PP][PPPP] [PP]P    })PP", dur=[1/2, 1/4, 1/4], lpf=linvar([1000, 2800], 16), lpr=0.5, amp=1).stop()


####################
# DRUMS

# INTRO

d1 >> play("(-   )n", dur=[1/2, 1/4, 1/4], amp=0.5)

d2 >> play("V ", dur=2, amp=vol_d2)

d5 >> play("X [(X[xx] [x xx]) ][X ][[X ]X]", dur=var([1, 2, 1], 16), lpf=1600, lpr=0.7, amp=0.5)

d6 >> play("^(oOoOoOo )", dur=1, hpf=1900, hpr=0.8, sample=1, amp=vol_d6)

d3 >> play("e{     [ e][ee][eeee][ee][ e][ee][e ]e}", dur=1/2, amp=0.4, rate=0.95)

d8 >> play("({[PP][PPPP] [PP]P    })PP", dur=[1/2, 1/4, 1/4], lpf=linvar([1000, 2800], 16), lpr=0.5, amp=vol_d8)

d4 >> play("f", dur=[1/2, rest(1/8), 1/8, rest(1/4)], rate=1, amp=0.5)

d4 >> play("(f[ff])~", dur=[1/2, rest(1/8), 1/8, rest(1/4)], rate=linvar([0.7, 0.05], 16), amp=0.5)


print(sorted(Attributes))
