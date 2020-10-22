Clock.bpm = 150
Scale.default = "minor"

Root.default = var([0,0,-1,0], dur=8)

~p1 >> piano((0,2,4), dur=8, amp=0.6, sus=4)

Root.default = var([0], dur=[32])

~p1 >> piano((0,2,4), dur=8, amp=0.6, sus=4)
Root.default = var([0, 7, 5], dur=[16, 8, 8])


~p1 >> piano((0,2,4), dur=8, amp=0.6, sus=4)

p1 >> piano(P[0:7], dur=PDur(5,16), amplify=var([0,1], dur=4), amp=0.65).penta().shuffle()

p5 >> rave(P[0:7], dur=PDur(5,16), amplify=var([0,1], dur=4), amp=0.65).penta().shuffle().stop()

~d1 >> play("(V)....(V[V V ])([ V]   )..", dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/4, 1/4], sample=3, lpf=2900, lpr=0.3, amp=0.6)


~d1 >> play("V...VV.V", amp=0.6, dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2], lpf=2900, lpr=0.3, sample=3)
b1 >> bass([0,0,0,0,-1], dur=PDur(5, 16)*2, amp=0.7, sus=1/2, lpf=500)
~p1 >> piano((0,2,4), dur=8, amp=0.6, sus=4)
b2 >> donk(0, dur=8, room=0.9, drive=0.5, sus=1/2, oct=4)
p5.stop()

p2 >> prophet(4, dur=1/16, amp=0.1, drive=0.2, amplify=var([0,1], 4)).stop()


p3 >> pulse(P[0:7], dur=PDur(5, 16), amp=0.1, drive=0.1, amplify=var([0,1], 4)).shuffle().stop()

p2 >> prophet(4, dur=1/16, amp=0.1, drive=0.2, amplify=var([0,1], 4)).stop()

Group(p1, p5, b2, d5, d6).solo(0)


var.sop_vol = var([0.6])

s1 >> soprano(P[0,2,3,4,3,2], dur=[2,1,1,2,1,1], oct=2, amp=var.sop_vol, sus=1/2)
s2 >> soprano(P[0,2,3,4,3,2]+2, dur=[2,1,1,2,1,1], oct=2, amp=var.sop_vol, sus=1/2)
s3 >> soprano(P[0,2,3,4,3,2]+3, dur=[2,1,1,2,1,1], oct=2, amp=var.sop_vol, sus=1/2)



~d1 >> play("V...VV.V", amp=0.6, dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2], lpf=2900, lpr=0.3, sample=3)

~d1 >> play("(V )........", dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/4, 1/4], sample=3, lpf=2900, lpr=0.3, amp=0.6)
d2 >> play(".o.o..(o[oo]oo).", amp=0.5, dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2], hpf=PRand(1000, 2400))

~d1 >> play("(V)....(V[V V ])([ V]   )..", dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/4, 1/4], sample=3, lpf=2900, lpr=0.3, amp=0.6)



d2 >> play(".o.o..(o[oo]o[ee]).", amp=0.5, dur=P[3/4, 1/4, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2], hpf=PRand(1000, 2400))

d3.amplify = abs(p2.amplify - 1)

~d3 >> play("(b[bb][bb][ b])", dur=1, amp=expvar([0.6, 0.8], 8), echo=[0, [2, 2, 2, 4], 2
, 0], chop=PRand(2, 9), drive=0.01, hpf=1200, hpr=expvar([0.1, 0.8], 8), pan=PWhite(-1, 1), sample=[0])



~d7 >> play("[f+f]", amp=0.55, dur=PDur(15, 16, [0, 0, 1, 0]) * 4, pan=PWhite(-1, 1), hpf=PRand(700, 1200), hpr=PRand(4, 7) / 10.0, sample=[0, 1])
d7.amplify = var([1, 0], PDur([3, 5, 5, 3], 8, [0, 1]))



~d4 >> play("   [tt]", amp=0.4, sample=[1, 0, 1, 2], dur=PDur(11, 16), hpf=PRand(200, 1400), hpr=PRand(2, 6)/10.0, pan=linvar([-1, 1], 8))


var.t = var([1, 0], P[1/4, 3/4 + 3] * 4)
~d5 >> play("Z", amp=0.1 * var.t, dur=1, lpf=PRand(100, 700), chop=[8, 16, 8, 32], echo=2, echodepth=2, pan=-1)
~d6 >> play("[ Q]", dur=1, amp=var.t * 0.3, chop=[24, 16, 8, 12], lpf=PRand(200, 1700), lpr=PRand(3, 8) / 10.0, echo=1, pan=1)
