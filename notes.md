# Advent Of Code 2017

## Day 13

### Part 2

- Consider example
- Scanner at depth 0, range 3
- You will not get caught by that scanner if you delay 1, 2, 3, 5, 6, 7
- I.e., you get caught at 0, 4, 8...if delay mod 4 == 0
- Or delay mod (range + 1) == 0
- Scanner at depth 1, range 2
- You get caught here if you delay 1, 3, 5
- I.e., you get caught if you (delay + 1) % 2 == 0
- I.e., you get caught if (delay + depth) % (range + 1) == 0
- That formula works for the first scanner too since depth is 0
- Scanner at depth 4, range 4
- Formula says you get caught if (delay + 4) % 5 === 0
- So at 1, 6, 11, but I don't think that's right
- I think you get caught  if you delay 2, 8, 14
- So the mod is six, not five
- So the mod is (range - 1) * 2
- And the thing will be there at delay + depth
- So is it as simple as (delay + depth) % ((range - 1) * 2) == 0?
- I think so, let's try the test case
- That worked, though I'm sure there's a faster way of mathing it instead of iterating
