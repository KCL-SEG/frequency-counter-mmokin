"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item)
        if key not in frequencies:
            frequencies[key] = 0
        frequencies[key] += 1
    # Your code goes here
    return frequencies
