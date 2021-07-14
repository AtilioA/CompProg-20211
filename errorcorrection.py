while True:
    n = int(input())
    if n == 0:
        break

    rowDiff = None
    colDiff = None
    corrupt = None

    matrix = [[] for _ in range(n)]
    for row in range(n):
        rowData = list(map(int, input().split()))

        for j, entry in enumerate(rowData):
            matrix[j].append(entry)

        if sum(rowData) % 2: # Even sum
            if not rowDiff:
                rowDiff = row + 1
            else:
                corrupt = True

    if not corrupt:
        for j, entry in enumerate(matrix):
            if sum(entry) % 2:
                if not colDiff:
                    colDiff = j + 1
                else:
                    corrupt = True

    if not corrupt:
        if not (colDiff or rowDiff):
            print("OK")
        else:
            print("Change bit ({},{})".format(rowDiff, colDiff))
    else:
        print("Corrupt")
