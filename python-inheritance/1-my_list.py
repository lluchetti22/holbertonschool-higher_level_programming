#!/usr/bin/python3
"""Module that defines MyList, a subclass of list."""


class MyList(list):
    """A subclass of list with a custom print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
