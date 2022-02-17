'''
es5:
Scrivere uno snake in python utilizzando la libreria turtle

Andrea Tomatis
'''

import turtle #documentazione: https://docs.python.org/3/library/turtle.html
import random #documentazione: https://docs.python.org/3/library/random.html


#inizializzazione dello snake (rappresentato da un cursore)
snake = turtle.Turtle()
snake.resizemode("user")
snake.shapesize(2.5, 2.5, 3)
snake.pencolor("blue")

#screen size
width = 800
height = 600

#inizializzazione della finestra di gioco
win = turtle.Screen()
win.setup(width=width, height=height)
win.title("Snake")
win.bgcolor("green")
win.register_shape("mela.gif") #registra una nuova forma per un cursore presa da file

#le mele sono realizzate da un cursore che si sposta
mela = turtle.Turtle()
mela.hideturtle()
mela.shape("mela.gif")
mela.up()

#punteggio realizzato dall'utente
punti = 0


#funzione per spostare lo snake verso sinistra
def left():
    snake.setheading(180)
    snake.setx(snake.xcor() - 10)
    if snake.xcor() < (width/2-20) * -1:
        win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
        False, align="center", font=("Arial", 30, "normal"))
    controllaMela()


#funzione per spostare lo snake verso destra
def right():
    snake.setheading(0)
    snake.setx(snake.xcor() + 10)
    if snake.xcor() > (width/2-20):
        win.clear()
        turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
        False, align="center", font=("Arial", 30, "normal"))
    controllaMela()


#funzione per spostare lo snake verso l'alto
def up():
	snake.setheading(90)
	snake.sety(snake.ycor() + 10)
	if snake.ycor() > height/2-20:
		win.clear()
		turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
		False, align="center", font=("Arial", 30, "normal"))
	controllaMela()


#funzione per spostare lo snake verso il basso
def down():
	snake.setheading(270)
	snake.sety(snake.ycor() - 10)
	if snake.ycor() < (height/2-20) * -1:
		win.clear()
		turtle.write(f"Hai perso! Il tuo punteggio e': {punti}",
		False, align="center", font=("Arial", 30, "normal"))
	controllaMela()


#funzione che controlla se lo snake mangia la mela
def controllaMela():
	if snake.pos() == mela.pos():
		aggiungiMela(width, height) #la mela si sposta in una nuova posizione
		global punti
		punti += 1  #il giocatore guadagna un punto


#la mela viene spostata in coordinate random
def aggiungiMela(width, height):
	x = random.randint(width/2 * -1, width/2)//10 * 10
	y = random.randint(height/2 * -1, height/2)//10 * 10
	mela.hideturtle()
	mela.setx(x)
	mela.sety(y)
	mela.showturtle()



def main():
	aggiungiMela(width, height)

	win.onkey(left, "Left")
	win.onkey(right, "Right")
	win.onkey(up, "Up")
	win.onkey(down, "Down")
	win.listen()
	win.mainloop()

	print(f"Hai perso: hai totalizzato {punti} punti")

if __name__ == "__main__":
	main()
