import turtle
import random

def tree(branch_len, t):
	if branch_len > 5:
		if branch_len <= 15:
			t.color("green")
		angle = random.randint(20,45)
		blen = random.randint(1,10)
		t.forward(branch_len)
		t.right(angle)
		tree(branch_len - blen, t)
		t.left(angle)
		tree(branch_len - blen, t)
		t.right(angle)
		t.backward(branch_len)

def main():
	t = turtle.Turtle()
	my_win = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("brown")
	tree(70, t)
	my_win.exitonclick()

main()
