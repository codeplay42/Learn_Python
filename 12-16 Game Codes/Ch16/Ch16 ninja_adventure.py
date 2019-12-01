import pyxel
from random import randint


class App:

    def __init__(self):
        pyxel.init(250, 150, caption='Ninja Adventure')
        self.game_state = 'start'
        pyxel.load('ninja.pyxres')
        self.score = 0
        self.ninja_pos = [40, 112]
        self.jump = False
        self.jump_speed = 8
        self.dart_pos = [-20, 60]
        self.shoot = False
        self.monster_pos = [260, 100, 280, 90, 300, 80]
        self.life = 3
        self.fireball_pos = [260, 100]
        self.fireball_shoot = False
        self.heart_pos = [120, -500]
        self.mp = 3
        self.count = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == 'start':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'playing'
        elif self.game_state == 'playing':
            if pyxel.btn(pyxel.KEY_LEFT):
                self.ninja_pos[0] -= 2
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.ninja_pos[0] += 2
            if self.ninja_pos[1] > 60:
                if pyxel.btnp(pyxel.KEY_UP):
                    self.jump = True
                    self.jump_speed = 8
                    pyxel.play(ch=0, snd=0)
            if self.jump:
                self.ninja_pos[1] -= self.jump_speed
                self.jump_speed -= 0.6
                if self.ninja_pos[1] > 112:
                    self.ninja_pos[1] = 112
                    self.jump = False
            if pyxel.btnp(pyxel.KEY_S):
                self.shoot = True
                self.dart_pos[0] = self.ninja_pos[0] + 16
                self.dart_pos[1] = self.ninja_pos[1] + 12
            if self.shoot:
                if self.dart_pos[0] > 0 and self.dart_pos[0] < 260:
                    self.dart_pos[0] += 8
                else:
                    self.shoot = False
                    self.dart_pos[1] = 200
            for i in range(0, 6, 2):
                self.monster_pos[i] -= 2
                if self.monster_pos[i] < -10:
                    self.monster_pos[i] = randint(270, 350)
                    self.monster_pos[i + 1] = randint(70, 110)
                if abs(self.dart_pos[0] - self.monster_pos[i]) < 8 and abs(self.dart_pos[1] - self.monster_pos[i + 1]) < 10:
                    self.monster_pos[i] = randint(270, 350)
                    self.monster_pos[i + 1] = randint(70, 110)
                    self.score += 1
                if abs(self.ninja_pos[0] - self.monster_pos[i]) < 20 and abs(self.ninja_pos[1] - self.monster_pos[i + 1]) < 10:
                    self.monster_pos[i] = randint(270, 350)
                    self.monster_pos[i + 1] = randint(70, 110)
                    self.life -= 1
            if self.life == 0:
                self.game_state = 'game over'
                pyxel.play(ch=0, snd=1)

            if self.monster_pos[0] >= 246 and self.monster_pos[0] < 248:
                self.fireball_shoot = True
                self.fireball_pos[0] = self.monster_pos[0] + 8
                self.fireball_pos[1] = self.monster_pos[1] + 8
            if self.fireball_shoot:
                self.fireball_pos[0] -= 3
                if self.fireball_pos[0] < -10:
                    self.fireball_shoot = False
            if abs(self.ninja_pos[0] - self.fireball_pos[0]) < 20 and abs(self.ninja_pos[1] - self.fireball_pos[1]) < 6:
                self.fireball_pos = [260, 100]
                self.life -= 1

            self.heart_pos[1] += 2
            if abs(self.ninja_pos[0] - self.heart_pos[0]) < 12 and abs(self.ninja_pos[1] - self.heart_pos[1]) < 12:
                if self.life < 3:
                    self.life += 1
                self.heart_pos[0] = randint(60, 160)
                self.heart_pos[1] = randint(-1000, -500)
            if self.heart_pos[1] > 160:
                self.heart_pos[0] = randint(60, 160)
                self.heart_pos[1] = randint(-1000, -500)

            if pyxel.btnp(pyxel.KEY_D):
                if self.mp == 3:
                    self.mp = 0
                    self.ninja_pos[0] = min(self.ninja_pos[0] + 100, 240)
                    self.count = 1
            if self.count:
                self.count += 1
                self.mp = int(self.count // 200)
                if self.mp == 3:
                    self.count = 0

    def draw(self):
        if self.game_state == 'start':
            pyxel.text(100, 55, 'Ninja Adventure', 3)
            pyxel.text(90, 70, 'Press Space to Play!', 2)
        elif self.game_state == 'playing':
            pyxel.cls(0)
            pyxel.text(200, 15, 'Score: ' + str(self.score), 2)
            pyxel.blt(0, 136, 1, 0, 0, 250, 2, 0)
            pyxel.blt(
                self.ninja_pos[0],
                self.ninja_pos[1],
                0, 25, 0, 22, 24, 0)
            pyxel.blt(
                self.dart_pos[0],
                self.dart_pos[1],
                0, 2, 2, 12, 12, 0)
            for i in range(0, 6, 2):
                pyxel.blt(
                    self.monster_pos[i],
                    self.monster_pos[i + 1],
                    0, 8 * i, 32, 16, 16, 0)
            pyxel.blt(
                self.fireball_pos[0],
                self.fireball_pos[1],
                0, 4, 53, 8, 8, 0)
            pyxel.blt(10, 6, 0, 0, 68, 16 * self.life, 12, 0)
            pyxel.blt(
                self.heart_pos[0],
                self.heart_pos[1],
                0, 0, 68, 16, 12, 0)
            pyxel.blt(10, 22, 0, 0, 85, 16 * self.mp, 12, 0)
        else:
            pyxel.text(110, 55, 'Game Over', 8)
            pyxel.text(85, 70, 'Press Space to Restart!', 2)
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'playing'
                self.score = 0
                self.life = 3
                self.monster_pos = [260, 100, 280, 90, 300, 80]
                self.heart_pos = [120, -500]
                self.count = 0
                self.mp = 3

App()
