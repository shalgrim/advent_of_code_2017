from collections import defaultdict


class Particle(object):
    def __init__(self, px, py, pz, vx, vy, vz, ax, ay, az):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az

    @property
    def position(self):
        return self.px, self.py, self.pz

    @staticmethod
    def octant(x, y, z):
        if x >= 0:
            if y >= 0:
                if z >= 0:
                    return 1
                else:
                    return 5
            elif z >= 0:
                return 2
            else:
                return 6
        elif y >= 0:
            if z >= 0:
                return 4
            else:
                return 8
        elif z >= 0:
            return 3
        else:
            return 7

    @property
    def current_octant(self):
        return self.octant(self.px, self.py, self.pz)

    @property
    def final_octant(self):
        return self.octant(self.ax, self.ay, self.az)

    @property
    def in_final_octant(self):
        return self.current_octant == self.final_octant

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz


def create_particle(line):
    elements = line.split(', ')
    coords = [e[3:-1] for e in elements]
    individual_coords = [i for c in coords for i in c.split(',')]
    intvals = [int(ic) for ic in individual_coords]
    return Particle(*intvals)


def remove_collisions(particles):
    positions_to_keys = defaultdict(list)

    for k, p in particles.items():
        positions_to_keys[p.position].append(k)

    for v in positions_to_keys.values():
        if len(v) > 1:
            for pindex in v:
                del particles[pindex]


def terminating_condition(particles):
    if not all (p.in_final_octant for p in particles):
        return False
    # TODO: for each octant, make sure particles are getting further away from each other
    # for o in range(8):
    #     if True:
    #         return False
    return True


def create_particles(lines):
    return {i: create_particle(line) for i, line in enumerate(lines)}


def main(lines):
    particles = create_particles(lines)
    remove_collisions(particles)
    while not terminating_condition(particles.values()):
        for p in particles.values():
            p.tick()
        remove_collisions(particles)
        print(f'{len(particles)}=')

    return len(particles)


if __name__ == '__main__':
    with open('data/input20.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))