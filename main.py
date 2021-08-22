width = 8  # x
height = 6  # y

Cell = []
px = 0
py = 0
for x in range(width):
    column =[]
    px = px + 1
    py = 0
    for y in range(height):
        py = py + 1
        column.append(str(px) + ',' + str(py))

    Cell.append(column)


print(Cell)


print("\n")
for y in range(height):
    for x in range(width):
        print(Cell[x][y], end=' | ')
    print()
