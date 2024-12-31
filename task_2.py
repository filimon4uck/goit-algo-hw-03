import turtle


def koch_curve(t: turtle.Turtle, order, size):
    if order == 0:
        t.fd(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=200):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    window.mainloop()


def input_depth():
    while True:
        try:
            user_input = int(input("Input depth recursion"))
            if user_input < 0:
                raise ValueError("Depth must be bigger than 0")
            return user_input
        except ValueError as e:
            print(f"Input error: {e}")


def main():
    order = input_depth()
    draw_koch_snowflake(order)


if __name__ == "__main__":
    main()
