import turtle
import pandas

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S State Game")
screen.addshape(image)
turtle.shape(image)
game_on = True
guessed = 0

text = turtle.Turtle()
text.hideturtle()
text.penup()

game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.backward(150)

guessed_states = []
not_guessed_states = []



data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()


while game_on:
    answer_state = screen.textinput(f"{guessed}/50 states correct", "What is another state name").lower()
    if guessed == 50:
        game_over.write("GAME OVER",font=('Arial', 50, 'normal'))
        game_on = False
    elif answer_state == "exit":
        break
    else:

        for state in states_list:
            if state.lower() == answer_state:
                guessed_states.append(state)
                coordinates = data[data["state"] == state]
                x_position = int(coordinates["x"].iloc[0])
                y_position = int(coordinates["y"].iloc[0])
                text.goto(x_position, y_position)

                text.write(f"{state}")
                text.color("black")
                guessed = guessed + 1

not_guessed_states = [state for state in states_list if state not in guessed_states]

pandas.DataFrame(not_guessed_states).to_csv("not_guessed_states.csv")
























