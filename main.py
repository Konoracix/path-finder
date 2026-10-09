import numpy as np
from helper import to_grid_values, bfs, reconstruct_path, grid_display

points = np.array([
    [1, 1, 0.2],
    [2, 1, 0.3],
    [3, 1, 0.2],
    [4, 1, 1.5],

    [1, 2, 0.2],
    [2, 2, 0.4],
    [3, 2, 1.2],
    [4, 2, 0.3],

    [1, 3, 0.3],
    [2, 3, 0.2],
    [3, 3, 0.3],
    [4, 3, 2.0]
])



ground_height = 0.3

robot = np.array([1, 1])

goal = np.array([4, 2])

z = points[:, 2]

height_above_ground = z - ground_height

obstacles_mask = height_above_ground > 0.5

obstacles = points[obstacles_mask]


obstacles_xy = obstacles[:, 0:2]

obstacles_x = obstacles_xy[:, 0]
obstacles_y = obstacles_xy[:, 1]

resolution = 1
min_x = 1
min_y = 1

grid_x, grid_y = to_grid_values(obstacles_x, obstacles_y, min_x, min_y, resolution)

grid_robot_x, grid_robot_y = to_grid_values(robot[0], robot[1], min_x, min_y, resolution)

grid_goal_x, grid_goal_y = to_grid_values(goal[0], goal[1], min_x, min_y, resolution)

grid = np.zeros((5, 5), dtype=int)

grid[grid_y, grid_x] = 1

# grid[1, 4] = 1

grid[grid_robot_y, grid_robot_x] = 2
grid[grid_goal_y, grid_goal_x] = 3

start = (grid_robot_x, grid_robot_y)
goal_grid = (grid_goal_x, grid_goal_y)

visited, came_from = bfs(grid, start, goal_grid)

path = reconstruct_path(came_from, start, goal_grid)

grid_display(grid, start, goal_grid, path)