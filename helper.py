import numpy as np

def to_grid_values(x, y, min_x, min_y, resolution):
    return np.floor((x - min_x) / resolution).astype(int), np.floor((y - min_y) / resolution).astype(int)

def is_free(grid, x, y):
    if not is_in_grid_limit(grid, x, y) or grid[y, x] == 1:
        return False
    return True

def is_in_grid_limit(grid, x, y):
    if x < 0 or x >= grid.shape[1]:
        return False
    if y < 0 or y >= grid.shape[0]:
        return False
    return True

def generate_neighbours(grid, x, y):
    points = []
    if is_free(grid, x, y-1):
        points.append((x, y-1))

    if is_free(grid, x, y+1):
        points.append((x, y+1))

    if is_free(grid, x-1, y):
        points.append((x-1, y))

    if is_free(grid, x+1, y):
        points.append((x+1, y))
    return points



def bfs(grid, start, goal):
    queue = [start]
    visited = [start]
    came_from = {}

    while queue:

        current = queue.pop(0)

        if goal == current:
            return visited, came_from

        neighbours = generate_neighbours(grid, current[0], current[1])

        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                came_from[neighbour] = current


    return visited, came_from


def reconstruct_path(came_from, start, goal):
    
    current = goal
    road = [current]
    if current not in came_from:
        raise Exception("Ni ma drogi kierowniku")
    while start not in road:
        current = came_from[current]
        road.append(current)

    road.reverse()
    return road

def grid_display(grid, start, goal_grid, path):
    display = np.full(grid.shape, ".", dtype="<U1")

    display[grid == 1] = "#"
    display[start[1], start[0]] = "S"
    display[goal_grid[1], goal_grid[0]] = "G"

    for x, y in path:
        if (x, y) != start and (x, y) != goal_grid:
            display[y, x] = "*"

    print("\nMapa:")
    for row in display:
        print(" ".join(row))

    print("\nTrasa:")

    route = " -> ".join(
        f"[{x}, {y}]"
        for x, y in path
    )

    print(route)


