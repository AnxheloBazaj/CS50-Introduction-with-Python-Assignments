import random


def main():
    generate_integer(get_level())


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
    score = 0
    attempts = 1
    if level == 1:
        max_range, min_range = 9, 0
    elif level == 2:
        max_range, min_range = 99, 10
    else:
        max_range, min_range = 999, 100

    for i in range(10):
        x = random.randint(min_range, max_range)
        y = random.randint(min_range, max_range)
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


if __name__ == "__main__":
    main()
