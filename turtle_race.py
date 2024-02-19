from turtle import Turtle , Screen
import random 
t=Turtle()
sc=Screen()
sc.setup(width=600,height=400)
t.hideturtle()
t.penup()
colors = ["red", "blue", "green", "orange", "purple", "pink", "brown"]
t.goto(-290,180)
t.write("Available colors: " + ", ".join(colors), align="left", font=("Arial", 12, "normal"))
user_bet=sc.textinput(title="PLACE YOUR BET!!!", prompt="Who will win? choose your Poison: ")
y=[-90,-60,-30,0,30,60,90]
all_turtle = []

for _ in range(7):
    t= Turtle(shape="turtle")
    t.color(colors[_])
    t.penup()
    t.goto(x=-280, y=y[_])   
    all_turtle.append(t)

is_race= True
if user_bet:
 while is_race:
    for turtle in all_turtle:
        rand_distance= random.randint(1,30)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 280:
            is_race = False
            winning_color = turtle.color()
            if user_bet.lower() == winning_color[0].lower():
                print("Congratulations! You won!")
            else:
                print("Sorry, you lost.")
            break
    
    
    
sc.mainloop()
