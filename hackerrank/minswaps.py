# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.


# Main workhorse which builds the cycle from the element index provided
# Also marks all elements in the cycle in visited set.
# By cycle I mean if we have [1, 3, 4, 2, 5] list and 3 as element we start building the cycle, it would be 3 -> 4 -> 2 cycle
def elementsInCycle(start_idx, arr, visited):
    num = 0
    idx = start_idx
    visited[idx] = True
    while arr[idx] != start_idx + 1:
        num += 1
        idx = arr[idx] - 1
        visited[idx] = True
    return num

# More effective algorightm
# We calculate cycle for each non-checked element. Sum of number of elements in cycles are the answer
def minimumSwapsEffective(arr):
    num = 0
    # Must be dictionary otherwise search operation below makes it quadratic. 
    # Nice thing to practice in python profiling
    visited = {}
    for i in range(len(arr)):
        if i not in visited:
            n = elementsInCycle(i, arr, visited)
            num += n
    return num

def isSorted(arr):
    for ind in range(1, len(arr)):
        if arr[ind] < arr[ind - 1]:
            return False
    return True

# Classic select sort, on each step we swap (or don't) min element.
# In case we swap we increment the counter
# It takes quadratic time to finish (we check if it's already sorted to stop but that could even make it worse)
def minimumSwapsSlow(arr):
    num = 0
    for i in range(len(arr) - 1):
        print(i, arr)
        min = arr[i]
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min_idx = j
                min = arr[j]
        if min_idx != i:
            num +=1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if isSorted(arr):
            return num
    return num

if __name__ == "__main__":
    with open('./minswaps.txt') as f:
        num = f.readline()
        data = f.readline()
    print(minimumSwapsEffective([int(x) for x in data.split(" ")]))    