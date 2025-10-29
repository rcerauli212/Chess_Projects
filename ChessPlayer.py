
# This code takes a csv file of a chess gasme noted in algebraic notation from raw_data.txt and plays the game, exporting the game as 
# a list of lists into chess_array.csv


import numpy as np
import pandas as pd
import csv

board_pos_array = ["a1","a2","a3","a4","a5","a6","a7","a8"],["b1","b2","b3","b4","b5","b6","b7","b8"],["c1","c2","c3","c4","c5","c6","c7","c8"],["d1","d2","d3","d4","d5","d6","d7","d8"],["e1","e2","e3","e4","e5","e6","e7","e8"],["f1","f2","f3","f4","f5","f6","f7","f8"],["g1","g2","g3","g4","g5","g6","g7","g8"],["h1","h2","h3","h4","h5","h6","h7","h8"]
board_pos = ["mover","a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8","d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
start_pos = ["W","WR","WP","E","E","E","E","BP","BR","WN","WP","E","E","E","E","BP","BN","WB","WP","E","E","E","E","BP","BB","WQ","WP","E","E","E","E","BP","BQ","WK","WP","E","E","E","E","BP","BK","WB","WP","E","E","E","E","BP","BB","WN","WP","E","E","E","E","BP","BN","WR","WP","E","E","E","E","BP","BR"]
turn = "W"
old_pos = "W,WR,WP,E,E,E,E,BP,BR,WN,WP,E,E,E,E,BP,BN,WB,WP,E,E,E,E,BP,BB,WQ,WP,E,E,E,E,BP,BQ,WK,WP,E,E,E,E,BP,BK,WB,WP,E,E,E,E,BP,BB,WN,WP,E,E,E,E,BP,BN,WR,WP,E,E,E,E,BP,BR"
old_pos_array = ["WR","WP","E","E","E","E","BP","BR"],["WN","WP","E","E","E","E","BP","BN"],["WB","WP","E","E","E","E","BP","BB"],["WQ","WP","E","E","E","E","BP","BQ"],["WK","WP","E","E","E","E","BP","BK"],["WB","WP","E","E","E","E","BP","BB"],["WN","WP","E","E","E","E","BP","BN"],["WR","WP","E","E","E","E","BP","BR"]
new_pos = "W,WR,WP,E,E,E,E,BP,BR,WN,WP,E,E,E,E,BP,BN,WB,WP,E,E,E,E,BP,BB,WQ,WP,E,E,E,E,BP,BQ,WK,WP,E,E,E,E,BP,BK,WB,WP,E,E,E,E,BP,BB,WN,WP,E,E,E,E,BP,BN,WR,WP,E,E,E,E,BP,BR"
lower_alpha = "abcdefgh"
numbers = "01234567"
numbers1 = "12345678"

with open("Achievements/AI-Chess-Project/data_organizer/raw_data.txt", "r") as raw:
    game = raw.read()
    game1 = (game.split("."))[1::]
    game2, game3, game4 = [], [], []
    for x in game1:
        game2.append(x[1:len(x)-2:1])
    for y in game2:
        game3.append(y.strip())
    for z in game3:
        game4.append(z.split(" "))
    dict1, dict2, dict3 = {}, {}, {}
    for x in range(len(board_pos)):
        dict1[board_pos[x]] = start_pos[x]
    for y in range(len(numbers)):
        dict2[lower_alpha[y]] = int(numbers[y])
    for z in range(len(numbers)):
        dict3[numbers1[z]] = int(numbers[z])
    chess_board_piece = np.asarray(old_pos_array)
    chess_board_pieces = pd.DataFrame(chess_board_piece, index=[_ for _ in lower_alpha], columns=[_ for _ in numbers1])  
    n = 0
    final_pieces = [["' ',WR,WP,E,E,E,E,BP,BR,WN,WP,E,E,E,E,BP,BN,WB,WP,E,E,E,E,BP,BB,WQ,WP,E,E,E,E,BP,BQ,WK,WP,E,E,E,E,BP,BK,WB,WP,E,E,E,E,BP,BB,WN,WP,E,E,E,E,BP,BN,WR,WP,E,E,E,E,BP,BR"]]
    for move in game4:
        if True:
            n += 1
            checkw_bool = False
            checkb_bool = False
            matew_bool = False
            mateb_bool = False
            if len(move) == 2 or len(move) == 3:
                h = 2
                if "+" in move[0]:
                    checkw_bool = True
                    move[0] = move[0][:len(move[0]) - 1]
                if "+" in move[1]:
                    checkb_bool = True
                    move[1] = move[1][:len(move[1]) - 1]
                if "#" in move[0]:
                    matew_bool = True
                    move[0] = move[0][:len(move[0]) - 1]
                if "#" in move[1]:
                    mateb_bool = True
                    move[1] = move[1][:len(move[1]) - 1]
            if len(move) == 1:
                h = 1
                if "+" in move[0]:
                    checkw_bool = True
                    move[0] = move[0][:len(move[0]) - 1]
                if "#" in move[0]:
                    matew_bool = True
                    move[0] = move[0][:len(move[0]) - 1]
            for z in range(h):
                if z == 0:
                    ww = "W"
                if z == 1:
                    ww = "B"

#################################### MOVE LOGIC ####################################

#### PAWN LOGIC ####
                if move[z][0] in lower_alpha:
                    if z == 0:
                        if move[z][0] in lower_alpha and "x" not in move[z]:
                            if chess_board_pieces.iloc[dict2[move[0][0]], dict3[move[0][1]] - 1] == "{0}P".format(ww):
                                chess_board_pieces.loc[move[0][0], str(int(move[0][1]) - 1)] = "E"
                            elif chess_board_pieces.iloc[dict2[move[0][0]], dict3[move[0][1]] - 2] == "{0}P".format(ww) and chess_board_pieces.iloc[dict2[move[0][0]], dict3[move[0][1]] - 1] == "E":
                                chess_board_pieces.loc[move[0][0], str(int(move[0][1]) - 2)] = "E"
                            chess_board_pieces.iloc[dict2[move[0][0]], dict3[move[0][1]]] = "{0}P".format(ww)
                        if move[0][0] in lower_alpha and "x" in move[0]:
                            if chess_board_pieces.iloc[dict2[move[0][2]], dict3[move[0][3]]] != "E":
                                chess_board_pieces.iloc[dict2[move[0][0]], dict3[move[0][3]] - 1] = "E"
                            elif chess_board_pieces.iloc[dict2[move[0][2]], dict3[move[0][3]]] == "E":
                                chess_board_pieces.iloc[dict2[move[0][2]], dict3[move[0][3]] - 1] = "E"
                            chess_board_pieces.loc[move[0][2], move[0][3]] = "{0}P".format(ww)
                        if "{0}P".format(ww) in chess_board_pieces["8"].values:
                            for letter in lower_alpha:
                                if chess_board_pieces.loc[letter, "8"] == "{0}P".format(ww):
                                    chess_board_pieces.loc[letter, "8"] = "W{}".format(move[0][-1])
                            move[0] = move[0][:len(move[0]) - 2]
                    if z == 1:
                        if move[1][0] in lower_alpha and "x" not in move[1]:
                            if chess_board_pieces.iloc[dict2[move[1][0]], dict3[move[1][1]] + 1] == "{0}P".format(ww):
                                chess_board_pieces.loc[move[1][0], str(int(move[1][1]) + 1)] = "E"
                            elif chess_board_pieces.iloc[dict2[move[1][0]], dict3[move[1][1]] + 2] == "{0}P".format(ww) and chess_board_pieces.iloc[dict2[move[1][0]], dict3[move[1][1]] + 1] == "E":
                                chess_board_pieces.loc[move[1][0], str(int(move[1][1]) + 2)] = "E"
                            chess_board_pieces.iloc[dict2[move[1][0]], dict3[move[1][1]]] = "{0}P".format(ww)
                        if move[1][0] in lower_alpha and "x" in move[1]:
                            if chess_board_pieces.iloc[dict2[move[1][2]], dict3[move[1][3]]] != "E":
                                chess_board_pieces.iloc[dict2[move[1][0]], dict3[move[1][3]] + 1] = "E"
                            elif chess_board_pieces.iloc[dict2[move[1][2]], dict3[move[1][3]]] == "E":
                                chess_board_pieces.iloc[dict2[move[1][2]], dict3[move[1][3]] + 1] = "E"
                            chess_board_pieces.loc[move[1][2], move[1][3]] = "{0}P".format(ww)
                        if "{0}P".format(ww) in chess_board_pieces["1"].values:
                            for letter in lower_alpha:
                                if chess_board_pieces.loc[letter, "1"] == "{0}P".format(ww):
                                    chess_board_pieces.loc[letter, "1"] = "B{}".format(move[1][-1])
                            move[1] = move[1][:len(move[1]) - 2]

    #### KING LOGIC ####  
                                
                if move[z][0] == "K" and "x" in move[z]:
                    for square1 in lower_alpha:
                        for square2 in numbers1:
                            if chess_board_pieces.loc[square1, square2] == "{0}K".format(ww):
                                chess_board_pieces.loc[square1, square2] = "E"
                    chess_board_pieces.iloc[dict2[move[z][2]], dict3[move[z][3]]] = "{0}K".format(ww)
                if move[z][0] == "K" and "x" not in move[z]:
                    for square1 in lower_alpha:
                        for square2 in numbers1:
                            if chess_board_pieces.loc[square1, square2] == "{0}K".format(ww):
                                chess_board_pieces.loc[square1, square2] = "E"
                    chess_board_pieces.iloc[dict2[move[z][1]], dict3[move[z][2]]] = "{0}K".format(ww)

    #### CASTLE LOGIC ####
                    
                if z == 0:
                    if move[z] == "O-O":
                        chess_board_pieces.loc["g", "1"] = "WK"
                        chess_board_pieces.loc["f", "1"] = "WR"
                        chess_board_pieces.loc["h", "1"] = "E"
                        chess_board_pieces.loc["e", "1"] = "E"
                    if move[z] == "O-O-O":
                        chess_board_pieces.loc["d", "1"] = "WR"
                        chess_board_pieces.loc["c", "1"] = "WK"
                        chess_board_pieces.loc["a", "1"] = "E"
                        chess_board_pieces.loc["b", "1"] = "E"
                        chess_board_pieces.loc["e", "1"] = "E"
                if z == 1:
                    if move[1] == "O-O":
                        chess_board_pieces.loc["g", "8"] = "BK"
                        chess_board_pieces.loc["f", "8"] = "BR"
                        chess_board_pieces.loc["h", "8"] = "E"
                        chess_board_pieces.loc["e", "8"] = "E"
                    if move[1] == "O-O-O":
                        chess_board_pieces.loc["d", "8"] = "BR"
                        chess_board_pieces.loc["c", "8"] = "BK"
                        chess_board_pieces.loc["a", "8"] = "E"
                        chess_board_pieces.loc["b", "8"] = "E"
                        chess_board_pieces.loc["e", "8"] = "E"

    #### FILES, DIAGONALS AND KNIGHT MOVE LOGIC
                    
                def file_row(row, column):
                    final_lst = []
                    for num in range(dict3[column], 8):
                        final_lst.append("{0}{1}".format(row, numbers1[num]))
                    for num in range(0, dict3[column]):
                        final_lst.append("{0}{1}".format(row, numbers1[num]))
                    final_lst.pop(0)
                    return final_lst
                
                def file_column(row, column):
                    final_lst = []
                    for num in range(dict2[row], 8):
                        final_lst.append("{0}{1}".format(lower_alpha[num], column))
                    for num in range(0, dict2[row]):
                        final_lst.append("{0}{1}".format(lower_alpha[num], column))
                    final_lst.pop(0)
                    return final_lst
                
                def top_row(row, column):
                    final_lst = []
                    for num in range(dict3[column], 8):
                        final_lst.append("{0}{1}".format(row, numbers1[num]))
                    final_lst.pop(0)
                    return final_lst
                
                def bottom_row(row, column):
                    final_lst = []
                    for num in range(dict3[column], 0, -1):
                        final_lst.append("{0}{1}".format(row, numbers1[num - 1]))
                    return final_lst

                def right_column(row, column):
                    final_lst = []
                    for num in range(dict2[row], 8):
                        final_lst.append("{0}{1}".format(lower_alpha[num], column))
                    final_lst.pop(0)
                    return final_lst
                
                def left_column(row, column):
                    final_lst = []
                    for num in range(dict2[row], 0, -1):
                        final_lst.append("{0}{1}".format(lower_alpha[num - 1], column))
                    return final_lst
                    
                def diag_top_right(row, column):
                    final_lst = []
                    temp_lst = []
                    if dict2[row] > dict3[column]:
                        for num in range(8 - dict2[row]):
                            if dict2[row] + num < 8 and dict3[column] + num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] + num], numbers1[dict3[column] + num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    if dict2[row] <= dict3[column]:
                        for num in range(8 - dict3[column]):
                            if dict2[row] + num < 8 and dict3[column] + num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] + num], numbers1[dict3[column] + num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    final_lst[0].pop(0)
                    return final_lst[0]
                
                def diag_top_left(row, column):
                    final_lst = []
                    temp_lst = []
                    if 8 - dict2[row] > dict3[column]:
                        for num in range(dict2[row] + 1):
                            if dict2[row] - num < 8 and dict3[column] + num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] - num], numbers1[dict3[column] + num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    if 8 - dict2[row] <= dict3[column]:
                        for num in range(8 - dict3[column]):
                            if dict2[row] - num < 8 and dict3[column] + num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] - num], numbers1[dict3[column] + num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    final_lst[0].pop(0)
                    return final_lst[0]
                
                def diag_bottom_right(row, column):
                    final_lst = []
                    temp_lst = []
                    if dict2[row] > 8 - dict3[column]:
                        for num in range(8 - dict2[row]):
                            if dict2[row] + num < 8 and dict3[column] - num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] + num], numbers1[dict3[column] - num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    if dict2[row] <= 8 - dict3[column]:
                        for num in range(dict3[column] + 1):
                            if dict2[row] + num < 8 and dict3[column] - num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] + num], numbers1[dict3[column] - num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    final_lst[0].pop(0)
                    return final_lst[0]
                
                def diag_bottom_left(row, column):
                    final_lst = []
                    temp_lst = []
                    if 8 - dict2[row] > 8 - dict3[column]:
                        for num in range(dict2[row] + 1):
                            if dict2[row] - num < 8 and dict3[column] - num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] - num], numbers1[dict3[column] - num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    if 8 - dict2[row] <= 8 - dict3[column]:
                        for num in range(dict3[column] + 1):
                            if dict2[row] - num < 8 and dict3[column] - num < 8:
                                temp_lst += ["{0}{1}".format(lower_alpha[dict2[row] - num], numbers1[dict3[column] - num])]
                        final_lst.append(temp_lst)
                        temp_lst = []
                    final_lst[0].pop(0)
                    return final_lst[0]

                def knight_moves(row, column):
                    move_lst = []
                    for x in range(-2, 3):
                        for y in range(-2, 3):
                            if abs(x) + abs(y) == 3 and x != 3 and y != 3 and 0 <= dict2[row] + x < 8 and 0 <= dict3[column] + y < 8:
                                move_lst.append("{0}{1}".format(lower_alpha[dict2[row] + x], numbers1[dict3[column] + y]))
                    return move_lst
                
    #### ROOK LOGIC ####
                
                rr = 0
                cr = 0
                topr = []
                bottomr = []
                rightc = []
                leftc = []
                if move[z][0] == "R" and "x" not in move[z] and len(move[z]) == 3:
                    rr = 1
                    cr = 2
                if move[z][0] == "R" and "x" in move[z] and len(move[z]) == 4:
                    rr = 2
                    cr = 3
                if (move[z][0] == "R" and "x" not in move[z] and len(move[z]) == 3) or (move[z][0] == "R" and "x" in move[z] and len(move[z]) == 4):
                    count = 0
                    holder = []
                    move_lst = []
                    for square in range(len(top_row(move[z][rr], move[z][cr]))):
                        move_lst.append(top_row(move[z][rr], move[z][cr])[square])
                        topr.append(top_row(move[z][rr], move[z][cr])[square])
                    for square in range(len(bottom_row(move[z][rr], move[z][cr]))):
                        move_lst.append(bottom_row(move[z][rr], move[z][cr])[square])
                        bottomr.append(bottom_row(move[z][rr], move[z][cr])[square])
                    for square in range(len(right_column(move[z][rr], move[z][cr]))):
                        move_lst.append(right_column(move[z][rr], move[z][cr])[square])
                        rightc.append(right_column(move[z][rr], move[z][cr])[square])
                    for square in range(len(left_column(move[z][rr], move[z][cr]))):
                        move_lst.append(left_column(move[z][rr], move[z][cr])[square])
                        leftc.append(left_column(move[z][rr], move[z][cr])[square])
                    for square in move_lst:
                        if chess_board_pieces.loc[square[0], square[1]] == "{0}R".format(ww):
                            count += 1
                            holder += [square]
                    if count == 1:
                        chess_board_pieces.loc[holder[0][0], holder[0][1]] = "E"
                        chess_board_pieces.loc[move[z][rr], move[z][cr]] = "{0}R".format(ww)  
                    else:
                        rook_piece = ""
                        for r in topr:
                            if chess_board_pieces.loc[r[0], r[1]] != "E" and chess_board_pieces.loc[r[0], r[1]] != "{0}R".format(ww):
                                break
                            elif chess_board_pieces.loc[r[0], r[1]] == "{0}R".format(ww):
                                rook_piece = r
                                break
                        for r in bottomr:
                            if chess_board_pieces.loc[r[0], r[1]] != "E" and chess_board_pieces.loc[r[0], r[1]] != "{0}R".format(ww):
                                break
                            elif chess_board_pieces.loc[r[0], r[1]] == "{0}R".format(ww):
                                rook_piece = r
                                break
                        for c in rightc:
                            if chess_board_pieces.loc[c[0], c[1]] != "E" and chess_board_pieces.loc[c[0], c[1]] != "{0}R".format(ww):
                                break
                            elif chess_board_pieces.loc[c[0], c[1]] == "{0}R".format(ww):
                                rook_piece = c
                                break
                        for c in leftc:
                            if chess_board_pieces.loc[c[0], c[1]] != "E" and chess_board_pieces.loc[c[0], c[1]] != "{0}R".format(ww):
                                break
                            elif chess_board_pieces.loc[c[0], c[1]] == "{0}R".format(ww):
                                rook_piece = c
                                break
                        chess_board_pieces.loc[rook_piece[0], rook_piece[1]] = "E"
                        chess_board_pieces.loc[move[z][rr], move[z][cr]] = "{0}R".format(ww)
                if move[z][0] == "R" and "x" not in move[z] and len(move[z]) == 4:
                    if move[z][1] in lower_alpha and move[z][2] in lower_alpha:
                        for value in numbers1:
                            if chess_board_pieces.loc[move[z][1], value] == "{0}R".format(ww):
                                chess_board_pieces.loc[move[z][1], value] = "E"
                        chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}R".format(ww)
                    if move[z][1] in numbers1 and move[z][3] in numbers1:
                        for value in lower_alpha:
                            if chess_board_pieces.loc[value, move[z][1]] == "{0}R".format(ww):
                                chess_board_pieces.loc[value, move[z][1]] = "E"
                        chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}R".format(ww)
                if move[z][0] == "R" and "x" in move[z] and len(move[z]) == 5:      
                    if move[z][1] in lower_alpha and move[z][3] in lower_alpha:
                        for value in numbers1:
                            if chess_board_pieces.loc[move[z][1], value] == "{0}R".format(ww):
                                chess_board_pieces.loc[move[z][1], value] = "E"
                        chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}R".format(ww)
                    if move[z][1] in numbers1 and move[z][4] in numbers1:
                        for value in lower_alpha:
                            if chess_board_pieces.loc[value, move[z][1]] == "{0}R".format(ww):
                                chess_board_pieces.loc[value, move[z][1]] = "E"
                        chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}R".format(ww)
                if move[z][0] == "R" and "x" not in move[z] and len(move[z]) == 5:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}R".format(ww)
                if move[z][0] == "R" and "x" in move[z] and len(move[z]) == 6:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][4], move[z][5]] = "{0}R".format(ww)
                
    #### BISHOP LOGIC ####
                    
                rb = 0
                cb = 0
                count1 = 0
                holder1 = []
                if move[z][0] == "B" and "x" not in move[z] and len(move[z]) == 3:
                    rb = 1
                    cb = 2
                if move[z][0] == "B" and "x" in move[z] and len(move[z]) == 4:
                    rb = 2
                    cb = 3
                if (move[z][0] == "B" and "x" not in move[z] and len(move[z]) == 3) or (move[z][0] == "B" and "x" in move[z] and len(move[z]) == 4):
                    move_lst = []
                    diag_topr_lst = []
                    diag_topl_lst = []
                    diag_bottomr_lst = []
                    diag_bottoml_lst = []
                    for square in range(len(diag_top_right(move[z][rb], move[z][cb]))):
                        move_lst.append(diag_top_right(move[z][rb], move[z][cb])[square])
                        diag_topr_lst.append(diag_top_right(move[z][rb], move[z][cb])[square])
                    for square in range(len(diag_top_left(move[z][rb], move[z][cb]))):
                        move_lst.append(diag_top_left(move[z][rb], move[z][cb])[square])
                        diag_topl_lst.append(diag_top_left(move[z][rb], move[z][cb])[square])
                    for square in range(len(diag_bottom_right(move[z][rb], move[z][cb]))):
                        move_lst.append(diag_bottom_right(move[z][rb], move[z][cb])[square])
                        diag_bottomr_lst.append(diag_bottom_right(move[z][rb], move[z][cb])[square])
                    for square in range(len(diag_bottom_left(move[z][rb], move[z][cb]))):
                        move_lst.append(diag_bottom_left(move[z][rb], move[z][cb])[square])
                        diag_bottoml_lst.append(diag_bottom_left(move[z][rb], move[z][cb])[square])
                    for square in move_lst:
                        if chess_board_pieces.loc[square[0], square[1]] == "{0}B".format(ww):
                            count1 += 1
                            holder1 += [square]
                    if count1 == 1:
                        chess_board_pieces.loc[holder1[0][0], holder1[0][1]] = "E"
                        chess_board_pieces.loc[move[z][rb], move[z][cb]] = "{0}B".format(ww)
                    else:
                        bishop_piece = ""
                        for topr in diag_topr_lst:
                            if chess_board_pieces.loc[topr[0], topr[1]] != "E" and chess_board_pieces.loc[topr[0], topr[1]] != "{0}B".format(ww):
                                break
                            elif chess_board_pieces.loc[topr[0], topr[1]] == "{0}B".format(ww):
                                bishop_piece = topr
                                break
                        for topl in diag_topl_lst:
                            if chess_board_pieces.loc[topl[0], topl[1]] != "E" and chess_board_pieces.loc[topl[0], topl[1]] != "{0}B".format(ww):
                                break
                            elif chess_board_pieces.loc[topl[0], topl[1]] == "{0}B".format(ww):
                                bishop_piece = topl
                                break
                        for br in diag_bottomr_lst:
                            if chess_board_pieces.loc[br[0], br[1]] != "E" and chess_board_pieces.loc[br[0], br[1]] != "{0}B".format(ww):
                                break
                            elif chess_board_pieces.loc[br[0], br[1]] == "{0}B".format(ww):
                                bishop_piece = br
                                break
                        for bl in diag_bottoml_lst:
                            if chess_board_pieces.loc[bl[0], bl[1]] != "E" and chess_board_pieces.loc[bl[0], bl[1]] != "{0}B".format(ww):
                                break
                            elif chess_board_pieces.loc[bl[0], bl[1]] == "{0}B".format(ww):
                                bishop_piece = bl
                                break
                        chess_board_pieces.loc[bishop_piece[0], bishop_piece[1]] = "E"
                        chess_board_pieces.loc[move[z][rb], move[z][cb]] = "{0}B".format(ww)
                if move[z][0] == "B" and "x" not in move[z] and len(move[z]) == 4:
                    if move[z][1] in lower_alpha and move[z][2] in lower_alpha:
                        for value in chess_board_pieces.loc[move[z][1]]:
                            if chess_board_pieces.loc[move[z][1], value] == "{0}B".format(ww):
                                chess_board_pieces.loc[move[z][1], value] = "E"
                        chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}B".format(ww)
                    if move[z][1] in numbers1 and move[z][3] in numbers1:
                        for value in chess_board_pieces.loc[:, move[z][1]]:
                            if chess_board_pieces.loc[value, move[z][1]] == "{0}B".format(ww):
                                chess_board_pieces.loc[value, move[z][1]] = "E"
                        chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}B".format(ww)
                if move[z][0] == "B" and "x" in move[z] and len(move[z]) == 5:      
                    if move[z][1] in lower_alpha and move[z][3] in lower_alpha:
                        for value in chess_board_pieces.loc[move[z][1]]:
                            if chess_board_pieces.loc[move[z][1], value] == "{0}B".format(ww):
                                chess_board_pieces.loc[move[z][1], value] = "E"
                        chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}B".format(ww)
                    if move[z][1] in numbers1 and move[z][4] in numbers1:
                        for value in chess_board_pieces.loc[:, move[z][1]]:
                            if chess_board_pieces.loc[value, move[z][1]] == "{0}B".format(ww):
                                chess_board_pieces.loc[value, move[z][1]] = "E"
                        chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}B".format(ww)
                if move[z][0] == "B" and "x" not in move[z] and len(move[z]) == 5:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}B".format(ww)
                if move[z][0] == "B" and "x" in move[z] and len(move[z]) == 6:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][4], move[z][5]] = "{0}B".format(ww)

    #### QUEEN LOGIC ####

                move_lst1 = []
                rq = 0
                cq = 0
                if move[z][0] == "Q" and "x" not in move[z] and len(move[z]) == 3:
                    rq = 1
                    cq = 2
                if move[z][0] == "Q" and "x" in move[z] and len(move[z]) == 4:
                    rq = 2
                    cq = 3
                if (move[z][0] == "Q" and "x" not in move[z] and len(move[z]) == 3) or (move[z][0] == "Q" and "x" in move[z] and len(move[z]) == 4):
                    move_lst = []
                    diag_topr_lst = []
                    diag_topl_lst = []
                    diag_bottomr_lst = []
                    diag_bottoml_lst = []
                    row_lst = []
                    column_lst = []
                    row_lstt = []
                    row_lstb = []
                    column_lstl = []
                    column_lstr = []
                    for square in range(len(diag_top_right(move[z][rq], move[z][cq]))):
                        move_lst.append(diag_top_right(move[z][rq], move[z][cq])[square])
                        diag_topr_lst.append(diag_top_right(move[z][rq], move[z][cq])[square])
                    for square in range(len(diag_top_left(move[z][rq], move[z][cq]))):
                        move_lst.append(diag_top_left(move[z][rq], move[z][cq])[square])
                        diag_topl_lst.append(diag_top_left(move[z][rq], move[z][cq])[square])
                    for square in range(len(diag_bottom_right(move[z][rq], move[z][cq]))):
                        move_lst.append(diag_bottom_right(move[z][rq], move[z][cq])[square])
                        diag_bottomr_lst.append(diag_bottom_right(move[z][rq], move[z][cq])[square])
                    for square in range(len(diag_bottom_left(move[z][rq], move[z][cq]))):
                        move_lst.append(diag_bottom_left(move[z][rq], move[z][cq])[square])
                        diag_bottoml_lst.append(diag_bottom_left(move[z][rq], move[z][cq])[square])
                    for square in range(len(file_row(move[z][rq], move[z][cq]))):
                        move_lst.append(file_row(move[z][rq], move[z][cq])[square])
                        row_lst.append(file_row(move[z][rq], move[z][cq])[square])
                    for square in range(len(file_column(move[z][rq], move[z][cq]))):
                        move_lst.append(file_column(move[z][rq], move[z][cq])[square])
                        column_lst.append(file_column(move[z][rq], move[z][cq])[square])
                    for square in range(len(top_row(move[z][rq], move[z][cq]))):
                        row_lstt.append(top_row(move[z][rq], move[z][cq])[square])
                    for square in range(len(bottom_row(move[z][rq], move[z][cq]))):
                        row_lstb.append(bottom_row(move[z][rq], move[z][cq])[square])
                    for square in range(len(right_column(move[z][rq], move[z][cq]))):
                        column_lstr.append(right_column(move[z][rq], move[z][cq])[square])
                    for square in range(len(left_column(move[z][rq], move[z][cq]))):
                        column_lstl.append(left_column(move[z][rq], move[z][cq])[square])
                    move_lst1 = move_lst[::]
                    for square in move_lst:
                        if chess_board_pieces.loc[square[0], square[1]] == "{0}Q".format(ww):
                            count1 += 1
                            holder1 += [square]
                    if count1 == 1:
                        chess_board_pieces.loc[holder1[0][0], holder1[0][1]] = "E"
                        chess_board_pieces.loc[move[z][rq], move[z][cq]] = "{0}Q".format(ww)
                    else:
                        queen_piece = ""
                        for topr in diag_topr_lst:
                            if chess_board_pieces.loc[topr[0], topr[1]] != "E" and chess_board_pieces.loc[topr[0], topr[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[topr[0], topr[1]] == "{0}Q".format(ww):
                                queen_piece = topr
                                break
                        for topl in diag_topl_lst:
                            if chess_board_pieces.loc[topl[0], topl[1]] != "E" and chess_board_pieces.loc[topl[0], topl[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[topl[0], topl[1]] == "{0}Q".format(ww):
                                queen_piece = topl
                                break
                        for br in diag_bottomr_lst:
                            if chess_board_pieces.loc[br[0], br[1]] != "E" and chess_board_pieces.loc[br[0], br[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[br[0], br[1]] == "{0}Q".format(ww):
                                queen_piece = br
                                break
                        for bl in diag_bottoml_lst:
                            if chess_board_pieces.loc[bl[0], bl[1]] != "E" and chess_board_pieces.loc[bl[0], bl[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[bl[0], bl[1]] == "{0}Q".format(ww):
                                queen_piece = bl
                                break
                        for r in row_lstt:
                            if chess_board_pieces.loc[r[0], r[1]] != "E" and chess_board_pieces.loc[r[0], r[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[r[0], r[1]] == "{0}Q".format(ww):
                                queen_piece = r
                                break
                        for r in row_lstb:
                            if chess_board_pieces.loc[r[0], r[1]] != "E" and chess_board_pieces.loc[r[0], r[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[r[0], r[1]] == "{0}Q".format(ww):
                                queen_piece = r
                                break
                        for c in column_lstr:
                            if chess_board_pieces.loc[c[0], c[1]] != "E" and chess_board_pieces.loc[c[0], c[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[c[0], c[1]] == "{0}Q".format(ww):
                                queen_piece = c
                                break
                        for c in column_lstl:
                            if chess_board_pieces.loc[c[0], c[1]] != "E" and chess_board_pieces.loc[c[0], c[1]] != "{0}Q".format(ww):
                                break
                            elif chess_board_pieces.loc[c[0], c[1]] == "{0}Q".format(ww):
                                queen_piece = c
                                break
                        chess_board_pieces.loc[queen_piece[0], queen_piece[1]] = "E"
                        chess_board_pieces.loc[move[z][rq], move[z][cq]] = "{0}Q".format(ww)
                if move[z][0] == "Q" and "x" not in move[z] and len(move[z]) == 4:
                    if move[z][1] in lower_alpha and move[z][2] in lower_alpha:
                        for square in move_lst1:
                            if square[0] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}Q".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}Q".format(ww)
                    if move[z][1] in numbers1 and move[z][3] in numbers1:
                        for square in move_lst1:
                            if square[1] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}Q".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}Q".format(ww)
                if move[z][0] == "Q" and "x" in move[z] and len(move[z]) == 5:
                    if move[z][1] in lower_alpha and move[z][3] in lower_alpha:
                        for square in move_lst1:
                            if square[0] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}Q".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}Q".format(ww)
                    if move[z][1] in numbers1 and move[z][4] in numbers1:
                        for square in move_lst1:
                            if square[1] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}Q".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}Q".format(ww)
                if move[z][0] == "Q" and "x" not in move[z] and len(move[z]) == 5:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}Q".format(ww)
                if move[z][0] == "Q" and "x" in move[z] and len(move[z]) == 6:
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][4], move[z][5]] = "{0}Q".format(ww)

    #### KNIGHT LOGIC ####
                    
                rn = 0
                cn = 0
                if move[z][0] == "N" and "x" not in move[z] and len(move[z]) == 3:
                    rn = 1
                    cn = 2
                if move[z][0] == "N" and "x" in move[z] and len(move[z]) == 4: 
                    rn = 2
                    cn = 3
                if (move[z][0] == "N" and "x" not in move[z] and len(move[z]) == 3) or (move[z][0] == "N" and "x" in move[z] and len(move[z]) == 4):
                    move_lst = knight_moves(move[z][rn], move[z][cn])
                    count = 0
                    holder = []
                    for square in move_lst:
                        if chess_board_pieces.loc[square[0], square[1]] == "{0}N".format(ww):
                            count += 1  
                            holder += [square]
                    if count == 1:
                        chess_board_pieces.loc[holder[0][0], holder[0][1]] = "E"
                        chess_board_pieces.loc[move[z][rn], move[z][cn]] = "{0}N".format(ww)
                if move[z][0] == "N" and "x" not in move[z] and len(move[z]) == 4:
                    move_lst = knight_moves(move[z][2], move[z][3])
                    if move[z][1] in lower_alpha and move[z][2] in lower_alpha:
                        for square in move_lst:
                            if square[0] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}N".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}N".format(ww)
                    if move[z][1] in numbers1 and move[z][3] in numbers1:
                        for square in move_lst:
                            if square[1] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}N".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][2], move[z][3]] = "{0}N".format(ww)
                if move[z][0] == "N" and "x" in move[z] and len(move[z]) == 5:
                    move_lst = knight_moves(move[z][3], move[z][4])
                    if move[z][1] in lower_alpha and move[z][3] in lower_alpha:
                        for square in move_lst:
                            if square[0] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}N".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}N".format(ww)
                    if move[z][1] in numbers1 and move[z][4] in numbers1:
                        for square in move_lst:
                            if square[1] == move[z][1] and chess_board_pieces.loc[square[0], square[1]] == "{0}N".format(ww):
                                chess_board_pieces.loc[square[0], square[1]] = "E"
                                chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}N".format(ww)
                if move[z][0] == "N" and "x" not in move[z] and len(move[z]) == 5:
                    move_lst = knight_moves(move[z][3], move[z][4])
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][3], move[z][4]] = "{0}N".format(ww)
                if move[z][0] == "N" and "x" in move[z] and len(move[z]) == 6:
                    move_lst = knight_moves(move[z][4], move[z][5])
                    chess_board_pieces.loc[move[z][1], move[z][2]] = "E"
                    chess_board_pieces.loc[move[z][4], move[z][5]] = "{0}N".format(ww)
                pieces = [ww]
                for row in lower_alpha:
                    for column in numbers1:
                        pieces.append(chess_board_pieces.loc[row, column])
                if checkw_bool and ww == "W":
                    pieces.append("+")
                if checkb_bool and ww == "B":
                    pieces.append("+")
                if matew_bool and ww == "W":
                    pieces.append("#")
                if mateb_bool and ww == "B":
                    pieces.append("#")
                if "0" in move:
                    pieces.append("0-1")
                if "1" in move:
                    pieces.append("1-0")
                if "1/2-1" in move:
                    pieces.append("1/2-1/2")
                final_pieces.append(pieces)
                if ww == "B":
                    print(n, move)
                    print(chess_board_pieces)
    with open("chess_array.csv", "w", newline = '') as holder:
        sender = csv.writer(holder, delimiter=",", lineterminator="\n")
        sender.writerows(final_pieces)        


