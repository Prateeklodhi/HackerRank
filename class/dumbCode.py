"""
A simple library to do all the operations which are required in academic practical or projects.
Date of file creation : 04-01-2024
Author: Prateek Kumar Lodhi
"""

import itertools
import time


class Sorting:
    def swap(self, first_value, second_value):
        """takes two values and this function will return the swapped values."""
        first_value = first_value + second_value
        second_value = first_value - second_value
        first_value = first_value - second_value
        return first_value, second_value

    def bubble_sort(self, iterable):
        """
        In bubble sort the biggest value goes to the last place first then the next larger goes to second last place and so on...
        First Iteration
        ===============================
        | [3] | [4] | 1 | 10 | 11 | 2 |
        ===============================
        ===============================
     => | 3 | [4] | [1] | 10 | 11 | 2 |
        ===============================
        ===============================
     => | 3 | 1 | [4] | [10] | 11 | 2 |
        ===============================
        ===============================
     => | 3 | 1 | 4 | [10] | [11] | 2 |
        ===============================
        ===============================
     => | 3 | 1 | 4 | 10 | [11] | [2] |
        ===============================
        ===========================
     => | 3 | 1 | 4 | 10 | 2 | 11 |
        ===========================
        Second Iteration
        ===============================
        | [3] | [1] | 4 | 10 | 2 | 11 |
        ===============================
        ===============================
     => | 1 | [3] | [4] | 10 | 2 | 11 |
        ===============================
        ===============================
     => | 1 | 3 | [4] | [10] | 2 | 11 |
        ===============================
        ===============================
     => | 1 | 3 | 4 | [10] | [2] | 11 |
        ===============================
        ===============================
     => | 1 | 3 | 4 | 2 | [10] | [11] |
        ===============================
        ===========================
     => | 1 | 3 | 4 | 2 | 10 | 11 |
        ===========================
        third Iteration
        ===============================
        | [1] | [3] | 4 | 10 | 2 | 11 |
        ===============================
        ===============================
     => | 1 | [3] | [4] | 2 | 10 | 11 |
        ===============================
        ===============================
     => | 1 | 3 | [4] | [2] | 10 | 11 |
        ===============================
        =============================
     => | 1 | 3 | 2 | 4 | 10 | 11 |
        =============================
         fourth Iteration
        ===============================
        | [1] | [3] | 2 | 4 | 10 | 11 |
        ===============================
        ===============================
     => | 1 | [3] | [2] | 4 | 10 | 11 |
        ===============================
        ===========================
     => | 1 | 2 | 3 | 4 | 10 | 11 |
        ===========================
        sucessfully sorted.....
        """
        length_iterable = len(iterable)
        for counter in range(length_iterable):
            for innercounter in range(counter):
                if iterable[counter] < iterable[innercounter]:
                    iterable[counter], iterable[innercounter] = self.swap(
                        iterable[counter], iterable[innercounter])
        return iterable

    def selectionSort(self, iterable):
        length_iterable = len(iterable)
        for counter, innercounter in itertools.product(range(length_iterable), range(length_iterable)):
            if iterable[counter] < iterable[innercounter]:
                iterable[counter], iterable[innercounter] = self.swap(
                    iterable[counter], iterable[innercounter])
        return iterable

    def insertion_sort(self):
        pass


tobesort = [10, 5, 1, 6, 2, 8, 3]
tobesort.sort()
sortpro = Sorting()

start = time.perf_counter()
print(sortpro.bubble_sort(tobesort))
end = time.perf_counter()

dur = end - start
print(f"bubble sort time   :{dur}")

start = time.perf_counter()
print(sortpro.selectionSort(tobesort))
end = time.perf_counter()
dur = end - start

print(f"selection sort time:f{dur}")
