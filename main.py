import turtle
import pandas

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
score = 0
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
missing_data = pandas.read_csv('missing_states.csv')
states = data.state.to_list()
guessed_states = []
missing_states = []
ms_dict = {'state': missing_states}

while len(guessed_states) < 50:
    t.hideturtle()
    t.penup()
    user_answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                   prompt='Enter a state\'s name:').title()
    if user_answer == 'Exit':
        for i in states:
            if i not in guessed_states:
                missing_states.append(i)
        df = pandas.DataFrame(ms_dict)
        df.to_csv('missing_states.csv', mode='w')
        break
    if user_answer in states:
        answer_checker = data[data.state == user_answer]
        t.goto(int(answer_checker.x), int(answer_checker.y))
        t.write(arg=f'{user_answer}', align='center', font=('Arial', 8, 'bold'))
        if user_answer not in guessed_states:
            guessed_states.append(user_answer)
if guessed_states == 50:
    t.write(arg='CONGRATULATIONS!', align='center', font=('Arial', 25, 'bold'))

screen.exitonclick()
