from dataclasses import dataclass, field
import numpy as np


@dataclass
class Image:
    id: int
    image: np.ndarray
    neighbours: set = field(default_factory=set)

    def __post_init__(self):
        self.borders = [
            list(self.image[0, :]),
            list(self.image[-1, :]),
            list(self.image[:, 0]),
            list(self.image[:, -1]),
        ]


with open("day20.txt", "r") as f:
    data = f.read().strip()

images = []
for tile in data.split("\n\n"):
    tile_id = int(tile.split(":\n")[0].split(" ")[1])
    tile = np.array([list(line) for line in tile.split(":\n")[-1].split("\n")])
    images.append(Image(tile_id, tile))


for i, image_1 in enumerate(images):
    for image_2 in images[i + 1 :]:
        if any(
            border
            for border in image_1.borders
            if border in image_2.borders or border[::-1] in image_2.borders
        ):
            image_1.neighbours.add(image_2.id)
            image_2.neighbours.add(image_1.id)


print(np.prod([image.id for image in images if len(image.neighbours) == 2]))

