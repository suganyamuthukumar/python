import array as arr


def findMaxProduct():
    A = arr.array('i', [8, 7, 6, 5, 4, 3, 2, 9])
    N = 8
    i: int = 0
    maxProduct = 0
    rightIndex: int = 0;
    while i < N:
        index: int = i + 1
        nextPerfectSqrIndex: int = index * index
        nextIndex: int = ((index * 2) + 1)
        while (nextPerfectSqrIndex / index) < N + 1:
            if nextPerfectSqrIndex % index == 0:
                rightIndex = int((nextPerfectSqrIndex / index)) - 1
                print("(" + str(index) + "," + str((rightIndex + 1)) + ")")
                if rightIndex == i:
                    if maxProduct < A[i]:
                        maxProduct = A[i]
                else:
                    product: int = A[i] * A[rightIndex]
                    if maxProduct < product:
                        maxProduct = product
            nextPerfectSqrIndex += nextIndex
            nextIndex += 2
        i += 1
    print(maxProduct)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    findMaxProduct()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
