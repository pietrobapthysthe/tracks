Master().amp = 0.92

Clock.set_time(-1)
var.ch = var([0,2, 0, -1], dur=16)
p1 >> piano(var.ch + P(0,2,4,3,5,7), dur=4)

p2 >> soprano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=2, amp=0.9, oct=3)

d1 >> play("X   ", dur=1)
d3 >> play("-", dur=1)

d2 >> play("  o ", dur=1)

b1 >> bass(var.ch, dur=1/4, sus=0.18, amp=0.8)
d_all.stop()

d1 >> play("X ", dur=1/2, amp=0.9)
d3 >> play("-(-------([--][----])-------([----][--]))", dur=1/2, amp=0.9)

d2 >> play("  o ", dur=1/2, amp=0.9)

p3 >> nylon(var.ch + P(0,2,4,3,5,7), dur=PDur(3,8), sus=1/8, amp=0.8)

p1 >> piano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=1/4, amp=0.9)

p1 >> piano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=1/4, amp=0.9).every(4,"offadd",4).every(3,"stutter",4)
~b1 >> bass(var.ch, dur=[1/4,1/4,rest(1/4),1/4,1/2,1/2], amp=0.8)
p2.stop()
Group(p1,b1).solo()

Group(p1,b1).solo(0)

p1 >> piano(var.ch + P(0,2,4,3,5,7), dur=4).solo()

p4 >> donk(var.ch + P[0:7][:3].shuffle(), dur=PDur(3,8))

b1 >> bass(var.ch + P[0][:12].loop(3)|P[4,3,2,0,2,1][:8].loop(2), dur=1/4, sus=0.18, amp=0.8)

p3.stop()
p1 >> piano(var.ch + P(0,2,4,3,5,7), dur=4).solo(0)

p1.stop()

d4 >> play("[sss]", amplify=var([1,0], dur=4), amp=0.5)

var.ch = var([0, 2,0,2], dur=16)
p5 >> karp(var.ch + P[0,3,5,3,2][:8], dur=PDur(5,8)).every(4,"offadd",3)

p1 >> piano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=1/4, amp=0.8).every(4,"offadd",4).every(3,"stutter",4)

p2 >> soprano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=2, amp=0.9, oct=3)

p3 >> nylon(var.ch + P(0,2,4,3,5,7), dur=PDur(3,8), sus=1/8, amp=0.8)

b1 >> bass(var.ch + P[0][:12].loop(3)|P[4,3,2,0,2,1][:8].loop(2), dur=PDur(5,8), sus=0.18, amp=0.8)
p1 >> piano(var.ch + P[0,2,4,3,5,7].shuffle(), dur=PDur(5,8), amp=0.8).every(4,"offadd",4).every(3,"stutter",4)

p1 >> piano(var.ch + P(0,2,4,3,5,7), dur=4, amp=0.9).solo()

~p1 >> piano(var.ch + P(0,2,4,3,5,7), dur=4)
