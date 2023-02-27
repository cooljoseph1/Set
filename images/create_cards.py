from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class Shape:
    def __init__(self, fill, shape):
        self.image = Image.open("shapes/" + fill + "_" + shape + ".png").convert("RGB")
        self.image = np.array(self.image) / 255

class Card:
    def __init__(self, number, color, fill, shape, padding=15):
        self.name = str(number) + "_" + color + "_" + fill + "_" + shape
        self.shape = Shape(fill, shape)
        self.color = color
        self.number = number

        self.padding = padding
        self._create_image()

    def _create_image(self):
        self.shape_height, self.shape_width, _ = self.shape.image.shape
        
        self.height = self.shape_height + 2 * self.padding
        self.width = 3 * self.shape_width + 4 * self.padding
        
        self.image = np.ones((self.height, self.width, 3))

        self._set_number()
        self._set_color()

        # Make black border
        self.image[0, :, :] = 0.0
        self.image[-1, :, :] = 0.0
        self.image[:, 0, :] = 0.0
        self.image[:, -1, :] = 0.0

    def _set_number(self):
        if self.number == 1:
            self.image[self.padding : self.padding+self.shape_height,
                       2 * self.padding + self.shape_width : 2 * self.padding + 2 * self.shape_width] = self.shape.image
        elif self.number == 2:
            self.image[self.padding : self.padding + self.shape_height,
                       (3 * self.padding) // 2 + self.shape_width // 2 : (3 * self.padding) // 2 + self.shape_width // 2 + self.shape_width] = self.shape.image
            self.image[self.padding : self.padding + self.shape_height,
                       (5 * self.padding) // 2 + (3 * self.shape_width) // 2 : (5 * self.padding) // 2 + (3 * self.shape_width) // 2 + self.shape_width] = self.shape.image

        else:
            self.image[self.padding : self.padding+self.shape_height,
                       self.padding : self.padding + self.shape_width] = self.shape.image
            self.image[self.padding : self.padding+self.shape_height,
                       2 * self.padding + self.shape_width : 2 * self.padding + 2 * self.shape_width] = self.shape.image
            self.image[self.padding : self.padding+self.shape_height,
                       3 * self.padding + 2 * self.shape_width : 3 * self.padding + 3 * self.shape_width] = self.shape.image
    
    def _set_color(self):
        color = None
        if self.color == "red":
            color = [1.0, 0.1, 0.2]
        elif self.color == "blue":
            color = [0.2, 0.2, 1.0]
        elif self.color == "gold":
            color = [0.9, 0.8, 0.0]
        self.image = 1 - (1 - self.image) * (1 - np.array(color))

    def save(self, name=None):
        name = name or self.name
        image = (self.image * 255).astype("uint8")
        image = Image.fromarray(image)
        image.save("cards/" + name + ".png")


for number in [1, 2, 3]:
    for color in ["red", "blue", "gold"]:
        for fill in ["solid", "open", "striped"]:
            for shape in ["oval", "diamond", "star"]:
                card = Card(number, color, fill, shape)
                card.save()
