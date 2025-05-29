print("  B   I   N   G   O")
print("---------------------")
numbers = [7, 22, 31, 50, 68, 3, 18, 42, 58, 71, 12, 29, 47, 62, 9, 16, 35, 53, 75, 1, 25, 40, 49, 61]
table_size = 5
row_x = table_size // 2
row_y = table_size // 2
data= 0
for x in range(table_size):
    for y in range(table_size):
        if x == row_x and y == row_y:
            print(f"{' ':4}", end=" ")
        else:
            print(f"{numbers[data]:>3}", end=" ")
            data += 1
    print()
print("--------------------")