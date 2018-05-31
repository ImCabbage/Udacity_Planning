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

def search():
	# closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	closed = np.zeros((len(grid), len(grid[0])), dtype=float)
	expand = (-1)*np.ones((len(grid), len(grid[0])), dtype=float)
	action = (-1)* np.ones((len(grid), len(grid[0])), dtype=float)


	closed[init[0]][init[1]] = 1
	expand[init[0]][init[1]] = 0
	cnt = 1

	x = init[0]
	y = init[1]
	g = 0

	open_list = [[g, x, y]]

	found = False
	resign = False

	while found is False and resign is False:

		if len(open_list) == 0:
			resign = True
			print 'fail'
		else:
			open_list.sort()
			open_list.reverse()
			next_ = open_list.pop()
			x = next_[1]
			y = next_[2]
			g = next_[0]

			if x == goal[0] and y == goal[1]:
				found = True
				print next_
			else:
				for i in range(len(delta)):
					x2 = x + delta[i][0]
					y2 = y + delta[i][1]
					if x2  >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
						if closed[x2][y2] == 0 and grid[x2][y2] == 0:
							g2 = g + cost
							open_list.append([g2, x2, y2])
							closed[x2][y2] = 1
							expand[x2][y2] = cnt
							action[x2][y2] = i
							cnt += 1
	print expand
	print action











search()
