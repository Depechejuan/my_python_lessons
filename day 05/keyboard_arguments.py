def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}!")
    print("Welcome Aboard!")


greet_user("Juan", "Leon")
#Arguments are positional. Position matters. First argument = first variable

# To avoid order, you can do this
greet_user(last_name="Leon", first_name="Juan")
#You MUST every argument, not only some, except in order


def calc_cost(total, shipping, discount):
    print(total, shipping, discount)


#improves readability when complex code. example:
calc_cost(total=50, shipping=5, discount=0.1)