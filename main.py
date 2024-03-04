# 1 
# -------------------------------------------------------------------

def load_matrix_from_file(path):
    with open(path, 'r') as file:
        rows = int(file.readline().strip())
        cols = int(file.readline().strip())
        matrix = [list(map(int, file.readline().strip().split(' '))) for _ in range(rows)]

    return matrix

def select_elements_closest_to_zero(matrix, group_size=10):
    total_sum = 0
    selected_elements = []
    num_rows = len(matrix)

    def find_best_combination_for_group(group):
        from itertools import product

        combinations = list(product(*group))
        best_combination = min(combinations, key=lambda x: abs(sum(x)))
        #print(sum(best_combination))
        return best_combination

    for i in range(0, num_rows, group_size):
        group = matrix[i:i+group_size]
        print(group)
        best_combination = find_best_combination_for_group(group)
        selected_elements.extend(best_combination)
        total_sum += sum(best_combination)

    return selected_elements, total_sum

filepath = "task1_data.txt"
choices, total_sum = select_elements_closest_to_zero(load_matrix_from_file(filepath))

print(total_sum - choices[-1])
print(choices[-1])
print(total_sum)

# 2
# ----------------------------------------------------------------------------------

def calculate_min_penalty(file_path):
    with open(file_path, 'r') as file:
        distances = [int(line.strip()) for line in file]
    distances.insert(0, 0)  

    n = len(distances)
    dp = [float('inf')] * n
    dp[0] = 0  

    for i in range(1, n):
        for j in range(i):
            penalty = (400 - (distances[i] - distances[j])) ** 2
            dp[i] = min(dp[i], dp[j] + penalty)
    return dp

file_path = "data-2.txt"
min_penalty = calculate_min_penalty(file_path)
print(f"Minimum total penalty: {min_penalty}")

# 3
# --------------------------------------------------------------------------------

def read_tokens(path):
    try:
        with open(path, 'r') as file:
            content = file.read().strip()
            number_list = [int(char) for char in content]
        return number_list
    except FileNotFoundError:
        print(f"Súbor nebol nájdený: {path}")

def max_win(tokens):
    n = len(tokens)
    dp = [[0] * n for _ in range (n)]
    for length in range(2, n+2, 2):
        for i in range(n-length+1):
            j = i+length-1
            if i == j:
                dp[i][j] = tokens[i]
            else:
                left_choice = tokens[i] + ((dp[i+2][j] if i+2 <= j else 0) if tokens[i+1] > tokens[j] else (dp[i+1][j-1] if i+1 <= j-1 else 0))
                right_choice = tokens[j] + ((dp[i+1][j-1] if i+1 <= j-1 else 0) if tokens[i] > tokens[j-1] else (dp[i][j-2] if i <= j-2 else 0))

                dp[i][j] = max(left_choice, right_choice)
    print(dp)
    return dp[0][n-1]

file = 'zetony.txt'

tokens = read_tokens(file)
#tokens = [1, 2, 1, 1, 2, 9, 6, 3]
win = max_win(tokens)
total = sum(tokens)

print(f"Total: {total}")
print(f"Win: {win}")
print(f"Dealer takes: {total - win}")