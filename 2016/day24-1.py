# %%
import heapq


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


# %%
with open("test.txt", "r") as f:
    maze = Maze([list(line) for line in f.read().splitlines()])

# %%

a_star_search(maze, (1, 1), (1, 9))
# %%
