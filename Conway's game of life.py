def get_generation(matrix, generations):
    cells = []
    for i in range(len(matrix)):
        cells.append([])
        for j in range(len(matrix[0])):
            cells[i].append(matrix[i][j])
    n = 0
    while n < generations:
        cells = moore(cells); # For each step n+2xn+2 matrix is created to simulate a dead cell neighbour boundary
        cells = newcells(cells); # Calls the function that generated the next step
        n += 1
    cells = crop(cells)
    return cells


def newcells(cells):  # To calculate the next generation from the rules
    gen = []
    for i in range(len(cells)):
        gen.append([])
        for j in range(len(cells[0])):
            val = count(i, j, cells)
            if val == 2:
                gen[i].append(cells[i][j])
            elif val == 3:
                gen[i].append(1)
            elif val < 2 or val > 3:
                gen[i].append(0)
            else:
                gen[i].append(0)
    return gen


def count(r, c, coods):  # Count the number of live cells
    l = [1, 0, -1];
    tot = 0
    for i in l:
        for j in l:
            if i == 0 and j == 0:
                pass
            elif r + i < 0 or c + j < 0 or r + i >= len(coods) or c + j >= len(coods[0]):
                pass
            elif coods[r + i][c + j] == 1:
                tot += 1
            else:
                pass
    return tot


def crop(cells):  # To remove the suurounding dead cells
    cells = removerow(cells);
    cells = transpose(cells);
    cells = removerow(cells);
    cells = transpose(cells)
    return cells


def removerow(cells):  # To remove dead cell rows
    gen = cells
    for i in range(len(cells)):
        if set(cells[i]) != {0}:
            break
        else:
            gen = gen[1:]
    for i in range(len(cells) - 1, -1, -1):
        if set(cells[i]) != {0}:
            break
        else:
            gen = gen[: len(gen) - 1]
    return gen


def transpose(m):  # To return the transpose
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])
    return t


def moore(cells):  # To create the surrounding dead cells
    for i in range(len(cells)):
        cells[i].append(0);
        cells[i].insert(0, 0)
    cells.insert(0, []);
    cells.append([])
    for j in range(len(cells[1])):
        cells[0].append(0);
        cells[len(cells) - 1].append(0)
    return cells

print("""Here a Conway's game of life (for anyone who is familiar to the game rule) 
is programmed that takes a matrix of 1's and 0's that represents live and dead cells 
and the number of steps as input to get the final matrix of the same format 
that represent's the game of life generations for the following input

refer to line 101 of the script to enter the input matrix
""")

input_matrix = [[1,0,0],[0,1,1],[1,1,0]] # Enter your initial matrix in list format (eg: [[1,0,0],[0,1,1],[1,1,0]] )
input_steps = int(input("Enter the generation step : "))
print("")
print(get_generation(input_matrix, input_steps))