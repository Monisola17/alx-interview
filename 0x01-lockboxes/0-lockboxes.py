#!/usr/bin/python3
"""
This module contains a function to check if all boxes can be opened.
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists
        representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = deque([0])

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
