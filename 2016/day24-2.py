# This website is absolutely genius for learning graph algorithms:
# https://www.redblobgames.com/pathfinding/a-star/introduction.html

import heapq
from itertools import permutations
from functools import lru_cache


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n_rows = len(maze)
        self.n_cols = len(maze[0])

        self.find_key_points()

    def find_key_points(self):
        self.keypoints = {}
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.maze[i][j] == "0":
                    self.start = (i, j)
                    self.keypoints[self.maze[i][j]] = (i, j)
                elif self.maze[i][j].isdigit():
                    self.keypoints[self.maze[i][j]] = (i, j)

    def find_neighbours(self, pos):
        neighs = []
        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neigh = (pos[0] + move[0], pos[1] + move[1])
            if (
                0 <= neigh[0] <= self.n_rows
                and 0 <= neigh[1] <= self.n_cols
                and self.maze[neigh[0]][neigh[1]] != "#"
            ):
                neighs.append(neigh)
        return neighs


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


@lru_cache
def a_star_search(maze, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in maze.find_neighbours(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def estimate_steps(keypoint_order, maze):
    estimated_steps = 0
    current_pos = maze.start
    for keypoint_idx in keypoint_order:
        next_pos = maze.keypoints[keypoint_idx]
        estimated_steps += heuristic(current_pos, next_pos)
        current_pos = next_pos
    return estimated_steps


def solve(maze, keypoint_order, max_steps=float("Inf")):
    current_pos = maze.start
    total_steps = 0
    for keypoint_idx in keypoint_order:
        goal = maze.keypoints[keypoint_idx]
        _, cost_so_far = a_star_search(maze, current_pos, goal)
        total_steps += cost_so_far[goal]
        if total_steps > max_steps:
            return float("Inf")
        current_pos = goal
    return total_steps


with open("day24.txt", "r") as f:
    maze = Maze([list(line) for line in f.read().splitlines()])
keypoint_orders = list(permutations([k for k in maze.keypoints.keys() if k != "0"]))
priority_keypoint_orders = PriorityQueue()
for keypoint_order in keypoint_orders:
    priority_keypoint_orders.put(
        keypoint_order + tuple("0"), estimate_steps(keypoint_order, maze)
    )

min_number_steps = float("Inf")
best_path = None

for _ in range(len(keypoint_orders)):
    keypoint_order = priority_keypoint_orders.get()
    steps = solve(maze, keypoint_order, min_number_steps)
    if steps < min_number_steps:
        min_number_steps = steps
        best_path = keypoint_order

print("\n", min_number_steps)
