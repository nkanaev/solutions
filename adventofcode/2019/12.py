import sys, itertools, re, math, functools


class Moon:
    def __init__(self, posx, posy, posz):
        self.posx, self.posy, self.posz = posx, posy, posz
        self.velx, self.vely, self.velz = 0, 0, 0

    def copy(self):
        return Moon(self.posx, self.posy, self.posz)

    def astuple(self):
        return (
            self.posx, self.posy, self.posz,
            self.velx, self.vely, self.velz,
        )

    def __hash__(self):
        return hash(self.astuple())

    def __eq__(self, other):
        return self.astuple() == other.astuple()

    def __repr__(self):
        return 'Moon(x=%3d, y=%3d, z=%3d, vx=%3d, vy=%3d, vz=%3d)' % self.astuple()


def comp(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    return 0


combinations = list(itertools.combinations([0, 1, 2, 3], 2))
combinations += [(b, a) for a, b in combinations]

def timestep(moons):
    for i1, i2 in combinations:
        moons[i1].velx += comp(moons[i1].posx, moons[i2].posx)
        moons[i1].vely += comp(moons[i1].posy, moons[i2].posy)
        moons[i1].velz += comp(moons[i1].posz, moons[i2].posz)
    for moon in moons:
        moon.posx += moon.velx
        moon.posy += moon.vely
        moon.posz += moon.velz


def energy(m):
    return (abs(m.posx)+abs(m.posy)+abs(m.posz)) \
         * (abs(m.velx)+abs(m.vely)+abs(m.velz))


def lcm(a, b):
    return a * b // math.gcd(a, b)


def sol1(moons):
    moons = [m.copy() for m in moons]
    for _ in range(1000):
        timestep(moons)
    return sum(energy(m) for m in moons)


def sol2(moons):
    pass


def main():
    def readmoon(line):
        xyz = list(map(int, re.match('<x=(.+), y=(.+), z=(.+)>', line).groups()))
        return Moon(*xyz)
    moons = [readmoon(sys.stdin.readline()) for _ in range(4)]
    print(sol1(moons))
    print(sol2(moons))


main()
