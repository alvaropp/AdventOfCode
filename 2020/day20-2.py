# Abusing deepcopy so it takes a couple of minutes to run

from copy import deepcopy
from itertools import product
import numpy as np


class Image:
    def __init__(self, image_id, image):
        self.id = image_id
        self.image = image

        rotation_list = [
            lambda x: x,
            lambda x: np.rot90(x, 1),
            lambda x: np.rot90(x, 2),
            lambda x: np.rot90(x, 3),
        ]
        flip_list = [lambda x: x, lambda x: np.fliplr(x)]

        self.permutations = list(product(rotation_list, flip_list))
        self.perm_idx = 0

    def permute(self, idx):
        fcns = self.permutations[idx]
        return fcns[0](fcns[1](deepcopy(self.image)))

    def accept_bottom(self, new_image):
        return list(self.permute(self.perm_idx)[-1, :]) == list(new_image[0, :])

    def accept_right(self, new_image):
        return list(self.permute(self.perm_idx)[:, -1]) == list(new_image[:, 0])


def solve(state, available_images):
    next_tile_coords = list(zip(*np.where(state == None)))[0]

    new_states_to_check = []
    for i, image in enumerate(available_images):
        for perm_idx in range(len(image.permutations)):

            top_ok = bool(
                next_tile_coords[0] <= 0
                or (
                    state[next_tile_coords[0] - 1, next_tile_coords[1]].accept_bottom(
                        image.permute(perm_idx)
                    )
                )
            )

            left_ok = bool(
                next_tile_coords[1] <= 0
                or (
                    state[next_tile_coords[0], next_tile_coords[1] - 1].accept_right(
                        image.permute(perm_idx)
                    )
                )
            )

            if top_ok and left_ok:
                _image = deepcopy(image)
                _image.perm_idx = perm_idx
                _images = deepcopy(available_images)
                _state = deepcopy(state)

                _ = _images.pop(i)
                _state[next_tile_coords[0], next_tile_coords[1]] = _image
                new_states_to_check.append((_state, _images))

    return new_states_to_check


def find_sea_monsters(image):
    n_sea_monsters = 0
    for r in range(len(image) - rows_sea_monster):
        for c in range(len(image[0]) - cols_sea_monster):
            found = not any(
                any(image[r + i][c + idx] != "#" for idx in indices)
                for i, indices in enumerate(sea_monster)
            )
            if found:
                n_sea_monsters += 1
    return n_sea_monsters


with open("day20.txt", "r") as f:
    data = f.read().strip()

all_images = []
for tile in data.split("\n\n"):
    tile_id = int(tile.split(":\n")[0].split(" ")[1])
    tile = np.array([list(line) for line in tile.split(":\n")[-1].split("\n")])
    all_images.append(Image(tile_id, tile))

square_side = int(np.sqrt(len(all_images)))
empty_state = np.full((square_side, square_side), None)
states_to_check = []
for i, image in enumerate(all_images):
    for perm_idx in range(len(image.permutations)):
        _image = deepcopy(image)
        _image.perm_idx = perm_idx
        _images = deepcopy(all_images)
        _new_state = deepcopy(empty_state)
        _new_state[0, 0] = _image
        _ = _images.pop(i)
        states_to_check.append((_new_state, _images))

found = False
while not found:
    state, available_images = states_to_check.pop()
    new_states_to_check = solve(state, available_images)

    for state, avail_images in new_states_to_check:
        if len(avail_images) == 0:
            found = True
            final = deepcopy(state)

    states_to_check.extend(new_states_to_check)


sea_monster = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]
rows_sea_monster = 3
cols_sea_monster = 20


image = []
for i in range(square_side):
    image_row = [
        final[i, j].permute(final[i, j].perm_idx)[1:-1, 1:-1]
        for j in range(square_side)
    ]

    image.append(image_row)

full_image = [np.concatenate(image[i], axis=1) for i in range(square_side)]
full_image = np.concatenate(full_image, axis=0)

total_n_hashes = (full_image == "#").sum()
full_image = Image(0, full_image)
n_hashes_in_sea_monster = 15
min_n_hashes = float("inf")
for perm_idx in range(len(full_image.permutations)):
    image = deepcopy(full_image.permute(perm_idx))
    image = ["".join(list(line)) for line in image]

    remaining_hashes = total_n_hashes - find_sea_monsters(image) * 15
    if remaining_hashes < min_n_hashes:
        min_n_hashes = remaining_hashes

print(min_n_hashes)
