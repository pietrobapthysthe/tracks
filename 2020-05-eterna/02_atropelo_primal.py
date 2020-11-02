Clock.bpm = 150
Root.default = "e"
Root.default -= 12
Scale.default = "minor"


var.ch = var([0])

Clock.set_time(-1)
~d1 >> play(
    '*',
    sample=[1, 1, 2, [3, 1], 4],
    dur=1/2,
    amp=.7,
    lpf=[300, 600, 300, [400, 800], 600],
    lpr=0.3,
    rate=[1, 0.95, 1.05, 1, 1],
    coarse=1,
)

~d3 >> play(
    "(p[pp][p ][pp])(p[ p])([p pp][[p ][p   ]p ][pp] )(ppp[ pp ])",
    dur=1/2,
    sample=var([1, 3], 32),
    lpf=3200,
    lpr=0.8,
    amp=.8,
    rate=[1, 0.995, 1, 1.005]
)

~d4 >> play("-", dur=PDur([3, 5, 2, 7], 8), sample=[1, 2, 3, 1], rate=[1, 1.05, 1, 0.95], echo=[1/4], pshift=[0.9, 1.1], pan=PWhite(0.7, -0.7), amp=0.5)
~b1 >> bass(var.ch + [0, [0, 0], 0, [0, 0], 0, 0, 0], dur=[1, 1/4, 3/4, 2, [2, 1], [1, 2], 1], lpf=300, amp=0.7, oct=5)

~d2 >> play('V', dur=1, lpf=500,  room=0.05)

Master().amplify = var([1, 0], [35, 5])

~b3 >> donk(b1.pitch + P[-4:4].shuffle(), dur=PDur(var([3, 5], 10), 8), drive=0.70, amp=0.4, amplify=0.8, sus=1/4, pan=0).penta().every(20, "shuffle")
~d9 >> play("s", dur=[1/4], amp=0.1, hpf=linvar([1900, 4000], 40), hpr=0.2, echo=1/16, rate=[0.95, 1, 1.05, 1], pshift=-0.05)

Master().amplify = 1

d9.stop()
~b1 >> bass(var.ch + [0, [2, 4], 3, [1, 2], 0, 7, 0], dur=[1, 1/4, 3/4, 2, [2, 1], [1, 2], 1], lpf=300, amp=0.7, oct=5)

~k1 >> keys(b1.pitch + P(0, 2, 4) + var([(0, 0, 3), (0, 0, -1)], 8), hpf=400, hpr=0.7, dur=[2, 1/2, 1/2, 1], sus=0.5, chop=1/4)

~d3 >> play(
    "(p[pp][p ][pp])(p[ p])([p pp][[p ][p   ]p ][pp] )(ppp[ pp ])",
    dur=1/2,
    sample=var([1, 3], 32),
    lpf=3200,
    lpr=0.15,
    amp=.05,
    rate=[1, 0.90, 1, 1.1],
    echo=1/64,
    pan=PWhite(.5, -.5),
    pshift=-.6,
)
~d4 >> play("e", dur=PDur([3, 5, 2, 7], 8), sample=[1, 2, 3], rate=[1, 1.05, 1, 0.95], pan=PWhite(-.7, .7), pshift=0.9)
~b1 >> bass(var.ch + P[0].loop(6)|P[7,4,5,2, 1].loop(2), dur=1/2, sus=1/4, amp=1).every(5, "stutter", 3, dur=1/3, sus=1/8)
Group(b1, d3, d4).solo()

~k1 >> keys(b1.pitch + P[0, 2, 4, 6][:10].shuffle(), hpf=800, hpr=0.7, dur=[2, 1/2, 1/2, 1], sus=0.5, drive=0.4, amp=0.8).every(20, "stutter", 2)
d9 >> play("s", dur=[1/4], amp=0.1, hpf=linvar([1900, 4000], 40), hpr=0.2, echo=1/16, rate=[0.95, 1, 1.05, 1], pshift=-0.05)

~k2 >> keys(k1.pitch + P(4, 7), hpf=800, hpr=0.7, dur=[2, 1/2, 1/2, 1], sus=0.5, drive=0.4, oct=5, amp=0.8).every(20, "stutter", 2)

Group(d_all, b_all).amplify = var([1, 0], [35, 5])

~d3 >> play(
    "(p[pp][p ][pp])(p[ p])([p pp][[p ][p   ]p ][pp] )(ppp[ pp ])",
    dur=1/2,
    sample=var([1, 3], 32),
    lpf=3200,
    lpr=0.8,
    amp=.8,
    rate=[1, 0.995, 1, 1.005]
)
~d4 >> play("-", dur=PDur([3, 5, 2, 7], 8), sample=[1, 2, 3, 1], rate=[1, 1.05, 1, 0.95], echo=[1/4], pshift=[0.9, 1.1], pan=PWhite(0.7, -0.7), amp=0.5)
Group(b1, d3, d4).solo(0)

Group(d_all, b_all).amplify = 1

k2.stop()
k1.stop()
~d3 >> play(
    "(p[pp][p ][pp])(p[ p])([p pp][[p ][p   ]p ][pp] )(ppp[ pp ])",
    dur=1/2,
    sample=var([1, 3], 32),
    lpf=3200,
    lpr=0.15,
    amp=.05,
    rate=[1, 0.90, 1, 1.1],
    echo=1/64,
    pan=PWhite(.5, -.5),
    pshift=-.6,
)
~d4 >> play("-", dur=PDur([3, 5, 2, 7], 8), sample=[1, 2, 3, 1], rate=[1, 1.05, 1, 0.95], echo=[1/4], pshift=[0.9, 1.1], pan=PWhite(0.7, -0.7), amp=0.5)
~b1 >> bass(var.ch + [0, [0, 0], 0, [0, 0], 0, 0, 0], dur=[1, 1/4, 3/4, 2, [2, 1], [1, 2], 1], lpf=300, amp=0.7, oct=5)

~b1 >> bass(var.ch + [0, [2, 4], 3, [1, 2], 0, 7, 0], dur=[1, 1/4, 3/4, 2, [2, 1], [1, 2], 1], lpf=300,  amp=0.7, oct=5)

~k1 >> keys(b1.pitch + P[0, 2, 4, 6][:10].shuffle(), hpf=800, hpr=0.7, dur=[2, 1/2, 1/2, 1], sus=0.5, drive=0.4, amp=0.8).every(20, "stutter", 2)

~k2 >> keys(k1.pitch + P(4, 7), hpf=800, hpr=0.7, dur=[2, 1/2, 1/2, 1], sus=0.5, drive=0.4, oct=5, amp=0.8).every(20, "stutter", 2)

d9.stop()
Group(d1, d4, k1, k2).solo()


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx