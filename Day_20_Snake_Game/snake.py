from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self,user_choosen_difficulty):
        self.all_segments_of_snake = []
        self.create_snake_body(user_choosen_difficulty)
        self.head = self.all_segments_of_snake[0]

    # def create_snake_body(self):
    #     STARTING_X_CORDINATE = 0
    #     for each_segment_of_snake in range(3):
    #         each_segment_of_snake = Turtle(shape="square")
    #         each_segment_of_snake.color("aliceblue")
    #         each_segment_of_snake.penup()
    #         each_segment_of_snake.goto(x=STARTING_X_CORDINATE, y=0)
    #         self.all_segments_of_snake.append(each_segment_of_snake)
    #         STARTING_X_CORDINATE -= 20
    
    def create_snake_body(self,user_choosen_difficulty):
        for each_position in STARTING_POSITIONS:
            self.add_segment_to_snake(each_position,user_choosen_difficulty)


    def add_segment_to_snake(self, each_position,user_choosen_difficulty):
        each_segment_of_snake = Turtle(shape="circle")
        each_segment_of_snake.color("aliceblue")
        each_segment_of_snake.penup()
        each_segment_of_snake.goto(each_position)
        each_segment_of_snake.speed(user_choosen_difficulty)
        print(each_segment_of_snake.speed())

        self.all_segments_of_snake.append(each_segment_of_snake)

    def extend(self,user_choosen_difficulty):
        self.add_segment_to_snake(self.all_segments_of_snake[-1].position(),user_choosen_difficulty)


    def move(self):

        for segment_num in range(len(self.all_segments_of_snake)-1, 0, -1):

            x_cordinate = self.all_segments_of_snake[segment_num - 1].xcor()
            y_cordinate = self.all_segments_of_snake[segment_num - 1].ycor()

            self.all_segments_of_snake[segment_num].goto(
                x_cordinate, y_cordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
