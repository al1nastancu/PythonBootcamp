# Mark an X on the map

row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = int(input("Mark the spot row & column: "))
x = int(position / 10)
y = position % 10
map[x][y] = 'X'
print(f'{row1}\n{row2}\n{row3}')