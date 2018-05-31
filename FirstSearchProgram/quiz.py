#! /usr/bin/env python

import numpy as np

# 0 = Navigable space
# 1 = Occupied space 
grid = [[0, 0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 1, 1, 1, 0],
		[0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1,len(grid[0])-1]
cost = 1

delta = [[-1, 0],   # go up
		 [0, -1],   # go left
		 [1, 0],	# go down
		 [0, 1]]    # go right

delta_name = ['^', '<', 'V', '>']

def search(grid, init, goal, cost):
	# initialization
	close_list = []
	close_list.append(init)

	# generate heuristic matrix
	H = np.zeros((len(grid), len(grid[0])), dtype=float)
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			H[i,j] = (goal[0] - i) + (goal[1] - j)

	while (close_list[-1] != goal):
		# check available points
		open_list = []
		for i in range(4):
			# get the coordinates of the potential waypoints
			tmp_point = [close_list[-1][0] + delta[i][0], close_list[-1][1] + delta[i][1]]
			# Step #1: check all the potential waypoints which are in the maze
			if ((tmp_point[0] >= 0) and (tmp_point[1] >= 0)):
				# Step #2: check all the potential waypoints which are not in the close list
				for j in range(len(close_list)):
					if ((tmp_point[0] != close_list[j][0]) and (tmp_point[1] != close_list[j][1])):
						open_list.append(tmp_point)
		

		open_list.append(tmp_point)

		# select the optimal waypoint
		F = 999
		index = 999
		for i in range(len(open_list)):
			tmp_point = open_list[i];
			tmp_F = cost + H[tmp_point[0], tmp_point[1]]
			if tmp_F < F:
				F = tmp_F
				index = i
		
		# add the waypoint to list 
		close_list.append(open_list[index])

		# print close_list
		# print "\n"








if __name__ == '__main__':
	search(grid, init, goal, cost)