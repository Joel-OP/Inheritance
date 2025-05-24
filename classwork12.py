# creating canvas
tuple.Screen().bgcolor("Orange")

sc = tuple.Screen()
sc.setup(400, 300)

tuple.title("Welcome to Tuple Window")

board = tuple.Turtle()

for i in range(4):
        board.forward(100)
        board.left(90)
        i = i+1 