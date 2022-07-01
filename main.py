import turtle
import pandas
screen = turtle.Screen()
screen.setup(width=550, height=600)
screen.title("Guess_indian_states/UT")
image = "tinywow_jpg_to_gif_3132449.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []

while len(guessed_state) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/28", prompt="Guess another state ").title()

    data = pandas.read_csv("india_state.csv")
    all_states = data.state.to_list()
    if answer_state == "Exit":
        missing_state = [states for states in all_states if states not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States to learn")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color("white")
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

guessed_ut = []
while len(guessed_ut) < 8:
    answer_ut = screen.textinput(title=f"{len(guessed_ut)}/8", prompt="Guess another UT ").title()
    data = pandas.read_csv("indian_ut.csv")
    all_ut = data.ut.to_list()
    if answer_ut == "Exit":
        missing_ut = [ut for ut in all_ut if ut not in guessed_ut]
        new_data = pandas.DataFrame(missing_ut)
        new_data.to_csv("UT to learn")
        break
    if answer_ut in all_ut:
        guessed_ut.append(answer_ut)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("white")
        ut_data = data[data.ut == answer_ut]
        t.goto(int(ut_data.X), int(ut_data.Y))
        t.write(answer_ut)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

