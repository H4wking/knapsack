def knapsack(items, weight):
    results = {i: {} for i in range(len(items) + 1)}
    calculated_results = {i: {} for i in range(len(items) + 1)}

    def knapsack_rec(n, w):
        if n == 0 or w == 0:
            return 0

        if w in calculated_results[n]:
            return calculated_results[n][w]

        it = items[n - 1]

        if it[1] > w:
            a = knapsack_rec(n - 1, w)
            calculated_results[n][w] = a
            return a

        else:
            a = it[0] + knapsack_rec(n - 1, w - it[1])
            b = knapsack_rec(n - 1, w)

            if a > b:
                results[n][w] = a
                calculated_results[n][w] = a
                return a

            else:
                calculated_results[n][w] = b
                return b

    total_value = knapsack_rec(len(items), weight)

    result_items = []
    w = weight

    for i in range(len(items), 0, -1):
        if w in results[i]:
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
