import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def is_matching(self, char):
        if self.bracket_type == '[' and char == ']':
            return True
        if self.bracket_type == '{' and char == '}':
            return True
        if self.bracket_type == '(' and char == ')':
            return True
        return False


def bracket_checker(text):
    bracket_stack = []
    for index, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            bracket_stack.append(Bracket(char, index))

        elif char in ("]", ")", "}"):
            if not bracket_stack:
                return index

            top = bracket_stack.pop()
            if not top.is_matching(char):
                return index
    if bracket_stack:
        top = bracket_stack.pop()
        return top.position

    return "Success"


if __name__ == "__main__":
    text = input()
    print(bracket_checker(text))
