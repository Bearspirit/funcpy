from functools import reduce

conquest_campaign = lambda n, m, battalion: \
    batle(n, m, double(battalion), 1)

double = lambda a: _double(a, set())

def _double(source, dest):
    if len(source) == 0:
        return dest
    return _double(source[2:], {tuple(source[:2])} | dest)

neighbors = lambda point: {
    point,
    (point[0] - 1, point[1]),
    (point[0] + 1, point[1]),
    (point[0], point[1] - 1),
    (point[0], point[1] + 1),
    }

all_neighbors = lambda points: reduce(
    lambda a, point: a | neighbors(point), points, set())

valid = lambda n, m: lambda double: \
    double[0] > 0 and double[0] <= n and double[1] > 0 and double[1] <= m

def batle(n, m, points, count):
    if len(points) == n * m:
        return count
    return batle(n, m, set(filter(valid(n, m), all_neighbors(points))), count + 1)