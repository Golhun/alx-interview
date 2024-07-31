#!/usr/bin/python3
"""This module provides a solution to the lockbox,
problem using a Queue implementation."""
from collections import deque


class Queue:
    """A class implementation of a queue."""

    def __init__(self):
        """The constructor method of the class."""
        self.items = deque()

    def enqueue(self, item):
        """This method enqueues items to the queue."""
        self.items.append(item)

    def dequeue(self):
        """This method dequeues items from the queue."""
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        """This method checks if the queue is empty."""
        return len(self.items) == 0

    @property
    def size(self):
        """This getter method returns the size of the queue."""
        return len(self.items)

    def __str__(self):
        """This returns the string representation of the queue."""
        return ", ".join([f"{x}" for x in self.items])


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
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = Queue()
    queue.enqueue(0)

    while queue.size:
        try:
            current_box = queue.dequeue()
            for key in boxes[current_box]:
                if 0 <= key < num_boxes and not visited[key]:
                    visited[key] = True
                    queue.enqueue(key)
        except IndexError:
            return False

    return all(visited)
