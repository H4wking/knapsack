def knapsack(items, weight):
    weights_sum = 0
    values_sum = 0
    for item in items:
        weights_sum += item[1]
        values_sum += item[0]
    if weights_sum <= weight:
        return values_sum, list(range(items))

    all_results = [0 for j in range(len(items) + 1)]
    items_to_keep = []

    def _find_opt_rec(i, x):
        a = _find_opt_rec(i - 1, x) if i - 1 > 0 else 0
        b = _find_opt_rec(i - 1, x - items[i - 1][1]) + items[i - 1][0] if i - 1 > 0 else 0
        if items[i-1][1] <= x and b > a:
            return b
            # items_to_keep[i][x] = 1
        else:
            return a

    for i in range(1, len(items) + 1):
        a = all_results[i-1]
        b = _find_opt_rec(i - 1, weight - items[i-1][1]) + items[i-1][0]
        if items[i-1][1] <= weight and b > a:
            all_results[i] = b
            items_to_keep.append(i - 1)
        else:
            all_results[i] = a



    final_subset = []
    w = weight

    # for i in range(len(items), 0, -1):
    #     if items_to_keep[i][w] == 1:
    #         final_subset.append(i - 1)
    #         w -= items[i-1][1]

    return all_results[len(items)], items_to_keep


if __name__ == "__main__":
    it = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]] //[9, 8, 3, 2, 1, 0]
    w = 20
    k = knapsack(it, w)
    res = k[1]
    s = 0
    print(k)
    for el in res:
        s += it[el][1]
    print(k, s)
