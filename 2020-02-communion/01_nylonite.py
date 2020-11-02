# based on pybr-algorave2

Scale.default = "minor"
Root.default = "E"
Root.default -= 12

Master().amplify = 0.74

vol_bass = 0.65
vol_piano = 0.5
vol_space = 0.65
vol_blip = 0.7


def bass1():
    ~b0 >> bass(var.roots, dur=[1/2,1,1/2], amp=vol_bass, oct=5, sus=1/2).every(2, "offadd", 2).every(4, "bubble")

def bass2():
    ~b0 >> bass(var.roots, dur=[2, rest(1/2), 1, 1/2, 1, rest(1/2), 1/2, rest(1/4), 1/4, 1/2, 1/2, 1/2], amp=vol_bass, oct=5)

def piano1():
    p1 >> piano(var.roots + P(0,2,4,6), dur=[8,8,8,8], amp=vol_piano)
    
def chords2():
    var.roots = var([0,3], dur=[16,8])

def piano2():
    p1 >> piano(var.roots + P(0,2,4,6), dur=[8,8,8,6,2], amp=vol_piano)

def intro():
    var.roots = var([0])
    bass1()
    hi1()
    hi2()    
    
def part_a():
    bu1()
    ca1()
    hi3()
    bass2()
    piano1()
    
def part_a2():
    chords2()
    piano2()
    
def drop():
    hi3()
    bu1()
    ca1()
    piano2()
    d6.stop()
    d7.stop()
    
def chords3():
    var.roots = var([0, 4, 3, 1], dur=[16, 8, 4, 4])
    

Clock.schedule(intro)
Clock.schedule(part_a, Clock.now() + 32)
Clock.schedule(part_a2, Clock.now() + 64)
Clock.schedule(chords3, Clock.now() + 128)

p4 >> space(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_space, pan=-1).every(2,"offadd",2).every(4, "bubble")

p5 >> blip(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_blip, pan=1).every(2,"offadd",2).every(4, "bubble")

~p4 >> space(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_space, pan=-1).every(2,"offadd",2).every(4, "bubble")
~p5 >> blip(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_blip, pan=1).every(2,"offadd",2).every(4, "bubble")


Group(p4, p5, d3, d4).stop()
p6 >> donk(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=0.5, oct=[5,6], pan=0.7).every(2,"offadd",2).every(4, "bubble")
hi1()

bass1()
p6 >> donk(var.roots, dur=PDur(5,8), sus=1/2, amp=0.5, oct=[5,6], pan=0.7).every(2,"offadd",2).every(4, "bubble")
p1.stop()
~d6 >> play("(V[VVVV]     (V [VV] )V)", dur=1, lpf=900, lpr=0.8, echo=0.25, amp=0.2)

~d5 >> play("f", dur=PDur(var([2, 5, 3, 3], 4), var([8, 5], 32)), lpf=600, lpr=0.4, sample=1, amp=0.3, pan=-0.7)

~d7 >> play(" (b ([bb][bb][bb][[bb]  [bb]  ]) )", lpf=linvar([400, 800], 12), dur=1, echo=0.5, amp=0.3)

p2 >> nylon(var.roots + [3, 6, 4], dur=1/2, amp=0.3, lpf=3000).every(4, "offadd", 4).every(3, "stutter", 3, pan=[-1, 1])


Group(d1, d5, d6, d7, p6).amplify = var([1, 0.2], dur=[28,4])

drop()

p2.stop()
p4 >> space(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_space, pan=-1).every(2,"offadd",2).every(4, "bubble")

p5 >> blip(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_blip, pan=1).every(2,"offadd",2).every(4, "bubble")

~p4 >> space(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_space, pan=-1).every(2,"offadd",2).every(4, "bubble")
~p5 >> blip(var.roots, dur=[1/2,1,1/2], sus=1/2, amp=vol_blip, pan=1).every(2,"offadd",2).every(4, "bubble")
~b0 >> bass(var.roots, dur=[1/2,1,1/2], amp=vol_bass, oct=5, sus=1/2).every(2, "offadd", 2).every(4, "bubble")

d3.stop()
d4.stop()

Group(p_all, b_all).amplify = var([1, 0], dur=[30,2])

################ FUNÇÕES
vol_hi1 = 0.25
vol_hi2 = 0.3
vol_hi3 = 0.25
vol_bu1 = 0.25
vol_ca1 = 0.25

def hi1():
    d1.reset()
    d1 >> play('-(-[--]  )-----( - [ -])', pan=-0.4, sample=3, amp=vol_hi1)    
def hi2():
    ~d2 >> play("s ((ss[s s ]s)[ss]s( e)) ", lpf=linvar([2600, 4000], 12), pan=0.4, amp=vol_hi2)
def hi3():
    d1.reset()
    d1 >> play("[--]", hpf=linvar([2000, 2900], 24), hpr=0.6, amp=vol_hi3).every(8, 'stutter', 4, amp=0.25)
def bu1():
    ~d3 >> play("X( [ X] (([xx]x) (x[xx]) ))", amp=vol_bu1, sample=2)
def ca1():
    ~d4 >> play(" (o[o o ]o )", amp=vol_ca1, hpf=linvar([800, 1900], 12), hpr=0.92)  

Group(d1,d2).solo()

d3.stop()
d4.stop()

################ BATERIA

hi()

hi2()

hi3()

bu1()

ca1()


~d5 >> play("f", dur=PDur(var([2, 5, 3, 3], 4), var([8, 5], 32)), lpf=600, lpr=0.4, sample=1, amp=0.3, pan=-0.7)

~d6 >> play("(V[VVVV]     (V [VV] )V)", dur=1, lpf=900, lpr=0.8, echo=0.25, amp=0.2)

~d7 >> play(" (b ([bb][bb][bb][[bb]  [bb]  ]) )", lpf=linvar([400, 800], 12), dur=1, echo=0.5, amp=0.3)

d5.stop()

d6.stop()

d7.stop()