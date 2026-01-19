from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 10
        self.MOVE_INCREMENT = 5

    def spawn_car(self):
        if random.randint(0, 2) == 0:
            tom = Turtle()
            tom.shape("circle")
            tom.penup()
            tom.color(random.choice(COLORS))
            tom.setheading(180)
            tom.speed("fastest")
            self.all_cars.append(tom)

    def send_car_to_start(self):
        for each_car in self.all_cars:
            if each_car.xcor() == 0 and each_car.ycor() == 0:
                each_car.goto(320, random.randint(-230, 240))

    def moving_car(self):
        for each_car in self.all_cars:
            if each_car.xcor() <= -320:
                each_car.ht()
            else:
                each_car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

