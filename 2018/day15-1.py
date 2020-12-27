# %%
import heapq
from dataclasses import dataclass, field

# %%
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# %%
@dataclass
class Player:
    pos: tuple
    race: str
    hit_points: int = 200
    attack_power: int = 3
    adjacent: list = field(default_factory=list)

    def compute_adjacent(self, maze):
        adjacent = []
        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neigh = (self.pos[0] + move[0], self.pos[1] + move[1])
            if (
                (0 <= neigh[0] <= maze.n_rows)
                and (0 <= neigh[1] <= maze.n_cols)
                and (maze.maze[neigh[0]][neigh[1]] != "#")
            ):
                adjacent.append(neigh)
        self.adjacent = adjacent

    def action(self, maze):
        for player in maze.all_players:
            player.compute_adjacent(maze)

        enemies = maze.elves if self.race == "G" else maze.goblins
        enemies_in_range = sorted(
            [enemy for enemy in enemies if self.pos in enemy.adjacent],
            key=lambda enemy: (enemy.hit_points, enemy.pos),
        )
        if enemies_in_range:
            self.attack(enemies_in_range[0], maze)
        else:
            self.move(maze)

    def attack(self, enemy, maze):
        enemy.hit_points -= self.attack_power
        if enemy.hit_points == 0:
            if enemy.race == "G":
                maze.goblins.pop(enemy)
            else:
                maze.elves.pop(enemy)
            maze.all_players.pop(enemy)

    def move(self, maze):
        enemies = maze.elves if self.race == "G" else maze.goblins
        pos_in_range = [
            [pos, idx] for idx, enemy in enumerate(enemies) for pos in enemy.adjacent
        ]
        paths = [
            maze.a_star_search(self.pos, destination[0]) for destination in pos_in_range
        ]
        distances = [path[1].get(tuple(pos[0]), float("Inf")) for pos, path in zip(pos_in_range, paths)]
        idx = [i for i, dist in enumerate(distances) if dist == min(distances)]
        closest_pos = sorted(
            [(i, pos) for i, pos in enumerate(pos_in_range) if i in idx],
            key=lambda pos: pos[1][0],
        )
        chosen_idx = closest_pos[0][0]
        maze.maze[self.pos[0]][self.pos[1]] = "."
        self.pos = maze.first_step_in_path(
            paths[chosen_idx][0], self.pos, tuple(closest_pos[0][1][0])
        )
        maze.maze[self.pos[0]][self.pos[1]] = self.race


@dataclass
class Maze:
    maze: list
    elves: list = field(default_factory=list)
    goblins: list = field(default_factory=list)
    all_players: list = field(default_factory=list)

    def __post_init__(self):
        self.n_rows = len(self.maze)
        self.n_cols = len(self.maze[0])

        elf_pos = []
        goblin_pos = []
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.maze[r][c] == "E":
                    elf_pos.append((r, c))
                elif self.maze[r][c] == "G":
                    goblin_pos.append((r, c))

        self.elves = [Player(pos, "E") for pos in elf_pos]
        self.goblins = [Player(pos, "G") for pos in goblin_pos]
        self.all_players = sorted(
            self.elves + self.goblins, key=lambda player: player.pos
        )

    def __repr__(self):
        return "\n".join("".join(line) for line in self.maze)

    def sort_players(self):
        pass

    def compute_adjacent(self, pos):
        adjacent = []
        for move in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neigh = (pos[0] + move[0], pos[1] + move[1])
            if (
                (0 <= neigh[0] <= self.n_rows)
                and (0 <= neigh[1] <= self.n_cols)
                and (self.maze[neigh[0]][neigh[1]] == ".")
            ):
                adjacent.append(neigh)
        return adjacent

    @staticmethod
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def first_step_in_path(came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        return path[-1]

    def a_star_search(self, start, goal):
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

            for next in self.compute_adjacent(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(next, goal)
                    frontier.put(next, priority)
                    came_from[next] = current

        return came_from, cost_so_far


with open("test.txt", "r") as f:
    data = [list(line) for line in f.read().splitlines()]

maze = Maze(data)

n_rounds = 3
for _ in range(n_rounds):
    print(maze)
    print()

    maze.sort_players()

    for i, player in enumerate(maze.all_players):
        player.action(maze)

print(maze)

# %%
