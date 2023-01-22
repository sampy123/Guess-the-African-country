import turtle
import pandas

screen = turtle.Screen()
screen.title("African country Quiz Game")
image = "Africa.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("54_countries.csv")
all_countries = data.countries.to_list()

answer_country = screen.textinput(
    title="Guess The Country", prompt="What's the country's name")
print(answer_country)

if answer_country in all_countries:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    country_data = data[data.countries == answer_country]
    t.goto(int(country_data.x), int(country_data.y))
    t.write(answer_country)

turtle.mainloop()
