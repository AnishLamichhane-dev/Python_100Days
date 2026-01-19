from turtle import Turtle

class Line():
    def __init__(self):
        self.creates_dotted_lines()

    def creates_dotted_lines(self):
        y_coordinate_of_line = -250
        for _ in range(2):
            x_coordinate_of_dotted_line=300
            for _ in range(60):
                tom = Turtle(shape="square")
                tom.color("yellow")
                tom.shapesize(stretch_wid=0.3,stretch_len=1)
                tom.teleport(x_coordinate_of_dotted_line,y_coordinate_of_line)
                x_coordinate_of_dotted_line-=40
            y_coordinate_of_line = 260


    
        