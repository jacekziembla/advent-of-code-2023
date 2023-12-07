with open("01/input.txt", "r") as file:
    lines = file.read().split()


def get_calibration_number(word: str) -> int:
    digits = [char for char in word if char.isdigit()]
    return int(digits[0] + digits[-1])


# Part 1
numbers = [get_calibration_number(line) for line in lines]
print(sum(numbers))


# Part 2
def replace_numbers(word: str) -> str:
    def replace_many(text: str, replace_map: dict) -> str:
        for key, value in replace_map.items():
            if key in text:
                text = text.replace(key, value)
        return text

    # Scrappy, not to lose letters that can be used for other numbers ;)
    word_map = {
        "one": "on1e",
        "two": "tw2o",
        "three": "th3ree",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "si6x",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }

    return replace_many(text=word, replace_map=word_map)


lines = [replace_numbers(line) for line in lines]
numbers = [get_calibration_number(line) for line in lines]
print(sum(numbers))
