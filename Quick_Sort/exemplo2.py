# Visualgo

import random

def quickSort(A, low, high): # expected O(N log N) worst case for ALL cases, the heavy time complexity analysis involving expected values are omitted
    if low < high:
        r = low + random.randrange(high-low+1) # a random index between [low..high]
        A[low], A[r] = A[r], A[low] # tada

        p = A[low] # p is the pivot
        m = low # S1 and S2 are initially empty
        for k in range(low+1, high+1): # expore the unknown region
            # case 2 (PATCHED solution to avoid TLE O(N^2) on input list with identical values)
            if A[k] < p or (A[k] == p and random.randrange(2) == 0):
                m += 1
                A[k], A[m] = A[m], A[k]
            # notice that we do nothing in case 1: A[k] > p
        A[low], A[m] = A[m], A[low] # final step, swap pivot with A[m]

        # a[low..high] ~> a[low..m-1], pivot, a[m+1..high]
        quickSort(A, low, m-1) # recursively sort left sublist
        # A[m] = pivot is already sorted after partition
        quickSort(A, m+1, high) # recursively sort right sublist

    return A
