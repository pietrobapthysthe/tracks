Scale.default = "dorian"

Master().amplify = 0.45

var.ch = var([0])

~p2 >> sitar(var.ch, dur=2, amp=0.58, pan=-0.2).every(2,"offadd",-3)
~dx >> play("XXX ", sample=1, dur=[2,1/2,1/2,1], amp=0.9)
~px >> piano(p2.pitch + P(0,2,4), dur=[2,1/2,1/2,rest(1)], pan=0.2, amp=0.9)

Group(p2,d0,px).solo()

b1 >> sawbass(var.ch, dur=1, sus=1/2).every(4, "stutter", 4, sus=1/16)
d7 >> play("V", dur=4, room=0.5, drive=0.35, lpf=2000, lpr=0.2, echo=0.1, amp=.85)

p1 >> karp(var.ch + P[0:7][:5], dur=var([PDur(5,8), PDur(5,8)/12], dur=[3,1]), pan=PWhite(-1,1), amp=1).shuffle()
~d1 >> play(" (-[--]- -[--]-[----])", amp=1)

dx.amplify=0
~d0 >> play("X ", amp=0.9, sample=1, lpf=2000)

~d3 >> play(" O", echo=0, dur=1, hpf=2000, hpr=0.3, amp=0.4)

var.ch = var([3])

var.ch = var([0])
~d4 >> play("bbbb", amp=0.1, lpf=2000, lpr=0.4, dur=PDur(var([7, 5, 3, 5], 8), 8), pan=PWhite(-.5, .5)).every(32, "stutter", 4)

~d4 >> play("b{bbb[bb]}b{b }", amp=0.1, lpf=2000, lpr=0.4, dur=PDur(var([7, 5, 3, 5], 8), 8), pan=PWhite(-.5, .5)).every(32, "stutter", 4)

~p3 >> viola(P[var.ch, 1,3,2], dur=[1/2,1/2,1/4,1/2,1/2,1], pan=1, scale=Scale.blues, amp=0.9)
~p4 >> viola(P[var.ch, 1,3,2], dur=[1/2,1/2,1/4,1/2,1/2,1], pan=-1, scale=Scale.blues, oct=4, amp=0.9)

Group(p3, p4).stop()

var.ch = var([2])

var.ch = var([0])

p3 >> viola(P[var.ch, 1,3,2], dur=[1/2,1/2,1/4,1/2,1/2,1], pan=1, scale=Scale.blues, amp=0.9).rarely("offadd", -1)
p4 >> viola(P[var.ch, 1,3,2], dur=[1/2,1/2,1/4,1/2,1/2,1], pan=-1, scale=Scale.blues, oct=4, amp=0.9).rarely("offadd", -1)
~d6 >> play("[ss]", dur=[1/2, 1/4, 1/2, 1/4, 1, rest(1/4), 1/4, 1/2], amp=0.8)
Group(p3,p4,d6).solo()

var.ch = var([0])

~d5 >> play("{f[ff][ff]ffff[ff] }", dur=PDur(5, 8), hpf=linvar([1200, 2600], 32), hpr=0.6)

~d8 >> play(var(["^", "f"], 4), sample=[0, 1, 0, 2], pan=PWhite(-0.5, 0.5), dur=PDur(7, 8))

~d8 >> play(var(["^[^ ^ ]", "f"], 4), sample=[0, 1, 0, 2], pan=PWhite(-0.5, 0.5), dur=PDur(7, 8))

~d8 >> play(var(["^[^^^^]", "f"], 4), sample=[0, 1, 0, 2], pan=PWhite(-0.5, 0.5), dur=PDur(7, 8))

liberta()

Group(p3,p4).amplify = var([1,0], dur=PDur(7,8))

Group(p3,p4).stop()

~d3 >> play(" (([OOOO]O)([OO]O)O[OO])", echo=0.25, dur=2, hpf=2000, hpr=0.3, amp=0.4)

saida()


nextBar(liberta)

@nextBar
def liberta():
    Group(d5,d8).stop()
    Group(p3,p4,d6).solo(0)


@nextBar
def saida():
    dx.amplify=1
    Group(px, dx, p2).solo()