# %%
from copy import deepcopy
from itertools import product
import numpy as np

# %%
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
        return fcns[0](fcns[1](self.image))

    def accept_bottom(self, new_image):
        return list(self.permute(self.perm_idx)[-1, :]) == list(new_image[0, :])

    def accept_right(self, new_image):
        return list(self.permute(self.perm_idx)[:, -1]) == list(new_image[:, 0])


# %%
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


with open("test.txt", "r") as f:
    data = f.read().strip()

all_images = []
for tile in data.split("\n\n"):
    tile_id = int(tile.split(":\n")[0].split(" ")[1])
    tile = np.array([list(line) for line in tile.split(":\n")[-1].split("\n")])
    all_images.append(Image(tile_id, tile))


empty_state = np.full((3, 3), None)

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

matrix = ""
for i in range(3):
    for j in range(3):
        matrix += str(final[i][j].id)
        matrix += " "
    matrix += "\n"
print(matrix)
# %%
