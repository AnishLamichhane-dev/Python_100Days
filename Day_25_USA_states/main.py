import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_name_list =states_data.state.tolist()

guessed_states  = []
score = 0

while len(guessed_states) < 50:
    user_answer = screen.textinput(f"{len(guessed_states)}/50 States Correct","What's another state's name?").title()

    if user_answer == "Exit":
        missing_states = [each_state for each_state in states_name_list if each_state not in guessed_states]
        overall=pandas.DataFrame(missing_states)
        overall.to_csv("states_to_learn.csv") 
        break

    if user_answer in states_name_list:
        guessed_states.append(user_answer)
        score+=1
        correct_state = states_data[states_data.state == user_answer]

        tim = turtle.Turtle()
        tim.ht()
        tim.teleport((correct_state["x"]).tolist()[0],(correct_state["y"]).tolist()[0])
        tim.write(f"{user_answer}", move=False, align='center', font=('Arial', 6, 'normal'))

screen.exitonclick()


