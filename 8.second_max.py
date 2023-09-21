from functools import reduce

max_st = lambda source: reduce(
    lambda ms, a: \
        ms if ms[0] == a \
        else (a, ms[1] + [ms[0]]) if ms[0] < a \
        else (ms[0], ms[1] + [a]),
    source,
    (source[0], []))

max2 = lambda source: max_st(max_st(source)[1])[0]