def knapsack_rec(items, weight, results):
    n = len(items)
    if n == 0 or weight == 0:
        return 0

    if items[n - 1][1] > weight:
        if (n - 1, weight) in results:
            return results[(n - 1, weight)]
        else:
            a = knapsack_rec(items[:-1], weight, results)
            return a

    else:
        if (n - 1, weight - items[n-1][1]) in results:
            a = items[n - 1][0] + results[(n - 1, weight - items[n-1][1])]
        else:
            a = items[n - 1][0] + knapsack_rec(items[:-1], weight - items[n-1][1], results)

        if (n - 1, weight) in results:
            b = results[(n - 1, weight)]
        else:
            b = knapsack_rec(items[:-1], weight, results)

        if a > b:
            results[(n, weight)] = a
            return a
        else:
            return b


def knapsack(items, weight):
    results = {}
    total_value = knapsack_rec(items, weight, results)

    result_items = []
    w = weight

    for i in range(len(items), 0, -1):
        if (i, w) in results:
            result_items.append(i - 1)
            w -= items[i-1][1]

    return total_value, result_items


if __name__ == "__main__":
    it = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]] # [9, 8, 3, 2, 1, 0]
    w = 20
    k = knapsack(it, w)
    res = k[1]
    s = 0
    print(k)
    for el in res:
        s += it[el][1]
    print(k, s)
