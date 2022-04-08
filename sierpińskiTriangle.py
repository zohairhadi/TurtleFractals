import turtle
import random
import time


pen = turtle.Turtle()

corner1 = pen.position()
corner2 = pen.position()
corner3 = pen.position()


class SierpińskiTriangle:
    def __init__(self, corner1, corner2, corner3, pen):
        self.corner1 = corner1
        self.corner2 = corner2
        self.corner3 = corner3
        self.pen = pen

    def draw(self):
        # inital dot anywhere inside triangle
        self.pen.forward(200)
        self.pen.dot()
        currentPenPosition = self.pen.position()

        while True:
            randCorner = random.randint(1, 3)
            if randCorner == 1:
                midpoint = ((self.corner1[0] + currentPenPosition[0]) / 2,
                            (self.corner1[1] + currentPenPosition[1]) / 2)
            elif randCorner == 2:
                midpoint = ((self.corner2[0] + currentPenPosition[0]) / 2,
                            (self.corner2[1] + currentPenPosition[1]) / 2)
            else:
                midpoint = ((self.corner3[0] + currentPenPosition[0]) / 2,
                            (self.corner3[1] + currentPenPosition[1]) / 2)

            # print(midpoint)
            self.pen.goto(midpoint)
            self.pen.dot(3, "red")
            currentPenPosition = self.pen.position()

    def drawInitalTriangle(self):
        # corner 1
        self.pen.dot()
        self.corner1 = self.pen.position()
        self.pen.forward(200)
        self.pen.left(120)

        # corner 2
        self.pen.dot()
        self.corner2 = self.pen.position()
        self.pen.forward(200)
        self.pen.left(120)

        # corner 3
        self.pen.dot()
        self.corner3 = self.pen.position()
        self.pen.forward(200)
        self.pen.left(120)


# Main Section
pen.penup()

triangle = SierpińskiTriangle(corner1, corner2, corner3, pen)
triangle.drawInitalTriangle()
triangle.draw()

time.sleep(5)
# hide the turtle
pen.hideturtle()
