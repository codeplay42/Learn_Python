import pyxel


class App:

    def __init__(self):
        pyxel.init(200, 150, caption='Sound Play')
        pyxel.sound(0).set(
            'c2rc2rg2rg2ra2ra2rg2rrr f2rf2re2re2rd2rd2rc2rrr'
            'g2rg2rf2rf2re2re2rd2rrr g2rg2rf2rf2re2re2rd2rrr'
            'c2rc2rg2rg2ra2ra2rg2rrr f2rf2re2re2rd2rd2rc2rrr',
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
