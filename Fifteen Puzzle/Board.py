import copy
import math

class Board:
    def __init__(self, list, last_move = '', depth=0):
        self.list = list
        self.depth = depth
        if last_move == '':
            self.last_move = []
            self.last_move.append(' ')
        else:
            self.last_move = last_move

    def next_move(self, move):
        if move == 'U' and self.last_move[-1] == 'D' or move == 'D' and self.last_move[-1] == 'U' or move == 'L' and self.last_move[-1] == 'R' or move == 'R' and self.last_move[-1] == 'L':
            return
        
        zero_position = self.search(0)

        list_copy = copy.deepcopy(self.list)
        moves_copy = copy.deepcopy(self.last_move)

        #self.print_board(list_copy)
        
        if move == 'U':
            if zero_position[0] != 0:
                list_copy[zero_position[0]][zero_position[1]] = list_copy[zero_position[0]-1][zero_position[1]]
                list_copy[zero_position[0]-1][zero_position[1]] = 0

                #self.print_board(list_copy)
                moves_copy.append(move)

                return(Board(list_copy,moves_copy,self.depth+1))
        
        if move == 'D':
            if zero_position[0] != 3:
                list_copy[zero_position[0]][zero_position[1]] = list_copy[zero_position[0]+1][zero_position[1]]
                list_copy[zero_position[0]+1][zero_position[1]] = 0

                #self.print_board(list_copy)
                moves_copy.append(move)

                return(Board(list_copy,moves_copy,self.depth+1))
            
        if move == 'L':
            if zero_position[1] != 0:
                list_copy[zero_position[0]][zero_position[1]] = list_copy[zero_position[0]][zero_position[1]-1]
                list_copy[zero_position[0]][zero_position[1]-1] = 0

                #self.print_board(list_copy)
                moves_copy.append(move)

                return(Board(list_copy,moves_copy,self.depth+1))
            
        if move == 'R':
            if zero_position[1] != 3:
                list_copy[zero_position[0]][zero_position[1]] = list_copy[zero_position[0]][zero_position[1]+1]
                list_copy[zero_position[0]][zero_position[1]+1] = 0

                #self.print_board(list_copy)
                moves_copy.append(move)

                return(Board(list_copy,moves_copy,self.depth+1))
            
    def hamm_coutning(self):
        i = 1
        count = 0
        for x in range(len(self.list)):
            for y in range(len(self.list[x])):
                if self.list[x][y] != i:
                    count += 1
                i += 1
                if i == 16:
                    i = 0
        return count
    
    def distance_sum(self):
        i = 1
        distance = 0
        for x in range(len(self.list)):
            for y in range(len(self.list[x])):
                searched_position = self.search(i)
                distance += math.sqrt((searched_position[0] - x)**2 + (searched_position[1] - y)**2)

                i += 1
                if i == 16:
                    i = 0
        return distance

            
    def print_board(self):
        print("Depth: " + str(self.depth) + " ,moves: " )
        print(*self.last_move)
        print(*self.list)

    def search(self, i):
        # printing the list using loop
        for x in range(len(self.list)):
            for y in range(len(self.list[x])):
                if self.list[x][y] == i:
                    return [x,y]

    def is_solved(self):
        return self.list == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
