import turtle
import pandas

data=pandas.read_csv("50_states.csv")
screen=turtle.Screen()
screen.title("US")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
turtle.setup(725,491)

all_st=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50 :
    ans = screen.textinput( f"{len(guessed_states)}/50 Guessed correct" , "What's another state's name?" )
    ans = ans.title()
    if ans == "Exit":
        missing_states=[]
        for state in all_st :
            if state not in guessed_states :
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if ans in all_st :
        if ans not in guessed_states :
            guessed_states.append(ans)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        st=data[data.state==ans]
        t.goto((int(st.x),int(st.y)))
        t.write(ans)



