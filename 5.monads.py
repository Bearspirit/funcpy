from pymonad.maybe import Just, Nothing

put = lambda dl, dr: lambda lr: Just((lr[0] + dl, lr[1] + dr))
stands = lambda max_delta: lambda lr: \
    Just(lr) if abs(lr[0] - lr[1]) <= max_delta else Nothing

left = lambda num: lambda lr: Just(lr) >> put(num, 0) >> stands(4)
right = lambda num: lambda lr: Just(lr) >> put(0, num) >> stands(4)
banana = lambda lr: Nothing

show = lambda maybe: print("fail" if maybe == Nothing else "OK")

begin = lambda: Just((0, 0))

show(begin() >> left(3) >> right(4) >> left(-1))
show(begin() >> left(4) >> right(7) >> left(-2))
show(begin() >> left(2) >> banana >> right(4) >> left(-1))