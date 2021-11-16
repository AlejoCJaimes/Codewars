def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def choose_best_sum(t, k, ls):
    temp_combinations = []
    temp_sumatories = []
    temp_list = list(filter(lambda x: (x <= t), ls))
    temp_list.sort()

    for combination in combinations(temp_list, k):
        _sum = sum(combination)

        if _sum <= t:
            temp_combinations.append(combination)
            temp_sumatories.append(_sum)

    # temp_combinations.sort()
    # temp_combinations.reverse()
    temp_sumatories.sort()
    temp_sumatories.reverse()

    return temp_sumatories[0] if bool(temp_sumatories) else None


if __name__ == '__main__':
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,
          123, 2333, 144, 50, 132, 123, 34, 89]
    print(choose_best_sum(230, 4, xs))
    print(choose_best_sum(430, 5, xs))
    print(choose_best_sum(430, 8, xs))
