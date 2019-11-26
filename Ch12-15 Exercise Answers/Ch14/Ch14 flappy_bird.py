import pyxel
from random import randint


class App:

    def __init__(self):
        pyxel.init(120, 180, caption='Flappy Bird')
        pyxel.load('flappy_bird.pyxres')
        self.game_state = 'start'
        self.score = 0
        self.bird_pos = [30, 80]
        self.speed = 0
        self.pipe_top_pos = [120, 80]
        self.pipe_bot_pos = [120, 110]
        self.play_sound = True  # 添加播放音效变量
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
                pyxel.play(ch=0, snd=0)  # 添加飞跃音效
            self.pipe_top_pos[0] -= 2
            self.pipe_bot_pos[0] -= 2
            if self.pipe_top_pos[0] < - 20:
                self.pipe_top_pos[0] = randint(160, 240)
                self.pipe_top_pos[1] = randint(60, 120)
                self.pipe_bot_pos[0] = self.pipe_top_pos[0]
                self.pipe_bot_pos[1] = self.pipe_top_pos[1] + 30
            if self.pipe_top_pos[0] - 12 <= 0 and self.pipe_top_pos[0] - 12 > -2:
                self.score += 1
            if abs(self.bird_pos[0] - self.pipe_top_pos[0]) < 16:
                if self.bird_pos[1] - self.pipe_top_pos[1] > 30 or self.bird_pos[1] - self.pipe_top_pos[1] < 0:
                    self.game_state = 'game over'

    def draw(self):
        if self.game_state == 'start':
            pyxel.cls(12)
            pyxel.text(36, 50, 'Flappy Bird', 8)
            pyxel.text(20, 60, 'Press Space to Play!', 1)
            pyxel.blt(50, 76, 0, 0, 2, 16, 11, 0)
        elif self.game_state == 'playing':
            pyxel.cls(12)
            pyxel.blt(0, 151, 1, 0, 17, 120, 23, 0)
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
        elif self.game_state == 'game over':
            pyxel.text(42, 50, 'Game Over', 8)
            pyxel.text(25, 60, 'Press S to Restart!', 2)
            if self.play_sound:
                pyxel.play(ch=0, snd=1)  # 添加游戏结束音效
                self.play_sound = False
            # 按 S 键重新开始游戏
            if pyxel.btnp(pyxel.KEY_S):
                self.game_state = 'playing'
                self.score = 0
                self.speed = 0
                self.pipe_top_pos = [120, 80]
                self.pipe_bot_pos = [120, 110]
                self.play_sound = True

App()
