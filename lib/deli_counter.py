katz_deli = []


def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
     line_str = " ".join([f"{idx}. {customer}" for idx, customer in enumerate(katz_deli, start=1)])
     print(f"The line is currently: {line_str}")


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        person = katz_deli.pop(0)
        print(f"Currently serving {person}.")