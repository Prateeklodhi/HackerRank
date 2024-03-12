picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
row_count = len(picture)
col_count = len(picture[0])
for row in picture:
    for col in row:
        if col== 0:
            print(" ", end="")
        else:
            print("*", end="")
    print("")
