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

## Day 17

### Part 2

- It seems like the value 0 will always be at index 0 in the buffer
- That makes sense...if the insert location is 0, it goes after (puts it in index 1)
- If the insert location is the last item, it goes after that extending the list
- So the question then becomes what value is in buffer[1] at 50,000,000 iterations
- Keeping a list of 50,000,001 seems inefficient
- The first several values to go there are 1, 4, 7, 10, 39, 50, 306, 449
- And what would be great is to create a function where you plug in one of those values and get the next
- Then you run that function until you get a number bigger than 50 million and the answer is the input before that
- After a number x gets inserted into location 1, the list is x+1 items long
- And then "location" is consider
- The next location is always (num_steps + location) % len(buffer)
- And in the case where a value x just got dropped into location 1, then it's
- new_location = 387 % (x+1)
- and then it's 386+(new_location) % (x+2)
- and so on until you get a value that's 1
- and x + ? is your new x?
