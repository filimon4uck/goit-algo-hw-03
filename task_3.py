def hanoi(n, source, target, auxiliary, pegs):
    if n == 1:
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {source} to {target}: {disk}")
        print(f"Current state: {pegs}")
    else:
        hanoi(n - 1, source, auxiliary, target, pegs)
        disk = pegs[source].pop()
        pegs[target].append(disk)
        print(f"Move disk {source} to {target}: {disk}")
        print(f"Current state: {pegs}")
        hanoi(n - 1, auxiliary, target, source, pegs)


def input_disks():
    while True:
        try:
            user_input = int(input("Input number of disk"))
            if user_input < 0:
                raise ValueError("Number must be bigger than 0")
            return user_input
        except ValueError as e:
            print(f"Input error: {e}")


def main():
    n = input_disks()

    pegs = {"A": list(range(n, 0, - 1)), "B": [], "C": []}

    print("Starting state", pegs)
    hanoi(n, "A", "B", "C", pegs)
    print("Final state", pegs)


if __name__ == "__main__":
    main()
