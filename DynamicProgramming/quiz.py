#! /usr/bin/env python

import numpy as np

# 0 = Navigable space
# 1 = Occupied space 
grid = [[0, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 0, 0],
	[0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 1, 0],
	[0, 0, 1, 1, 1, 0],
	[0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

cost_step = 1

delta = [[-1, 0],   # go up
	 [0, -1],   # go left
	 [1, 0],	  # go down
	 [0, 1]]    # go right

delta_name = ['^', '<', 'V', '>']

value = 99*np.ones((len(grid), len(grid[0])),dtype=int)
policy = [[' ' for row in range(len(grid))] for col in range(len(grid[0]))]

change = True

while change:
	change = False

	for x in range(len(grid)):
		for y in range(len(grid[0])):

			if x == goal[0] and y == goal[1]:
				if value[x][y] > 0:
					value[x][y] = 0
					policy[x][y] = '*'
					change = True
			elif grid[x][y] == 0:
				for a in range(len(delta)):
					x2 = x + delta[a][0]
					y2 = y + delta[a][1]

					if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
						v2 = value[x2][y2] + cost_step

						if v2 < value[x][y]:
							change = True
							value[x][y] = v2 
							policy[x][y] = delta_name[a]

for i in range(len(grid)):
	print policy[i]
	print '\n'