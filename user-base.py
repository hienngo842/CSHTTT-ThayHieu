import math

A = [
    [5, 3, 0, 1],
    [4, 1, 3, 2],
    [3, 4, 0, 5],
    [1, 0, 3, 4],
    [1, 1, 5, 0],
]

print('A = ')
print(A)

rows = []
row_len = len(A)
col_len = len(A[0])

for i in range(row_len):
    for j in range(col_len):
        if A[i][j] != 0:
            continue
        rows.append([i, j])

print('rows: ')
print(rows)

for item in rows:
    cur = item[0]
    sum_sim_r = 0
    sum_sim = 0
    for i in range(row_len):
        if i == cur:
            continue
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for j in range(col_len):
            if A[cur][j] == 0 or A[i][j] == 0:
                continue
            sum1 += A[cur][j] * A[i][j]
            sum2 += A[cur][j] * A[cur][j]
            sum3 += A[i][j] * A[i][j]
        cos = sum1 / (math.sqrt(sum2 * sum2) * math.sqrt(sum3 * sum3))
        sum_sim += abs(cos)
        sum_sim_r += cos * A[i][j]
    A[cur][item[1]] = sum_sim_r / sum_sim
print('results: ')
print(A)