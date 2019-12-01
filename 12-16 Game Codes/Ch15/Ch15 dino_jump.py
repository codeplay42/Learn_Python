import pyxel
from random import randint


class App:

    def __init__(self):
        pyxel.init(200, 100, caption='Dinosaur Jump')
        self.game_state = 'start'
        pyxel.load('dino_jump.pyxres')
        self.score = 0
        self.dinasour_pos = [40, 56]
        self.dinasour_ani_pos = [(0, 0), (24, 0), (48, 0)]
        self.jump = False
        self.jump_distance = 8
        self.move_speed = 2
        self.cactus_pos = [220, 60, 320, 64]
        self.bird_pos = [800, 70]
        self.bird_ani_pos = [(9, 55), (41, 55)]
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.game_state == 'start':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.game_state = 'playing'
        elif self.game_state == 'playing':
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.jump = True
                pyxel.play(ch=0, snd=0)
            if self.jump:
                self.dinasour_pos[1] -= self.jump_distance
                self.jump_distance -= 0.6
                if self.dinasour_pos[1] > 56:
                    self.dinasour_pos[1] = 56
                    self.jump = False
                    self.jump_distance = 8
            if pyxel.btn(pyxel.KEY_LEFT):
                self.dinasour_pos[0] -= 2
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.dinasour_pos[0] += 2
            self.cactus_pos[0] -= self.move_speed
            self.cactus_pos[2] -= self.move_speed
            self.bird_pos[0] -= self.move_speed + 1
            if self.cactus_pos[0] < -10:
                self.score += 1
                self.cactus_pos[0] = randint(
                    max(220, self.cactus_pos[2] + 80), 300)
            if self.cactus_pos[2] < -10:
                self.score += 1
                self.cactus_pos[2] = randint(
                    max(220, self.cactus_pos[0] + 80), 300)
            if self.bird_pos[0] < -10:
                self.score += 1
                self.bird_pos[0] = randint(400, 800)
                self.bird_pos[1] = randint(20, 60)

            self.collision_detect(self.cactus_pos, 0, 16, 16)
            self.collision_detect(self.cactus_pos, 2, 16, 16)
            self.collision_detect(self.bird_pos, 0, 16, 16)

    def collision_detect(self, obj, index, x, y):
        if abs(self.dinasour_pos[0] - obj[index]) < x and abs(self.dinasour_pos[1] - obj[index + 1]) < y:
            self.game_state = 'game over'
            pyxel.play(ch=0, snd=1)

    def draw(self):
        if self.game_state == 'start':
            pyxel.text(76, 35, 'Dinosaur Jump', 3)
            pyxel.text(66, 50, 'Press Space to Play!', 2)
        elif self.game_state == 'playing':
            pyxel.cls(0)
            pyxel.text(160, 10, 'Score: ' + str(self.score), 2)
            pyxel.blt(0, 80, 0, 0, 88, 255, 8, 0)
            di_x = self.dinasour_ani_pos[int(pyxel.frame_count / 3) % 3][0]
            di_y = self.dinasour_ani_pos[int(pyxel.frame_count / 3) % 3][1]
            pyxel.blt(
                self.dinasour_pos[0],
                self.dinasour_pos[1],
                0, di_x, di_y, 24, 24, 0)
            pyxel.blt(
                self.cactus_pos[0],
                self.cactus_pos[1],
                0, 8, 32, 16, 24, 0)
            pyxel.blt(
                self.cactus_pos[2],
                self.cactus_pos[3],
                0, 24, 36, 16, 18, 0)
            bd_x = self.bird_ani_pos[int(pyxel.frame_count / 4) % 2][0]
            bd_y = self.bird_ani_pos[int(pyxel.frame_count / 4) % 2][1]
            pyxel.blt(
                self.bird_pos[0],
                self.bird_pos[1],
                0, bd_x, bd_y, 24, 20, 0)
        else:
            pyxel.text(80, 35, 'Game Over', 8)


App()
