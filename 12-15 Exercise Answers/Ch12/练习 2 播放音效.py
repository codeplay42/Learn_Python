import pyxel


class App:

    def __init__(self):
        pyxel.init(200, 150, caption='Sound Play')
        pyxel.load('make_sound.pyxres')  # 导入声音文件
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.text(45, 60, 'Press A or D to play sound', 2)

    def update(self):
        if pyxel.btnp(pyxel.KEY_A):  # 按 A 键播放音乐
            pyxel.play(ch=0, snd=0)
        elif pyxel.btnp(pyxel.KEY_D):
            pyxel.play(ch=0, snd=1)

App()
