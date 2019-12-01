import pyxel
from random import randint


class App:

    def __init__(self):
        pyxel.init(120, 180, caption='Flappy Bird')
        self.game_state = 'start'
        pyxel.load('flappy_bird.pyxres')  # 导入游戏素材
        self.score = 0
        self.bird_pos = [30, 80]
        self.speed = 0
        self.pipe_top_pos = [120, 80]
        self.pipe_bot_pos = [120, 110]
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == 'start':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'playing'
        elif self.game_state == 'playing':
            self.bird_pos[1] += self.speed
            self.speed += 0.35
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.speed = -3
            self.pipe_top_pos[0] -= 2
            self.pipe_bot_pos[0] -= 2
            # 管道移出屏幕重置位置
            if self.pipe_top_pos[0] < - 20:
                self.pipe_top_pos[0] = randint(160, 240)  # 随机设置上管道 x 坐标
                self.pipe_top_pos[1] = randint(60, 120)
                self.pipe_bot_pos[0] = self.pipe_top_pos[0]
                self.pipe_bot_pos[1] = self.pipe_top_pos[1] + 30
            # 计算得分
            if self.pipe_top_pos[0] - 12 <= 0 and self.pipe_top_pos[0] - 12 > -2:
                self.score += 1
            # 碰撞检测
            if abs(self.bird_pos[0] - self.pipe_top_pos[0]) < 16:
                if self.bird_pos[1] - self.pipe_top_pos[1] > 30 or self.bird_pos[1] - self.pipe_top_pos[1] < 0:
                    self.game_state = 'game over'

    def draw(self):
        if self.game_state == 'start':
                # 显示开始画面
            pyxel.cls(12)
            pyxel.text(36, 50, 'Flappy Bird', 8)
            pyxel.text(20, 60, 'Press Space to Play!', 1)
            pyxel.blt(50, 76, 0, 0, 2, 16, 11, 0)
        elif self.game_state == 'playing':
            pyxel.cls(12)
            pyxel.blt(0, 151, 1, 0, 17, 120, 23, 0)
            # 显示小鸟
            pyxel.blt(
                self.bird_pos[0],
                self.bird_pos[1],
                0, 0, 2, 16, 11, 0)
            pipe_length = 120 - self.pipe_top_pos[1]
            pyxel.blt(
                self.pipe_top_pos[0],
                0,
                0, 32, pipe_length, 16, self.pipe_top_pos[1], 0)
            pyxel.blt(
                self.pipe_bot_pos[0],
                self.pipe_bot_pos[1],
                0, 32, 128, 16, 128, 0)
            pyxel.blt(0, 174, 1, 0, 0, 120, 6, 0)
            pyxel.text(80, 10, 'Score:' + str(self.score), 2)

App()
