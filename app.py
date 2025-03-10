import pyxel

pyxel.init(39, 33, title="Morpion")
pyxel.load("res.pyxres")

class Morpion:
    def __init__(self):
        self.j = 1
        self.m = [[0, 5, 10], [15, 20, 25], [30, 35, 40]]

    def update(self):
        self.affichage()
        self.tableau()

    def draw(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.j = 1
            self.m = [[0, 5, 10], [15, 20, 25], [30, 35, 40]]

        if self.j == 1:
            pyxel.blt(3, 27, 0, 0, 0, 5, 3)
            for i in range(3):
                for k in range(3):
                    if pyxel.btnp(pyxel.KEY_KP_1 + i * 3 + k) or pyxel.btnp(pyxel.KEY_1 + i * 3 + k):
                        if self.m[i][k] != 46 and self.m[i][k] != 53:
                            self.m[i][k] = 46
                            self.j = 2
                            break

        elif self.j == 2:
            pyxel.blt(31, 27, 0, 0, 0, 5, 3)
            for i in range(3):
                for k in range(3):
                    if pyxel.btnp(pyxel.KEY_KP_1 + i * 3 + k) or pyxel.btnp(pyxel.KEY_1 + i * 3 + k):
                        if self.m[i][k] != 46 and self.m[i][k] != 53:
                            self.m[i][k] = 53
                            self.j = 1
                            break

        if self.win1():
            self.j = 3
            pyxel.rectb(2, 8, 7, 19, 11)
            pyxel.text(4, 28, "J1 a win", 8)

        elif self.win2():
            self.j = 4
            pyxel.rectb(30, 8, 7, 19, 11)
            pyxel.text(4, 28, "J2 a win", 8)

        elif self.win3():
            self.j = 5
            pyxel.rectb(2, 8, 7, 19, 13)
            pyxel.rectb(30, 8, 7, 19, 13)
            pyxel.text(3, 28, "Match nul", 8)

    def affichage(self):
        pyxel.cls(0)
        pyxel.blt(1, 1, 0, 0, 16, 37, 5)
        pyxel.blt(3, 9, 0, 0, 24, 5, 11)
        pyxel.blt(31, 9, 0, 6, 24, 5, 11)
        pyxel.blt(3, 21, 0, 46, 8, 5, 5)
        pyxel.blt(31, 21, 0, 53, 8, 5, 5)
        for i in range(4):
            pyxel.line(10 + i * 6, 8, 10 + i * 6, 26, 7)
            pyxel.line(10, 8 + i * 6, 28, 8 + i * 6, 7)

    def tableau(self):
        for i in range(3):
            for j in range(3):
                pyxel.blt(11 + j * 6, 9 + i * 6, 0, self.m[i][j], 8, 5, 5)

    def win1(self):
        n = len(self.m)
        p = 46

        for i in range(n):
            if all(self.m[i][j] == p for j in range(n)):
                return True
            if all(self.m[j][i] == p for j in range(n)):
                return True

        if all(self.m[i][i] == p for i in range(n)):
            return True
        if all(self.m[i][n - 1 - i] == p for i in range(n)):
            return True

        return False

    def win2(self):
        n = len(self.m)
        p = 53
        for i in range(n):
            if all(x == p for x in self.m[i]):
                return True
            if all(self.m[j][i] == p for j in range(n)):
                return True
        if all(self.m[i][i] == p for i in range(n)):
            return True
        if all(self.m[i][n - 1 - i] == p for i in range(n)):
            return True
        return False

    def win3(self):
        n = len(self.m)
        p1 = 46
        p2 = 53

        if all(self.m[i][j] in (p1, p2) for i in range(n) for j in range(n)):
            return True
        return False

morpion = Morpion()
pyxel.run(morpion.update, morpion.draw)