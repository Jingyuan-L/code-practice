def getElements(arr, queries):
    # Write your code here
    if arr is None or len(arr) <= 1 or queries is None or len(queries) == 0:
        return []

    res = []
    n = arr[0]
    row = []
    for query in queries:
        pos = (query[0] - 1) * n + query[1]
        res.append[arr[pos]]

    return res


if __name__ == '__main__':


    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = getElements(arr, queries)

    print(result)