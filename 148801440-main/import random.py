import random


def main():
    for i in range(10):
        difficulty = get_level()
        num1 = generate_integer(difficulty)
        num2 = generate_integer(difficulty)
        game_logic(num1, num2)


def game_logic(x,y):
    score = 0
    attempts = 1
    z = x + y
    while True:
        prompt = f"{x} + {y} = "
        try:
            result = int(input(prompt))
        except ValueError:
            continue
        if result != z:
            if attempts == 3:
                print(prompt, z)
                attempts = 1
                break
            print("EEE")
            attempts += 1
            continue
        elif result == z:
            attempts = 1
            score += 1
            break

    print(f"Score:{score}")


def get_level():
    while True:
        try:
            level = int(input("Level:"))
        except ValueError:
            continue
        if level != 0 and level <= 3:
            return level


def generate_integer(level):
    max_range = 0
    min_range = 0
    if level == 1:
        max_range, min_range = 9, 0
    elif level == 2:
        max_range, min_range = 99, 10
    else:
        max_range, min_range = 999, 100
    return random.randint(min_range, max_range)


if __name__ == "__main__":
    main()
