from unittest import TestCase

from day20_2 import main, create_particles, remove_collisions


class TestDay20(TestCase):
    def setUp(self):
        with open('data/test20_2.txt') as f:
            self.part_two_lines = [line.strip() for line in f.readlines()]


    def test_part_two(self):
        self.assertEqual(main(self.part_two_lines), 1)

    def test_ticks_and_collisions(self):
        particles = create_particles(self.part_two_lines)
        self.assertEqual(len(particles), 4)
        remove_collisions(particles)
        self.assertEqual(len(particles), 4)

        for p in particles.values():
            p.tick()
        remove_collisions(particles)
        self.assertEqual(len(particles), 4)

        for p in particles.values():
            p.tick()
        remove_collisions(particles)
        self.assertEqual(len(particles), 1)
