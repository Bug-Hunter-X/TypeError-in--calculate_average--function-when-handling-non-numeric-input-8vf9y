# Python: Handling Non-Numeric Input in Average Calculation
This repository demonstrates a common Python error: a `TypeError` occurring when a function designed to calculate the average of numbers receives a list containing non-numeric elements (such as strings).
The `bug.py` file shows the problematic code, while `bugSolution.py` presents a robust solution.
## Problem
The original `calculate_average` function attempts to calculate the average of a list of numbers but lacks proper error handling for non-numeric data. This results in a `TypeError` if the list contains elements other than numbers. 
## Solution
The improved function in `bugSolution.py` includes error handling to check for non-numeric elements and to deal with an empty list, ensuring the function works correctly under various input scenarios.