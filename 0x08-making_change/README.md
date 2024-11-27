# 0. Change Comes From Within - Coin Change Problem

The goal of this project is to tackle the classic **coin change problem** using both **greedy algorithms** and **dynamic programming**. You will determine the minimum number of coins required to make a given amount using a list of available coin denominations. This problem will test your understanding of algorithmic efficiency, decision-making, and the application of dynamic programming techniques.

## Project Overview

In this project, you will implement two approaches to solve the **coin change problem**:

1. **Greedy Algorithm**:
   - A greedy approach attempts to make the optimal choice at each step, aiming for a local optimum that results in a globally optimal solution. This approach may fail in some cases, so it is essential to determine if it is appropriate for your given coin denominations.

2. **Dynamic Programming**:
   - Dynamic programming (DP) is a technique used to solve problems by breaking them down into simpler sub-problems. In this case, DP allows you to optimize the solution to the coin change problem by solving overlapping subproblems and storing their results to avoid redundant computations.

The goal is to determine the minimum number of coins needed to make a target amount, given a set of available coin denominations.

## Concepts Covered

To successfully complete this project, you will need to have an understanding of the following key concepts:

### Greedy Algorithms

- Understanding how greedy algorithms work and why they may be suitable for the coin change problem.
- Recognizing the limitations of greedy algorithms and understanding the scenarios where they might not provide an optimal solution.

### Dynamic Programming

- Basic principles of dynamic programming as a method to solve optimization problems.
- The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

### Algorithmic Complexity

- Analyzing the time and space complexity of the solutions.
- Striving for solutions with lower complexity to meet runtime constraints.

### Problem-Solving Strategies

- Breaking down the problem into smaller, manageable sub-problems.
- Comparing iterative and recursive approaches to dynamic programming.

### Python Programming

- Manipulating lists and utilizing list comprehensions.
- Implementing functions with efficient looping and conditional statements.

## Resources

To help you complete this project successfully, the following resources are recommended:

- **Python Official Documentation**: For control flow tools such as loops and if statements.
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to Find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=GJrLfj7yq1A)

These resources will help you understand both greedy and dynamic programming approaches to solve the problem.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow **PEP 8** style guidelines (version 1.7.x).
- All files must be executable.

## Approach

1. **Greedy Approach**:
   - Sort the coin denominations in descending order.
   - Iterate over the sorted list, choosing as many coins as possible from the largest denomination to the smallest, until the target amount is reached or the coins run out.

2. **Dynamic Programming Approach**:
   - Use a bottom-up DP approach to store the minimum number of coins needed for all amounts up to the target amount.
   - Solve subproblems iteratively by considering each coin and each possible amount.

## Algorithmic Complexity

- The **Greedy algorithm** has a time complexity of \(O(n \log n)\) due to sorting, where \(n\) is the number of denominations.
- The **Dynamic Programming approach** has a time complexity of \(O(m \times n)\), where \(m\) is the target amount and \(n\) is the number of coin denominations.

## Conclusion

This project will reinforce your skills in algorithm design, optimization, and Python programming. By comparing the greedy algorithm and dynamic programming approach, you will gain a deeper understanding of which strategies are best suited for different problem constraints.

Good luck, and happy coding!

## Additional Resources

- **Mock Technical Interview**: An opportunity to test your understanding of the concepts and the solutions you've implemented in a simulated interview setting.

