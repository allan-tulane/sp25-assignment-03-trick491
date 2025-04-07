# CMPS 2200 Assignment 3
## Answers

**Name:**____Patrick Johnson_____________________


Place all written answers from `assignment-03.md` here for easier grading.
1. 

a. start with a number N and an empty list of coins. Find the largest power of 2, denoted as 2^k, where 2^k ≤ N. Deduct 2^k from N and append 2^k to the coin list until N ≤ 1, then output the resulting list of coins.

b. Optimal; it always selects the largest possible 2^k at each step. Largest coin value will never exceed N. No combination of smaller coins could reduce total number needed without increasing count.

c. Work: O(log n), Span: O(log n)

2.

a. coin denominations D = [1, 4, 5] and target amount N = 8, the greedy algorithm picks 5 and three 1s (4 coins), but the optimal solution uses two 4s (only 2 coins).

b. This problem exhibits optimal substructure since it builds the solution to the overall problem by solving smaller, simpler subproblems.

c. With top-down method, we have to take into account all substructures; therefore span is O(n) and work is O(n).
