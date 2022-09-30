import pyxel


class App:
    def __init__(self):
        self.img = 0

        pyxel.init(256, 256)

        # load our images into the 3 image banks
        pyxel.image(0).load(0, 0, "img1.jpg")
        pyxel.image(1).load(0, 0, "img2.jpg")
        pyxel.image(2).load(0, 0, "img3.jpg")

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count % 60 == 0:
            self.img = (self.img + 1) % 3

    def draw(self):
        # draw the current image bank at (0, 0) with a size of (256, 256)
        pyxel.blt(0, 0, self.img, 0, 0, 256, 256)


if __name__ == "__main__":
    App().run()
