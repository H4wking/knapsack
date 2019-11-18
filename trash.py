def knapsack(items, weight):
    weights_sum = 0
    values_sum = 0
    for item in items:
        weights_sum += item[1]
        values_sum += item[0]
    if weights_sum <= weight:
        return values_sum, list(range(items))

    all_results = [[0 for i in range(weight + 1)] for j in range(len(items) + 1)]
    final_subset = []

    for i in range(1, len(items) + 1):
        is_in_final_subset = False
        for x in range(1, weight + 1):
            a = all_results[i-1][x]
            b = all_results[i-1][x - items[i-1][1]] + items[i-1][0]
            if items[i-1][1] > x:
                all_results[i][x] = a
            else:
                all_results[i][x] = max([a, b])
                # if not is_in_final_subset and b > a:
                #     final_subset.append(i - 1)
                #     is_in_final_subset = True
                if not is_in_final_subset and b > a:
                    final_subset.append(i - 1)
                    is_in_final_subset = True

    # final_subset = []

    def _find_subset(i, x):
        if i > 0 and x > 0:
            # if all_results[i-1][weight - items[i-1][1]] + items[i-1][0] > all_results[i-1][weight - items[i-1][1]]:
            #     print(i)
            #     return [i] + _find_subset(i - 1)
            if all_results[i-1][x] == all_results[i][x]:
                _find_subset(i - 1, x)
            else:
                final_subset.append(i)
                _find_subset(i - 1, x - items[i-2][1])

    _find_subset(len(items) - 1, weight)

    # if i > 0 and j > 0:
    #     if dp[i - 1][j] == dp[i][j]:
    #         _construct_solution(dp, wt, i - 1, j, optimal_set)
    #     else:
    #         optimal_set.add(i)
    #         _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


    # for i in range(len(items) - 1, -1, -1):
    #     if all_results[i][weight - items[i][1]] + items[i][0] > all_results[i-1][weight]:
    #         final_subset.append(i)

    return all_results[len(items)][weight], final_subset


if __name__ == "__main__":
    it = [[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]]
    w = 10
    k = knapsack(it, w)
    res = k[1]
    s = 0
    print(k)
    for el in res:
        s += it[el][1]
    print(k, s)
