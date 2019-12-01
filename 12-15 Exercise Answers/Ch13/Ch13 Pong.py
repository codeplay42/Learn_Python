import pyxel


class App:

    def __init__(self):
        pyxel.init(160, 120, caption='Pong')
        pyxel.load('sounds.pyxres')  # 导入音效文件
        self.game_state = 'start'
        self.ball_x = 60
        self.ball_y = 60
        self.x_speed = 3
        self.y_speed = 3
        self.pannel_pos = [0, 60, 158, 60]
        self.score = [0, 0]
        self.play_sound = True  # 新建变量
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == 'start':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'playing'
        elif self.game_state == 'playing':
            self.ball_x += self.x_speed
            self.ball_y += self.y_speed
            if self.ball_x < 5:
                self.x_speed = -self.x_speed
                if self.ball_y <= self.pannel_pos[1] + 18 and self.ball_y >= self.pannel_pos[1]:
                    self.score[0] += 1
                    pyxel.play(ch=0, snd=0)  # 播放碰撞音效
                else:
                    self.game_state = 'game over'  # 如果漏接球，则游戏结束
            if self.ball_x > 155:
                self.x_speed = -self.x_speed
                if self.ball_y <= self.pannel_pos[3] + 18 and self.ball_y >= self.pannel_pos[3]:
                    self.score[1] += 1
                    pyxel.play(ch=0, snd=0)
                else:
                    self.game_state = 'game over'

            if self.ball_y < 5 or self.ball_y > 115:
                self.y_speed = -self.y_speed
            if pyxel.btn(pyxel.KEY_W):
                self.pannel_pos[1] -= 3
            elif pyxel.btn(pyxel.KEY_S):
                self.pannel_pos[1] += 3
            if pyxel.btn(pyxel.KEY_UP):
                self.pannel_pos[3] -= 3
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.pannel_pos[3] += 3

    def draw(self):
        if self.game_state == 'start':
            pyxel.text(75, 40, 'Pong', 8)
            pyxel.text(40, 60, 'Press Space to Play!', 2)
        elif self.game_state == 'playing':
            pyxel.cls(0)
            pyxel.circ(self.ball_x, self.ball_y, 3, 8)
            pyxel.rect(self.pannel_pos[0], self.pannel_pos[1], 2, 18, 4)
            pyxel.rect(self.pannel_pos[2], self.pannel_pos[3], 2, 18, 4)
            pyxel.text(40, 10, str(self.score[0]), 2)
            pyxel.text(120, 10, str(self.score[1]), 2)
        # 添加 Game Over 状态
        else:
            pyxel.text(60, 50, 'Game Over', 8)
            # 播放 1 次 Game Over 音效
            if self.play_sound:
                pyxel.play(ch=0, snd=1)
                self.play_sound = False

App()
