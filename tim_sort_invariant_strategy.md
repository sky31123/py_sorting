If MIN_RUN length is R, $$K = \frac{N}{R}$$
<br>**Without invariant strategy:** 
<br> $$Total Merges = (R + R) + (2R + R) + (3R + R) + ... \approx 2R + 3R + .. + KR \approx RK\frac{K+1}{2} \approx RK² \approx N².$$
<br>**With Invariant Strategy**
<br>If A is third last and B is second last and C is last run in RUNS,
1) A > B + C 
2) B > C

<br>If above conditions are maintained RUNs will look like Christmas tree from bottom and no merge is required in first while loop, and it doesn't matter which order you merge them it'll be balanced merge.
<br>But if they are not maintained, keep merging in inner loop to keep them balanced. This comes by design in merge sort but not here.

<br>**Example**
RUNS = 20R, 12R, 7R, 4R, 2R, R (ideal balanced)

let's make it unbalanced,
20R, 12R, R, 7R, 4R, 2R, R
if balancing didn't happen this is what total computation look like,
<br>20R + 12R = 32R
<br>32R + R = 33R
<br>33R + 7R = 40R
<br>40R + 4R = 44R
<br>44R + 2R = 46R
<br>46R + R = 47R
<br>Total = 32R + 33R + 40R + 44R + 46R + 47R = **242R**.
<br>
Here's what it looks like with balancing,
<br>20R, 12R, R
<br>20R 12R R 7R = 20R 12R 8R = 32R 8R
<br>32R 8R 4R
<br>32R 8R 4R 2R
<br>32R 8R 4R 2R R
<br>32R + 8R = 40R
<br>40R + 4R = 44R
<br>44R + 2R = 46R
<br>46R + R = 47R
<br>32R (while balancing) + 8R (while balancing) + 40R + 44R + 46R + 47R = **217R**