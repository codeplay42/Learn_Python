import pyxel


class App:

    def __init__(self):
        pyxel.init(200, 150, caption='Sound Play')
        pyxel.sound(0).set(
            'c2c2d2d2e2e2c2c2 c2c2d2d2e2e2c2c2 e2e2f2f2g2g2rr e2e2f2f2g2g2rr'
            'g2a2g2f2e2e2c2c2 g2a2g2f2e2e2c2c2 d2d2g1g1c2c2rr d2d2g1g1c2c2rr',
            'p',
            '6',
            'n',
            30
        )
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.text(80, 50, 'Sound Play', 2)  # 显示文字
        pyxel.text(75, 65, '1: play music', 3)
        pyxel.text(75, 75, '2: stop music', 3)

    def update(self):
        if pyxel.btnp(pyxel.KEY_1):  # 按1键播放音乐
            pyxel.play(0, 0, loop=True)
        elif pyxel.btnp(pyxel.KEY_2):
            pyxel.stop()

App()
