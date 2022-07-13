from queue import Queue
from collections import deque


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != 1


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path

def bfs(maze, start, goal):
    queue = deque()
    queue.append(start)
    predecessors = {start: None}

    while not queue:
        current_cell = queue.append()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.append(neighbour)
                predecessors[neighbour] = current_cell
    return None

if __name__ == "__main__":

    maze = [[0] * 10 for row in range(10)]

    #obstacles

    maze[7][7] =1
    maze[8][7] =1
    maze[9][7] =1
    maze[7][8] =1

    offsets = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0)


    }

    start_pos = (0, 0)
    goal_pos = (9, 9)

    result = bfs(maze, start_pos, goal_pos)