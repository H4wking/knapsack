def knapsack(items, weight):
    weights_sum = 0
    values_sum = 0
    for item in items:
        weights_sum += item[1]
        values_sum += item[0]
    if weights_sum <= weight:
        return values_sum, list(range(items))

    all_results = [[0 for i in range(len(items) + 1)] for j in range(weight + 1)]
    items_to_keep = [[0 for i in range(len(items) + 1)] for j in range(weight + 1)]

    for i in range(1, len(items) + 1):
        for x in range(1, weight + 1):
            a = all_results[x][i-1]
            b = all_results[x - items[i-1][1]][i-1] + items[i-1][0]
            if items[i-1][1] <= x and b > a:
                all_results[x][i] = b
                items_to_keep[x][i] = 1
            else:
                all_results[x][i] = a

    final_subset = []
    w = weight

    for i in range(len(items), 0, -1):
        if items_to_keep[w][i] == 1:
            final_subset.append(i - 1)
            w -= items[i-1][1]

    return all_results[weight][len(items)], final_subset


if __name__ == "__main__":
    it = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]]
    w = 10
    k = knapsack(it, w)
    res = k[1]
    s = 0
    for el in res:
        s += it[el][1]
    print(k, s)
    print(list(range(it)))
