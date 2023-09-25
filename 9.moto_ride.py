from functools import reduce

separ = lambda l: zip(l[::2], l[1::2])
res = lambda l: reduce(lambda s, t: (s[0] + t[0] * (t[1] - s[1]), t[1]), l, (0, 0))[0]
dist = lambda l: res(separ(l))