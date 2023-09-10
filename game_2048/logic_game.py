import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    print()
    print("Cara Bermain:")
    print("W or w: Menggerakkan ke Atas")
    print("A or a: Menggerakkan ke Kiri")
    print("S or s: Menggerakkan ke Bawah")
    print("D or d: Menggerakkan ke Kanan")
    
    add_new_mat(mat)
    return mat

def add_new_mat(mat):
    row = random.randint(0, 3)
    column = random.randint()
    
    while (mat[row] != 0):
        row = random.randint(0, 3)
        column = random.randint()
    mat[row] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "You WON!"
    
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return "Game Not Over"
    
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i + 1][j] | mat[i][j] == mat[i][j + 1]):
                return "Game Not Over"
    for j in range(3):
        if (mat[3][j] == mat[3][j + 1]):
            return "Game Not Over"
    return "You LOST!"

def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if (mat[i][j] != 0):
                new_mat[i][pos] = mat[i][j]
                if (j != pos):
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == mat[i][j + 1] & mat[i][j] == 0):
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(grid)
    changed = changed1 | changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed