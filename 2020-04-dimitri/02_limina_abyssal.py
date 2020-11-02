Scale.default = "phrygian"
Clock.bpm=150
Master().amplify = .45

var.ch = var([0])

p2 >> gong(var.ch + [P(0,var([3, 3, 3, [4, 0]], [7.5, 5, 5, 2.5])), P(0,1)], dur=[1,1/2,1], oct=2, amp=0.38)

~d8 >> play("T", dur=[3/2, 1], lpf=2400, pan=0.75, amp=0.6)
~d9 >> play("p", dur=[3/2, 1, 1/2, 1/4, rest(3/4), 1/2, 1/4, [1/4, rest(1/4)]], lpf=1800, pan=-.75, amp=0.45)

~d2 >> play("[ss]", dur=[1/2, rest(1/4), 1/2, rest(1/4), 1, rest(1/4), 1/4, 1, 3/4, rest(1/4)], pan=PWhite(.5, -.5), amp=0.6)

~d1 >> play("X ", sample=2, lpf=1800, lpr=0.4, amp=0.60, room=0, drive=0)
b1 >> bass(var.ch + var([0,1], dur=[9,1]), dur=1, amp=0.6, lpf=600, sus=0.5)
dx >> play(" (---(---[--]))", sample=1, hpf=1000, amp=0.8)

~b1 >> bass(var.ch + var([0,1], dur=[9,1]), dur=1, amp=0.6, lpf=600, sus=0.5).every([15,5], 'offadd',2)

~p1 >> pads(var.ch, dur=4, vib=2, vibdepth=1, amp=0.7)

var.ch = var([4])

var.ch = var([0])
~d5 >> play("z", dur=PDur(var([6, 3], 5), 10), amp=0.55, room=0, hpf=linvar([1400, 2600], 40), hpr=0.25, drive=0.01, pan=-0.8)

~p1 >> pads(var.ch, dur=var([4,1/4], dur=4), vib=2, vibdepth=1, amp=0.7)


~d5 >> play("z", dur=PDur(var([6, 3], 5), 10), amp=0.55, room=0, lpf=linvar([200, 800], 40), lpr=0.25, drive=0.01, pan=0)
~p1 >> pads(var.ch + [0,0,2,3], dur=var([4,1/4], dur=4), vib=2, vibdepth=1, amp=0.7, pan=0).every(3, "offadd", -1)
Group(d5, p1).solo()

Group(d5, p1).solo(0)
d5.stop()
q2 >> keys(var.ch + P[0,3,5,6,7][:8], dur=1/32, pan=0, amp=0.7).every(4, "offadd", 3)

Master().amplify = 1
var.ch = var([0])

Master().amplify = .92
var.ch = var([4])

Master().amplify = 0.87
var.ch = var([7])

Master().amplify = 1
var.ch = var([0])

Group(p2, d8, d9).solo()

