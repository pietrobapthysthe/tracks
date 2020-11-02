Scale.default = "minor"

Master().amplify = 0.76

var.roots = var([0,2,0,2,0], dur=[24, 8,8,8,8])

fuzz_vol = 0.5
bass_vol = 0.6
karp_vol = 0.7
keys_vol = 0.7

p1 >> fuzz(0, amp=fuzz_vol)

p1 >> fuzz(0, oct=4, amp=fuzz_vol)

p1 >> fuzz(0 + P[0,2,3,5], oct=4, amp=fuzz_vol)

p1 >> fuzz(0 + P[0,2,3,5], oct=4, dur=1/2, amp=fuzz_vol)

p1 >> fuzz(0 + P[0,2,3,5], oct=4, dur=1/2, amp=fuzz_vol).every(8, "bubble")

b1 >> bass(0, dur=8, amp=bass_vol)
p1 >> fuzz(0 + P[0,2,3,5], oct=4, dur=1/2, lpf=linvar([300, 2000], 12), amp=fuzz_vol).every(8, "bubble")

p2 >> karp(0 + P[0,2,3,7,9], dur=[1/2,1,1/2,1,1,1/2], amp=karp_vol)

var.roots = var([0,2,0,2,0], dur=[24,8,8,8,8])
b1 >> bass(var.roots, dur=8, amp=bass_vol)
p1 >> fuzz(var.roots + [0,2,3,5], oct=4, dur=1/2, lpf=linvar([300, 2000], 12), amp=fuzz_vol).every(8, "bubble")
p2 >> karp(var.roots + [0,2,3,7,9], dur=[1/2,1,1/2,1,1,1/2], amp=karp_vol)

p3 >> keys(P[0:7], drive=0.1, dur=var([1/2], dur=[2,4]), sus=1/4, amp=keys_vol).penta().shuffle()

################### buildup
p3 >> keys(P[0:7], drive=0.1, dur=var([1/4, 1/2], dur=[2,4]), sus=1/4, amp=keys_vol, pan=0).penta().shuffle()
d7 >> play("-------[--]", hpf=2000, hpr=0.1, room=0.6, pan=[-1, 1], dur=1/2)
d8 >> play("x       ")
Group(p1, p2, b1, d1, d2, d3).stop()
#########################

############# drop
var.roots = var([0,2,0,2,0], dur=[24,8,8,8,8])
b1 >> bass(var.roots, dur=4, amp=bass_vol)
p1 >> fuzz(var.roots + [0,2,3,5], oct=4, dur=1/2, lpf=linvar([300, 2000], 12), amp=fuzz_vol).every(8, "bubble")

p2 >> karp(var.roots + [0,2,3,7,9], dur=[1/2,1,1/2,1,1,1/2], amp=karp_vol, amplify=0)

p3 >> keys(P[0:7], drive=0.1, dur=var([1/4, 1/2], dur=[2,4]), sus=1/4, amp=keys_vol, pan=0).penta().shuffle()
d1 >> play("[--]", dur=var([1/2, 1], 8), amp=0.5)
d3 >> play("(++ (++[++  ]+))", amp=0.5)
d4 >> play("V(( [V V ] [VV]) )  ", dur=1/2, amp=0.6)
d5 >> play("  O ", dur=1/2, amp=0.3)
d2.stop()
d7.stop()
##############

###### entra viola
p1.stop()
var.roots = var([0,2,0,2,0], dur=[16,8,8,8,8])
p4 >> viola(p2.pitch, dur=[8, 8, 1, 2, 1, 4], amp=1)
d7 >> play("-------[--]", hpf=2000, hpr=0.1, room=0.6, pan=[-1, 1], dur=1/2)
Group(d1, d3).stop()
#####################

p1.stop()


############# DRUMS
d1 >> play("[--]", dur=var([1/2, 1], 8), amp=0.5)

d2 >> play("V ", amp=0.7)

d3 >> play("(++ +)", amp=0.5)

d3 >> play("(++ (++[++  ]+))", amp=0.6)

d4 >> play("V(( [V V ] [VV]) )  ", dur=1/2, amp=0.6).stop()
d5 >> play("  O ", dur=1/2, amp=0.3).stop()

d6 >> play("{^ ^[^^][^ ][^ ^ ][^^] }", amp=0.6, lpf=800, lpr=0.2).stop()

d7 >> play("-------[--]", hpf=2000, hpr=0.1, room=0.6, pan=[-1, 1], dur=1/2)