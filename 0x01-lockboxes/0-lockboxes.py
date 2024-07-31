#!/usr/bin/python3


class BoxUnlocker:
    """
    A class to determine if all boxes can be unlocked,
    given the initial state.
    Each box may contain keys to other boxes,
    and the first box is initially
    unlocked.
    """

    def __init__(self, boxes):
        """
        Initializes the BoxUnlocker with a list of boxes.

        Args:
            boxes (list of list of int):
            A list where each element is a list of
            keys corresponding to other boxes.
        """
        self.boxes = boxes
        self.visited = set()
        self.stack = []

    def can_unlock_all(self):
        """
        Determines if all boxes can be unlocked.

        Returns:
            bool: True if all boxes can be unlocked, False otherwise.
        """
        # Start with the first box
        self.stack.append(0)

        while self.stack:
            box = self.stack.pop()
            if box not in self.visited:
                self.visited.add(box)
                # Add all keys in the current box to the stack
                self.stack.extend(
                    key for key in self.boxes[box] if key not in self.visited
                )

        # Check if all boxes have been visited
        return len(self.visited) == len(self.boxes)
