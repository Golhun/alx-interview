#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int):
        A list where each element is a list of keys
        corresponding to other boxes.
        The first box (boxes[0]) is unlocked initially.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Initialize the set to keep track of visited boxes
    visited = set()

    # Initialize the stack for Depth-First Search (DFS) with the first box
    stack = [0]

    while stack:
        # Get the current box from the stack
        box = stack.pop()

        if box not in visited:
            # Mark the current box as visited
            visited.add(box)

            # Add all keys in the current box to the stack,
            # if they lead to unvisited boxes
            stack.extend(
                key for key in boxes[box] if key not in visited
            )

    return len(visited) == len(boxes)
