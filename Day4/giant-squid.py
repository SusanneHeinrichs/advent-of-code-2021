import copy

with open('data/day_4.txt', 'r') as f:
    lines = f.readlines()
    bingo = [entry.strip() for entry in lines]

drawn_numbers = list(bingo[0].split(","))
boards = []
board = []
for i in range(2, len(bingo)):
    if(bingo[i] == ''):
        boards.append(board)
        board = []
    else:
        board.append(list(bingo[i].split()))

marked_boards = copy.deepcopy(boards)
def mark_n_check():
    for number in drawn_numbers:
        result= False
        for i in range(len(boards)):
                for j in range(len(boards[0])):
                    for k in range(0,5):
                        if(marked_boards[i][j][k] == number):
                            marked_boards[i][j][k] = "X"
        for i in range(len(boards)):
            for j in range(len(boards[0])):
                result = all(X == marked_boards[i][j][0] for X in marked_boards[i][j])
                if result: 
                    return marked_boards[i], number

                
result = mark_n_check()
print(result[0])
sum = 0
for i in range(0,5):
    for j in range(0,5):
        if result[0][i][j] != 'X':
            sum += int(result[0][i][j])
end_result = sum * int(result[1])
print(end_result)









