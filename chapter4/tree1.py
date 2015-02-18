import turtle
import random


def tree(branch_len, t):
	#t.color("black")
	if branch_len > 1:
		t.forward(branch_len)
		t.right(20)
		tree(branch_len - 20, t)
		t.left(40)
		tree(branch_len - 20, t)
		t.right(20)
		tree(branch_len - 20, t)
		t.color("green")
		t.backward(branch_len)


def main():
	t = turtle.Turtle()
	my_win = turtle.Screen()
	t.left(90)
	#t.up()
	#t.backward(90)
	#t.down()
	t.color("brown")
	tree(90, t)
	my_win.exitonclick()

main()
