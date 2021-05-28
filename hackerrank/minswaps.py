def isSorted(arr):
    for ind in range(1, len(arr)):
        if arr[ind] < arr[ind - 1]:
            return False
    return True


def elementsInCycle(start_idx, arr, visited):
    num = 0
    idx = start_idx
    visited[idx] = True
    while arr[idx] != start_idx + 1:
        num += 1
        idx = arr[idx] - 1
        visited[idx] = True
    return num

def minimumSwaps(arr):
    visited = []
    num = 0
    visited = {}
    for i in range(len(arr)):
        if i not in visited:
            n = elementsInCycle(i, arr, visited)
            num += n
    return num


# Complete the minimumSwaps function below.
def minimumSwaps2(arr):
    res = 0
    for i in range(len(arr) - 1):
        print(i, arr)
        min = arr[i]
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min_idx = j
                min = arr[j]
        if min_idx != i:
            res +=1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if isSorted(arr):
            return res
    return res


if __name__ == "__main__":
    f = open('./minswaps.txt')
    f.readline()
    s = f.readline()
    l = [int(x) for x in s.split(" ")]
    print(minimumSwaps(l))
