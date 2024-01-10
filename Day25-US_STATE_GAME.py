import turtle
import pandas

#TODO make a screen with the image
screen=turtle.Screen()
image="../Desktop/python codes/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer=turtle.Turtle()
writer.color("black")
writer.penup()

##TODO acquire coordinates of diffrent locations(states) from the screen
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


us_states_data=pandas.read_csv("../Desktop/python codes/us-states-game-start/50_states.csv")
us_states_only=us_states_data["state"]
all_us_states_list=us_states_only.to_list()
correct_answer_list=[]
correct_answer=0

while len(correct_answer_list)<50:
    # TODO make a textinput window
    state_answer = screen.textinput(title=f"Score : {correct_answer}/50", prompt=f"what's another state name ?  ")
    for state in all_us_states_list:
        if state_answer.lower().replace(" ","")==state.lower().replace(" ",""):
            correct_answer+=1
            correct_answer_list.append(state_answer)
            state_answer_details=us_states_data[us_states_data.state==state]
            print(state_answer_details)
            xcor=int(state_answer_details["x"])
            print(xcor)
            ycor=int(state_answer_details["y"])
            print(ycor)
            writer.goto(xcor,ycor)
            writer.write(arg=state)
    if state_answer.lower()=="exit":
        break

#TODO make a csv file for unguessed states
print(all_us_states_list)
print(correct_answer_list)
# unguessed_states_list=all_us_states_list
unguessed_states_list=[state for state  in all_us_states_list if state.lower().replace(" ","") not in correct_answer_list]
# for state in correct_answer_list:
#     unguessed_states_list.remove(state.title())
print(unguessed_states_list)
print(len(unguessed_states_list))

unguessed_states_dict={"State":unguessed_states_list}
unguessed_data=pandas.DataFrame(unguessed_states_dict)
# you have to close the exel file to avoid error
unguessed_data.to_csv("../Desktop/python codes/us-states-game-start/states_to_learn.csv")