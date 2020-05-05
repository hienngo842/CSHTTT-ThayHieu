import math

A = [
    [5, 3, 0, 1],
    [4, 1, 3, 2],
    [3, 4, 0, 5],
    [1, 0, 3, 4],
    [1, 1, 5, 0],
]
print('A: ')
print(A)

rows = []
row_len = len(A)
col_len = len(A[0])

for i in range(row_len):
    for j in range(col_len):
        if A[i][j] != 0:
            continue
        rows.append([i, j])

print('Rows: ')
print(rows)
for item in rows:
    sum_sim = 0
    sum_sim_r = 0
    cur = item[1]
    for i in range(col_len):
        if i == cur:
            continue
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for j in range(row_len):
            if A[j][cur] == 0 or A[j][i] == 0:
                continue
            sum1 += A[j][cur] * A[j][i]
            sum2 += A[j][cur] * A[j][cur]
            sum3 += A[j][i] * A[j][i]
        cos = sum1 / (math.sqrt(sum2 * sum2) * math.sqrt(sum3 * sum3))
        sum_sim += abs(cos)
        sum_sim_r += cos * A[j][i]
    A[item[0]][cur] = sum_sim_r / sum_sim
print('Results: ')
print(A)